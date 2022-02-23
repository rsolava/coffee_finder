import streamlit as st
import pandas as pd
import numpy as np
import en_core_web_sm

import re
import string

import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA

from scipy.spatial import distance

import pickle

def clean_text(s):
    s = s.lower()
    s = s.replace("check-ins","")
    s = s.replace("check-in","")
    s = re.sub('[%s]' % re.escape(string.punctuation), ' ', s)
    s = re.sub('[%s]' % re.escape(string.digits), ' ', s)
    return s

def lemmatize_document(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])

def find_top_recs(topic_scores, n):
    dists = shop_top_df.apply(lambda x: distance.cosine(x,topic_scores), axis = 1)
    dists = np.where(dists == 0.0, 1, dists)

    best_indices = np.argpartition(dists, n)[:n]
    return [shop_df.SHOP.iloc[i] for i in best_indices]

def recommend_from_text(text,n):
    text = clean_text(text)
    text = lemmatize_document(text)
    dtm = cv.transform([text])
    topic_scores = lda.transform(dtm)
    return find_top_recs(topic_scores,n)


if "iter" not in st.session_state:
    st.session_state["iter"] = 1

    st.session_state["shop_df"] = pickle.load( open("shop_df.p","rb"))
    st.session_state["cv"] = pickle.load(open("cv.p","rb"))
    st.session_state["lda"] = pickle.load(open("lda.p","rb"))

else:
    st.session_state.iter += 1




shop_df = st.session_state.shop_df
shop_top_df = shop_df.drop(columns = ["RATING","SHOP"])
cv = st.session_state.cv
lda = st.session_state.lda
nlp = en_core_web_sm.load()

text = st.text_area("Enter a description of your ideal coffee shop here!")

if st.session_state.iter > 1:

    recs = recommend_from_text(text,5)

    for i in range(0,5):
        st.text(str(i+1) + ". "+ recs[i])
