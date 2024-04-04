import pandas as pd


def load_data(path:str) -> pd.DataFrame:
    ''' this function loads data from a csv file'''
    data = pd.read_csv(path)
    data['datum'] = pd.to_datetime(data.datum)
    data.set_index("datum", inplace= True)
    return data