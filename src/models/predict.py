import pandas as pd 
import pickle

from src.features.tokenize import tokenize
from src.features.dictionary import create_dictionary
from src.features.utils import clean_up_text

#import gensim
#from typing import List
#from src.features import nlp
#from src.data.prepare_data import read_sample
#from gensim.models import CoherenceModel

def load_model():
    with open(r"models/model.pkl", "rb") as input_file:
        model = pickle.load(input_file)
    return(model)

def predict(model,text:str):
    text      = pd.DataFrame(data={'review':[text]}, columns=['review'])
    doc       = clean_up_text(text)
    lemma     = tokenize(doc)
    id2word   = create_dictionary(lemma)
    corpus    = [id2word.doc2bow(text) for text in lemma]
    prediction= model[corpus]

    topics = list()
    for prob in prediction[0][1]:
        for topic in prob[1]:
            topics.append(topic)
    moda = max(set(topics), key=topics.count)
    topics = model.print_topics()[moda]
    return topics
    
# how to test
# >>> from src.models.test import *
# >>> model = load_model()
# >>> test = predict(model, 'Best SPA, attention 10/10. Amazing food and experience!! 100% recommended. Massages are great, rooms are clean and location is great. Definitely going to come back! If you want to have the whole Antigua experience don’t hesitate to choose this hotel.')