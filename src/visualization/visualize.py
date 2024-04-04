import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as xp
import seaborn as sn


def vis_target_ts():
    '''this function plots the time series'''
    fig1 = go.Figure()
    fig2 = go.Figure()
    fig1.add_trace(go.Scatter(x=data.index.tolist(), y=data["vkmge"], mode = "lines" ,name = "Sales"))
    fig2.add_trace(go.Scatter(x=data.index.tolist(), y=data["a"], mode = "lines" ,name = "Sales"))

    fig1.update_layout(title='Time Series Data : vkp_mge', xaxis_title='Date', yaxis_title='sales quantity')
    fig2.update_layout(title = 'Time_Series_Data : a', xaxis_title = 'Date', yaxis_title = "A")
    fig1.show()
    fig2.show()
    
    
def vis_target_ts(data:pd.DataFrame):
    '''this function plots the time series'''
    fig1 = go.Figure()
    fig2 = go.Figure()
    fig1.add_trace(go.Scatter(x=data.index.tolist(), y=data["vkmge"], mode = "lines" ,name = "Sales"))
    fig2.add_trace(go.Scatter(x=data.index.tolist(), y=data["a"], mode = "lines" ,name = "Sales"))
    fig1.update_layout(title='Time Series Data : vkp_mge', xaxis_title='Date', yaxis_title='sales quantity')
    fig2.update_layout(title = 'Time_Series_Data : a', xaxis_title = 'Date', yaxis_title = "A")
    fig1.show()
    fig2.show()
    
def vis_monthly(data_season,feat):
    vk_month = data_season.groupby("month")[feat].mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=vk_month.index, y=vk_month.values, mode = "lines" ,name = "Monthly Sales"))
    fig.update_layout(title=f'Monthly Time Series Visualization : {feat}', xaxis_title='Month', yaxis_title='sales quantity')
    fig.show()
    
def vis_year_month(data_season, feat):
    vk_year_month = pd.DataFrame(data_season.groupby(["month","year"])[feat].mean()).reset_index()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=vk_year_month[vk_year_month["year"]==2018].month, y=vk_year_month[vk_year_month["year"]==2018]\
        [feat], mode = "lines" ,name = "Monthly Sales 2018"))
    fig.add_trace(go.Scatter(x=vk_year_month[vk_year_month["year"]==2019].month, y=vk_year_month[vk_year_month["year"]==2019]\
        [feat], mode = "lines" ,name = "Monthly Sales 2019"))
    fig.update_layout(title=f'Monthly Time Series Visualization : {feat}', xaxis_title='Month', yaxis_title='sales quantity')
    fig.show()
    
def vis_box_month(data_season, feat):
    fig = xp.box(data_season, y=feat, x="month", title= f"Box Plot {feat} : Monthly Sales")
    fig.show()
    
def vis_week_day(data_season,feat):
    data_season['weekday_name'] = pd.Categorical(data_season['weekday_name'],\
        categories=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], ordered=True)
    vk_weekday = data_season.groupby("weekday_name")[feat].mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=vk_weekday.index, y=vk_weekday.values, mode = "lines" ,name = "Daily Sales"))
    fig.update_layout(title=f'Daily Time Series Visualization : {feat}', xaxis_title='Week days', yaxis_title='sales quantity')
    fig.show()
    
def vis_quarter_w_day(data_season,feat):
    vk_quarter_day_week = pd.DataFrame(data_season.groupby(["quarter","weekday_name"])[feat].mean()).reset_index()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=vk_quarter_day_week[vk_quarter_day_week["quarter"]==1].\
        weekday_name, y=vk_quarter_day_week[vk_quarter_day_week["quarter"]==1]\
        [feat], mode = "lines" ,name = "Quarter 1"))
    fig.add_trace(go.Scatter(x=vk_quarter_day_week[vk_quarter_day_week["quarter"]==2].\
        weekday_name, y=vk_quarter_day_week[vk_quarter_day_week["quarter"]==2]\
        [feat], mode = "lines" ,name = "Quarter 2"))
    fig.add_trace(go.Scatter(x=vk_quarter_day_week[vk_quarter_day_week["quarter"]==3].\
        weekday_name, y=vk_quarter_day_week[vk_quarter_day_week["quarter"]==3]\
        [feat], mode = "lines" ,name = "Quarter 3"))
    fig.add_trace(go.Scatter(x=vk_quarter_day_week[vk_quarter_day_week["quarter"]==4].\
        weekday_name, y=vk_quarter_day_week[vk_quarter_day_week["quarter"]==4]\
        [feat], mode = "lines" ,name = "Quarter 4"))
    fig.update_layout(title=f'Weekday_Quarter Time Series Visualization : {feat}', xaxis_title='Week_Day', yaxis_title='sales quantity')
    fig.show()
    
def vis_box_quarter(data_season, feat):
    fig = xp.box(data_season, y=feat, x="quarter", title=f"Box Plot {feat} : Quarter Sales")
    fig.show()
    
def vis_model_eval(test_ts:pd.DataFrame, forecast_df:pd.DataFrame):
    plt.figure(figsize=(10, 6))
    plt.plot(test_ts.index, test_ts['vkmge'], label='Actual vkmge', color='blue')
    plt.plot(forecast_df.index, forecast_df['vkmge'], label='Forecasted vkmge', linestyle='--', color='red')
    plt.title('Forecasted vkmge vs Actual vkmge')
    plt.xlabel('Date')
    plt.ylabel('vkmge')
    plt.legend()
    plt.grid(True)
    plt.show()