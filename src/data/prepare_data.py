import pandas as pd
from pandas import DataFrame

def read_sample() -> DataFrame:
    df = pd.read_csv('data/raw/tripadvisor.csv')

    return df