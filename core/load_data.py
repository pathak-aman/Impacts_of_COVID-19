import pandas as pd

def load_dataframe(from_url = False): 
    if from_url:
        url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
        return pd.read_csv("url")
    else:
        return pd.read_csv("data/data.csv")
        