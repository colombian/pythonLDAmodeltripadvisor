from typing import List

from gensim.corpora import dictionary
import gensim.corpora as corpora


def create_dictionary(documents: List[List[str]]): #-> gensim.corpora:
    return corpora.Dictionary(documents)
