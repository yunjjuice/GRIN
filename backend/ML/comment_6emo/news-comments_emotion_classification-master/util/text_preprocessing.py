import numpy as np
from konlpy.tag import Okt
from konlpy.tag import Mecab


def tokenize_okt(comment):
    """
    ** 참고 - konlpy.Okt 패키지 사용 **

    :param comment: 뉴스 댓글 문장 하나
    :return: 문장을 token단위로 쪼갠 후 리스트로 반환

    """
    okt = Okt()
    malist = okt.pos(comment, norm=True, stem=True)
    r = []

    tag_list = ['Noun', "Verb", 'Adjective', "Adverb", "Determiner", "Exclamation", "Emotion"]

    # 불용어 추가
    stopwords = ['하다', ',', '들', '이', '..', '.', '것', '다', '이다', '~', '그', '그녀', '저', '...', '"', '~~']

    try:
        for word, tag in malist:
            if tag in tag_list:
                if not word in stopwords:
                    r.append(word)
        return r
    except Exception as e:
        print(e)

def tokenize_mecab(sentence):
    mecab = Mecab()
    result = [x for x in mecab.nouns(sentence) if len(x)>1]
    return result


def count_comment(token_data):
    unique_comment_tokenized = [list(i) for i in set(tuple(i) for i in token_data)]
    word_dic = {}

    # word count
    for words in unique_comment_tokenized:
        for word in words:
            if not (word in word_dic):
                word_dic[word] = 0
            word_dic[word] += 1

    keys = sorted(word_dic.items(), key = lambda x: x[1], reverse = True)
    for word, count in keys[:50]:
        print("{0}({1}) ".format(word, count), end = "")

    # [] 없애주는 코드
    from itertools import chain
    words = set(chain(*unique_comment_tokenized))

    n_vocab = len(words)
    print("")
    print("Total Vocab: ", n_vocab)
    print("")

    return keys, n_vocab



def preprocess(text):
    '''
    말뭉치 단어 별로 아이디로 변환해주는 함수
    :param text:
    :return:
    '''
    # 간단한 전처리
    text = text.lower()
    text = text.replace('.', ' .')
    words = text.split(' ')

    # 단어를 Id로
    word_to_id = {}
    id_to_word = {}
    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    corpus = np.array([word_to_id[w] for w in words])

    return corpus, word_to_id, id_to_word