import pandas as pd
import time

from gensim.models import word2vec


def load_data(path):
    """
    :param path: 파일 주소
    :return: 뉴스 댓글 dataframe
    """
    # mac
    all_daum_txt = open(path, 'r', encoding='cp949')
    i = 0
    news_id = []
    comment_id = []
    comments = []

    while True:
        line = all_daum_txt.readline()
        if not line: break
        n_id = line.split("|$|")[0]  # news_id
        news_id.append(n_id)
        c_id = line.split("|$|")[1]  # comment_id
        comment_id.append(c_id)
        temp = line.split("|$|")[4]  # comment
        comments.append(temp)
        i += 1

    print(i)
    print("@@@@@@")

    daum_data = pd.DataFrame([news_id, comment_id, comments])
    daum_data = daum_data.T
    daum_data.columns = ["news_id", "comment_id", "comment"]
    return daum_data


def load_news_data(path):
    """
    :param path: 파일 주소
    :return: 뉴스 dataframe
    """
    # mac
    all_daum_txt = open(path, 'r', encoding='cp949')
    i = 0
    news_id = []
    news_title = []
    news_content = []

    while True:
        line = all_daum_txt.readline()
        if not line: break
        n_id = line.split("|$|")[0]  # news_id
        news_id.append(n_id)
        n_title = line.split("|$|")[1]  # news_title
        news_title.append(n_title)
        n_content = line.split("|$|")[2]  # news_contents
        news_content.append(n_content)
        i += 1

    print(i)
    print("@@@@@@")

    daum_news_df = pd.DataFrame([news_id, news_title, news_content])
    daum_news_df = daum_news_df.T
    daum_news_df.columns = ["news_id", "title", "content"]
    return daum_news_df



def load_word2vec(w2v_path):
    # word2vec 모델 불러오기
    start = time.time()
    print("word2vec 모델 불러오기 ... ", end="", flush=True)
    w2v_model = word2vec.Word2Vec.load(w2v_path)
    print("finished in {:.2f} sec.".format(time.time() - start), flush=True)

    # 벡터 노말라이즈 해서 용량 대폭 감소시킴
    w2v_model.wv.init_sims(replace=True)

    # about model
    word_vectors = w2v_model.wv.vectors
    word_idxs = w2v_model.wv.index2word
    n_words = word_vectors.shape[0]
    vec_size = word_vectors.shape[1]
    print("#words = {0}, vector size = {1}".format(n_words, vec_size))

    return w2v_model
