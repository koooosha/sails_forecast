import numpy as np
from sklearn.metrics import mean_absolute_percentage_error

def performance_eval(y_true:list, y_pred:list): 
    '''this function calculates the performance metrics'''
    mse = ((y_pred - y_true) ** 2).mean()
    
    #mape= np.mean(np.abs((y_true - y_pred) / (y_true))) * 100
    mape = np.mean([np.abs(yt - yp)*100/yt for yt,yp in zip(y_true,y_pred) if yt != 0])
    performance_data= {'MSE':round(mse, 2),
                      'RMSE':round(np.sqrt(mse), 2),
                       'MAPE':round(mape, 2)
                      }
    return performance_data