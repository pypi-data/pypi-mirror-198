"""
In this module we get the 2 datasets and apply 2 model on them.We have 2 datasets: boston & wine. Also we have 2 models:linear & tree. 
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn import datasets
from utils import reg,load_data
import argparse 



# Function definition
def reg(model_type,X_train,y_train,X_test,y_test):
    """
    In this function, it gives model_type,X_train,y_train,X_test,y_test and retuns y_pred & y_test_pred. 
    """
    if model_type == "linear":
        model = LinearRegression()

    elif model_type == "tree":
        model = DecisionTreeRegressor()

    else:
        raise Exception(f"model {model_type} does not exist!")


    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)

    # Predicting Test data with the model
    y_test_pred = model.predict(X_test)

    # Model Evaluation
    acc_linreg = metrics.r2_score(y_test, y_test_pred)
    print('MAE:',metrics.mean_absolute_error(y_test, y_test_pred))
    print('R^2:', acc_linreg)
    print('Adjusted R^2:',1 - (1-metrics.r2_score(y_test, y_test_pred))*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1))
    print('MSE:',metrics.mean_squared_error(y_test, y_test_pred))
    print('RMSE:',np.sqrt(metrics.mean_squared_error(y_test, y_test_pred)))




def load_data(data_type):
    """
    In this functin, we load 2 datasets data.
    """
    if data_type == "boston":
        d= datasets.load_boston()
        df = pd.DataFrame(d["data"], columns=d["feature_names"])
        X = d["data"]
        y = d["target"]

    elif data_type == "wine":
        d  = datasets.load_wine()
        df = pd.DataFrame(d["data"], columns=d["feature_names"])
        X = d["data"]
        y = d["target"]

    else:
        raise Exception(f"data_type {data_type} does not exist!")


    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 4)


    return X_train, X_test, y_train, y_test



 

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_type', help="select data type ", required=True)
    parser.add_argument('--model_type', help="select model", required=True)
    args = parser.parse_args()

    print("running model: ",args.model_type,"with data: " , args.data_type)
    X_tr, X_ts, y_tr, y_ts = load_data(args.data_type)
    reg(args.model_type,X_tr,y_tr,X_ts,y_ts)
    
