from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import grangercausalitytests
import pandas as pd
import plotly.graph_objects as go
def checking_stationary(ts:list,ts_name:str)->bool:
    '''This function runs adfuller test for checking if a timeserie is stationary or not!!'''
    result = adfuller(ts)
    p_value = result[1]
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print(f'{key}: {value}')
    if p_value < 0.05:
        print(f"The TimeSerie {ts_name} is Stationary!!")
        return True
    else:
        print(f"The timeserie {ts_name} is not stationary!!")
        return False
    
    

def ts_seasonal_decompose(ts:pd.DataFrame, ts_name:str):
    '''This function decompose a time series into trend, seasonal and residual components in additive form'''
    ts_decompose = seasonal_decompose(ts, model='additive')
    ts_trend = ts_decompose.trend
    ts_season = ts_decompose.seasonal
    ts_res = ts_decompose.resid
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=ts_trend.index.tolist(), y=ts_trend, mode = "lines" ,name = "Trend"))
    fig.update_layout(title=f'Time Series Data decomposition-Trend: {ts_name}', \
        xaxis_title='Date', yaxis_title='Decomposed Elements')
    fig.show()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x= ts_season.index.tolist(), y=ts_season, mode = "lines" ,name = "Seasonal"))
    fig.update_layout(title=f'Time Series Data decomposition-Seasonality: {ts_name}', \
        xaxis_title='Date', yaxis_title='Decomposed Elements')
    fig.show()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x= ts_season.index.tolist(), y = ts_res, mode = "lines" , name = "Residual"))
    fig.update_layout(title=f'Time Series Data decomposition-Residual: {ts_name}', \
        xaxis_title='Date', yaxis_title='Decomposed Elements')
    fig.show()
    return ts_trend, ts_season, ts_res


def grag_test(data:pd.DataFrame, max_lag:int):
    '''This function runs the grangercausality test to check the causal relation between multi time series'''
    grag_result = grangercausalitytests(data,maxlag=max_lag)
    return grag_result