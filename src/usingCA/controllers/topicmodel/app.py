import os
import io
import sys
import numpy as np
import pickle

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# spacy for lemmatization
import spacy
import en_core_web_sm

# NLTK Stop words
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
nlp = en_core_web_sm.load()

# Tokenize words and Clean-up text
def sent_to_words(documents):
    for doc in documents:
        yield(gensim.utils.simple_preprocess(str(doc), deacc=True))  # deacc=True removes punctuations
# Remove Stopwords
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]
# Lemmatize
def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'ADV']):
    """https://spacy.io/api/annotation"""
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        #texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        texts_out.append([token.lemma_ for token in doc])
    return texts_out
def takeSecond(elem):
    return elem[1]
def flatRecom(seq):
    seen_bl = set()
    seen_add_bl = seen_bl.add
    return [x for x in seq if not (x[0] in seen_bl or seen_add_bl(x[0]))]
def getNumRecs(max_num_recs):
    try:
      num_recs = int(sys.argv[2]) if int(sys.argv[2])<=max_num_recs else max_num_recs
      return num_recs
    except:
      return 5

class DataLoader:
  def __init__(self, dir):
    self.id2word = corpora.Dictionary.load(dir+'/dict1')
    self.corpus = corpora.MmCorpus(dir+'/corpus1.mm')
    self.lda_model = gensim.models.ldamodel.LdaModel.load(dir+'/lda1.model')
    self.num_topic = 100
    self.max_num_recs = 50
    with open(dir+"/recommendations.pickle", "rb") as i_file:
      self.recs = pickle.load(i_file)

def main():
  # load data
  dir = sys.argv[0].replace('/app.py','')
  data = DataLoader(dir)
  id2word, corpus, lda_model, recs, num_topic, max_num_recs = data.id2word, data.corpus, data.lda_model, data.recs, data.num_topic, data.max_num_recs
  # user input
  u_input = sys.argv[1]
  num_recs = getNumRecs(max_num_recs)
  preprocessed_input = lemmatization(remove_stopwords(list(sent_to_words([u_input]))))
  ans = [id2word.doc2bow(text) for text in preprocessed_input]
  # transform user input to a topic distribution
  doc_vec = lda_model[ans[0]][0]
  ans_vec = [0]*num_topic
  for doc in doc_vec:
    ans_vec[doc[0]] = doc[1]
  response = []
  # rank recommendations
  for rec in recs:
    for i,z in enumerate(rec[0]):
      response.append([rec[1], ans_vec[i]*z[1]])
  response = sorted(response, key=takeSecond, reverse=True)
  response = flatRecom(response)
  # output ranked recommendations (dict)
  print({r[0]: r[1] for r in response[:num_recs]})

if __name__ == "__main__":
  main()
