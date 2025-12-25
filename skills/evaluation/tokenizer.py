from pythainlp import word_tokenize
from pythainlp.corpus.common import thai_stopwords
import re

stopwords = set(thai_stopwords())
len(stopwords)

def preprocess_thai(text):
    # engine="newmm" <- default
    # tokens = word_tokenize(text, engine="newmm", keep_whitespace=False)
    text = re.sub(r"[^ก-๙a-zA-Z\s]", "", text)  # remove non-text symbols
    tokens = word_tokenize(text, engine="attacut", keep_whitespace=False)
    tokens = [t for t in tokens if t not in stopwords and len(t) > 1]
    return tokens