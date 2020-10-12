
import tensorflow as tf

from transformers import *
import pandas as pd
import numpy as np
from konlpy.tag import Okt
import re

import sys

import logging
import os
import unicodedata
from shutil import copyfile

# from transformers import PreTrainedTokenizer

logger = logging.getLogger(__name__)

VOCAB_FILES_NAMES = {"vocab_file": "tokenizer_78b3253a26.model",
                     "vocab_txt": "vocab.txt"}

PRETRAINED_VOCAB_FILES_MAP = {
    "vocab_file": {
        "monologg/kobert": "https://s3.amazonaws.com/models.huggingface.co/bert/monologg/kobert/tokenizer_78b3253a26.model",
        "monologg/kobert-lm": "https://s3.amazonaws.com/models.huggingface.co/bert/monologg/kobert-lm/tokenizer_78b3253a26.model",
        "monologg/distilkobert": "https://s3.amazonaws.com/models.huggingface.co/bert/monologg/distilkobert/tokenizer_78b3253a26.model"
    },
    "vocab_txt": {
        "monologg/kobert": "https://s3.amazonaws.com/models.huggingface.co/bert/monologg/kobert/vocab.txt",
        "monologg/kobert-lm": "https://s3.amazonaws.com/models.huggingface.co/bert/monologg/kobert-lm/vocab.txt",
        "monologg/distilkobert": "https://s3.amazonaws.com/models.huggingface.co/bert/monologg/distilkobert/vocab.txt"
    }
}

PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES = {
    "monologg/kobert": 64,
    "monologg/kobert-lm": 64,
    "monologg/distilkobert": 64
}

PRETRAINED_INIT_CONFIGURATION = {
    "monologg/kobert": {"do_lower_case": False},
    "monologg/kobert-lm": {"do_lower_case": False},
    "monologg/distilkobert": {"do_lower_case": False}
}

SPIECE_UNDERLINE = u'▁'


class KoBertTokenizer(PreTrainedTokenizer):
    """
        SentencePiece based tokenizer. Peculiarities:
            - requires `SentencePiece <https://github.com/google/sentencepiece>`_
    """
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    pretrained_init_configuration = PRETRAINED_INIT_CONFIGURATION
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES

    def __init__(
            self,
            vocab_file,
            vocab_txt,
            do_lower_case=False,
            remove_space=True,
            keep_accents=False,
            unk_token="[UNK]",
            sep_token="[SEP]",
            pad_token="[PAD]",
            cls_token="[CLS]",
            mask_token="[MASK]",
            **kwargs):
        super().__init__(
            unk_token=unk_token,
            sep_token=sep_token,
            pad_token=pad_token,
            cls_token=cls_token,
            mask_token=mask_token,
            **kwargs
        )

        # Build vocab
        self.token2idx = dict()
        self.idx2token = []
        with open(vocab_txt, 'r', encoding='utf-8') as f:
            for idx, token in enumerate(f):
                token = token.strip()
                self.token2idx[token] = idx
                self.idx2token.append(token)

        self.max_len_single_sentence = self.max_len - 2  # take into account special tokens
        self.max_len_sentences_pair = self.max_len - 3  # take into account special tokens

        try:
            import sentencepiece as spm
        except ImportError:
            logger.warning(
                "You need to install SentencePiece to use KoBertTokenizer: https://github.com/google/sentencepiece"
                "pip install sentencepiece")

        self.do_lower_case = do_lower_case
        self.remove_space = remove_space
        self.keep_accents = keep_accents
        self.vocab_file = vocab_file
        self.vocab_txt = vocab_txt

        self.sp_model = spm.SentencePieceProcessor()
        self.sp_model.Load(vocab_file)

    @property
    def vocab_size(self):
        return len(self.idx2token)

    def __getstate__(self):
        state = self.__dict__.copy()
        state["sp_model"] = None
        return state

    def __setstate__(self, d):
        self.__dict__ = d
        try:
            import sentencepiece as spm
        except ImportError:
            logger.warning(
                "You need to install SentencePiece to use KoBertTokenizer: https://github.com/google/sentencepiece"
                "pip install sentencepiece")
        self.sp_model = spm.SentencePieceProcessor()
        self.sp_model.Load(self.vocab_file)

    def preprocess_text(self, inputs):
        if self.remove_space:
            outputs = " ".join(inputs.strip().split())
        else:
            outputs = inputs
        outputs = outputs.replace("``", '"').replace("''", '"')

        if not self.keep_accents:
            outputs = unicodedata.normalize('NFKD', outputs)
            outputs = "".join([c for c in outputs if not unicodedata.combining(c)])
        if self.do_lower_case:
            outputs = outputs.lower()

        return outputs

    def _tokenize(self, text, return_unicode=True, sample=False):
        """ Tokenize a string. """
        text = self.preprocess_text(text)

        if not sample:
            pieces = self.sp_model.EncodeAsPieces(text)
        else:
            pieces = self.sp_model.SampleEncodeAsPieces(text, 64, 0.1)
        new_pieces = []
        for piece in pieces:
            if len(piece) > 1 and piece[-1] == str(",") and piece[-2].isdigit():
                cur_pieces = self.sp_model.EncodeAsPieces(piece[:-1].replace(SPIECE_UNDERLINE, ""))
                if piece[0] != SPIECE_UNDERLINE and cur_pieces[0][0] == SPIECE_UNDERLINE:
                    if len(cur_pieces[0]) == 1:
                        cur_pieces = cur_pieces[1:]
                    else:
                        cur_pieces[0] = cur_pieces[0][1:]
                cur_pieces.append(piece[-1])
                new_pieces.extend(cur_pieces)
            else:
                new_pieces.append(piece)

        return new_pieces

    def _convert_token_to_id(self, token):
        """ Converts a token (str/unicode) in an id using the vocab. """
        return self.token2idx.get(token, self.token2idx[self.unk_token])

    def _convert_id_to_token(self, index, return_unicode=True):
        """Converts an index (integer) in a token (string/unicode) using the vocab."""
        return self.idx2token[index]

    def convert_tokens_to_string(self, tokens):
        """Converts a sequence of tokens (strings for sub-words) in a single string."""
        out_string = "".join(tokens).replace(SPIECE_UNDERLINE, " ").strip()
        return out_string

    def build_inputs_with_special_tokens(self, token_ids_0, token_ids_1=None):
        """
        Build model inputs from a sequence or a pair of sequence for sequence classification tasks
        by concatenating and adding special tokens.
        A RoBERTa sequence has the following format:
            single sequence: [CLS] X [SEP]
            pair of sequences: [CLS] A [SEP] B [SEP]
        """
        if token_ids_1 is None:
            return [self.cls_token_id] + token_ids_0 + [self.sep_token_id]
        cls = [self.cls_token_id]
        sep = [self.sep_token_id]
        return cls + token_ids_0 + sep + token_ids_1 + sep

    def get_special_tokens_mask(self, token_ids_0, token_ids_1=None, already_has_special_tokens=False):
        """
        Retrieves sequence ids from a token list that has no special tokens added. This method is called when adding
        special tokens using the tokenizer ``prepare_for_model`` or ``encode_plus`` methods.
        Args:
            token_ids_0: list of ids (must not contain special tokens)
            token_ids_1: Optional list of ids (must not contain special tokens), necessary when fetching sequence ids
                for sequence pairs
            already_has_special_tokens: (default False) Set to True if the token list is already formated with
                special tokens for the model
        Returns:
            A list of integers in the range [0, 1]: 0 for a special token, 1 for a sequence token.
        """

        if already_has_special_tokens:
            if token_ids_1 is not None:
                raise ValueError(
                    "You should not supply a second sequence if the provided sequence of "
                    "ids is already formated with special tokens for the model."
                )
            return list(map(lambda x: 1 if x in [self.sep_token_id, self.cls_token_id] else 0, token_ids_0))

        if token_ids_1 is not None:
            return [1] + ([0] * len(token_ids_0)) + [1] + ([0] * len(token_ids_1)) + [1]
        return [1] + ([0] * len(token_ids_0)) + [1]

    def create_token_type_ids_from_sequences(self, token_ids_0, token_ids_1=None):
        """
        Creates a mask from the two sequences passed to be used in a sequence-pair classification task.
        A BERT sequence pair mask has the following format:
        0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1
        | first sequence    | second sequence
        if token_ids_1 is None, only returns the first portion of the mask (0's).
        """
        sep = [self.sep_token_id]
        cls = [self.cls_token_id]
        if token_ids_1 is None:
            return len(cls + token_ids_0 + sep) * [0]
        return len(cls + token_ids_0 + sep) * [0] + len(token_ids_1 + sep) * [1]

    def save_vocabulary(self, save_directory):
        """ Save the sentencepiece vocabulary (copy original file) and special tokens file
            to a directory.
        """
        if not os.path.isdir(save_directory):
            logger.error("Vocabulary path ({}) should be a directory".format(save_directory))
            return

        # 1. Save sentencepiece model
        out_vocab_model = os.path.join(save_directory, VOCAB_FILES_NAMES["vocab_file"])

        if os.path.abspath(self.vocab_file) != os.path.abspath(out_vocab_model):
            copyfile(self.vocab_file, out_vocab_model)

        # 2. Save vocab.txt
        index = 0
        out_vocab_txt = os.path.join(save_directory, VOCAB_FILES_NAMES["vocab_txt"])
        with open(out_vocab_txt, "w", encoding="utf-8") as writer:
            for token, token_index in sorted(self.token2idx.items(), key=lambda kv: kv[1]):
                if index != token_index:
                    logger.warning(
                        "Saving vocabulary to {}: vocabulary indices are not consecutive."
                        " Please check that the vocabulary is not corrupted!".format(out_vocab_txt)
                    )
                    index = token_index
                writer.write(token + "\n")
                index += 1

        return out_vocab_model, out_vocab_txt


tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert')




def create_sentiment_bert():
    # 버트 pretrained 모델 로드
    SEQ_LEN = 64
    model = TFBertModel.from_pretrained("monologg/kobert", from_pt=True)
    # 토큰 인풋, 마스크 인풋, 세그먼트 인풋 정의
    token_inputs = tf.keras.layers.Input((SEQ_LEN,), dtype=tf.int32, name='input_word_ids')
    mask_inputs = tf.keras.layers.Input((SEQ_LEN,), dtype=tf.int32, name='input_masks')
    segment_inputs = tf.keras.layers.Input((SEQ_LEN,), dtype=tf.int32, name='input_segment')
    # 인풋이 [토큰, 마스크, 세그먼트]인 모델 정의
    bert_outputs = model([token_inputs, mask_inputs, segment_inputs])

    bert_outputs = bert_outputs[1]
    sentiment_first = tf.keras.layers.Dense(4, activation='softmax',
                                            kernel_initializer=tf.keras.initializers.TruncatedNormal(0.02))(
        bert_outputs)
    sentiment_model = tf.keras.Model([token_inputs, mask_inputs, segment_inputs], sentiment_first)
    # 옵티마이저는 간단하게 Adam 옵티마이저 활용
    sentiment_model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.00001),
                            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                            metrics=['sparse_categorical_accuracy'])
    return sentiment_model


def mean_answer_label(*preds):
    preds_sum = np.zeros(preds[0].shape[0])
    for pred in preds:
        preds_sum += np.argmax(pred, axis=-1)
    return np.round(preds_sum / len(preds), 0).astype(int)


mod = sys.modules[__name__]


def sentence_convert_data(data):
    SEQ_LEN = 64
    global tokenizer

    tokens, masks, segments = [], [], []
    token = tokenizer.encode(data, max_length=SEQ_LEN, pad_to_max_length=True)
    # token = tokenizer.encode(data)

    num_zeros = token.count(0)
    mask = [1] * (SEQ_LEN - num_zeros) + [0] * num_zeros
    segment = [0] * SEQ_LEN

    tokens.append(token)
    segments.append(segment)
    masks.append(mask)

    tokens = np.array(tokens)
    masks = np.array(masks)
    segments = np.array(segments)
    return [tokens, masks, segments]


def category_evaluation_predict(sentence):
    cat_dict = {'0': "기쁨", '1': "슬픔", '2': "화남", '3': "중립"}
    global mod
    sentence = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…]+", "", sentence)
    sentence = re.sub("\\n+", " ", sentence)
    sentence = re.sub("\\t+", " ", sentence)
    data_x = sentence_convert_data(sentence)
    print(data_x)

    path = "C:/Users/multicampus/PycharmProjects/s03p23a201/backend/ML/bert_test/"
    sentiment_model.load_weights(os.path.join(path, "sentiment_model55.h5"))

    # setattr(mod, 'chung', sentiment_model)
    setattr(mod, 'emo', sentiment_model.predict(data_x, batch_size=1))

    print("확인", sentiment_model.predict(data_x, batch_size=1))
    print("이모 ",emo)
    for e in emo[0]:
        print(e)

    def plus_dic_val(emo_score, emo):
        ai_weight = 0.6
        dic_weight = 1 - ai_weight

        for i in range(0, len(emo[0])):
            emo[0][i] = emo[0][i]*ai_weight + emo_score[i]*dic_weight
            print("ee ", emo[0][i])
        print(emo)




    #감성사전
    okt = Okt()

    NRC = pd.read_csv("C:/Users/multicampus/PycharmProjects/s03p23a201/backend/ML/data/after_change_csv.csv",
                header=None,)

    NRC = NRC[(NRC != 0).all(1)]

    # 인덱스 번호 리셋
    NRC = NRC.reset_index(drop=True)

    ko_stopwords = pd.read_csv("C:/Users/multicampus/PycharmProjects/s03p23a201/backend/ML/data/ko_stopwords.txt",
                  engine="python", header=None, sep="\n")
    pos_review = sentence
    stop_words = ko_stopwords

    raw = pos_review.lower()
    tokens = okt.morphs(pos_review)
    print(raw)
    print(tokens)
    stopped_tokens = [i for i in tokens if not i in stop_words] # 불용어 제거
    match_words = [x for x in stopped_tokens if x in list(NRC[0])] # 사전과 매칭
    print("stop",stopped_tokens)
    print(match_words)
    emotion=[]
    for i in match_words:
        temp = list(NRC.iloc[np.where(NRC[0] == i)[0],1])
        for j in temp:
            emotion.append(j)

    # sentiment_result1 = pd.Series(emotion).value_counts()
    # print("asdasd  ",sentiment_result1[0])
    emo_score = [0, 0, 0, 1]
    ai_weight = 0.7
    dic_weight = 1 - ai_weight
    if len(emotion) != 0:
        emo_score = [0,0,0,1/len(emotion)]
        for i in emotion:
            if i == 'Positive' or i == 'Anticipation' or i =='Joy' or i =='Trust' or i =='Surprise':
                emo_score[0]+=1
            elif i == 'Negative':
                emo_score[1]+=1
                emo_score[2]+=1
            elif i == 'Sadness' or i =='Fear':
                emo_score[1] += 1
            elif i == 'Anger' or i =='Disgust':
                emo_score[2]+=1

            # print("dd ",i)
            # print(emo_score)
        for i in range(len(emo_score)-1):
            emo_score[i] = emo_score[i]/len(emo_score)

        plus_dic_val(emo_score, emo)


        # print(emo_score)
    # print(sentiment_result1, sentiment_result1.plot.bar(), raw)

    preds = str(mean_answer_label(emo).item())
    for pred in preds:
        print("프레드 ", pred)
    print(preds)


    if preds == '0':
        print(cat_dict[preds], "  입니다.")
    elif preds == '1':
        print(cat_dict[preds], "  입니다.")
    elif preds == '2':
        print(cat_dict[preds], "  입니다.")
    elif preds == '3':
        print(cat_dict[preds], "  입니다.")
    else:
        print("노답")


sentiment_model = create_sentiment_bert()

# sentiment_model.load_weights(os.path.join("bert", "sentiment_model.h5"))

chungwon = """보컬이 진짜 중요한 게 메이트 노래 중에 내 띵곡은 전부 임헌일곡들. 사실 메이트 음악색 자체는 임헌일이 더 컸는데, 결국 갈라서선 보컬이 강한 정준일이 더 잘나감(물론 정준일이 만든 노래, 부른 노래도 엄청 좋아하지만)"""
print(chungwon, category_evaluation_predict(chungwon))

chungwon = "오늘은 아빠와 함께 바다에 갔다 정말 재미있는 하루였다"
print(chungwon, category_evaluation_predict(chungwon))

chungwon = "숙제가 너무 많아서 힘이 빠진다...숙제하기 싫다..."
print(chungwon, category_evaluation_predict(chungwon))

chungwon = "그 새끼는 왜 그러는지 모르겠다 개빡친다"
print(chungwon, category_evaluation_predict(chungwon))

chungwon = "내가 좋아하던 배우가 죽었다. 너무 슬펐다"
print(chungwon, category_evaluation_predict(chungwon))

chungwon = "하늘도 꿀꿀하고 우울했다."
print(chungwon, category_evaluation_predict(chungwon))

chungwon = "오랜만에 친구들과 함께 영화를 보았다. 맛있는 피자도 먹었다. 행복한 하루였다"
print(chungwon, category_evaluation_predict(chungwon))

chungwon = "박근혜 하야하라"
print(chungwon, category_evaluation_predict(chungwon))