import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import numpy as np
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

df_test = pd.read_csv('df_area_non_zero_test_mm.csv')
df_test = df_test[df_test['Pothole number'] != 117]
df = pd.read_csv('filtered_potholes_mm_out.csv')
df.columns = df.columns.str.strip()

X = df[['pothole_area']]
y = df['Bags used']

test = df_test[['pothole_area']]


def svr(X, test, y_train, df_test):
    """
    Support Vector Regression with Grid Search.

    Trains a Support Vector Regressor (SVR) model on the provided training data using 
    a grid search to optimize hyperparameters. The best model is then used to predict 
    the target variable on the test data.

    Parameters:
    -----------
    X : pandas.DataFrame
        Features from the training dataset.
    test : pandas.DataFrame
        Features from the test dataset for prediction.
    y_train : pandas.Series
        Target variable (number of bags used) from the training dataset.
    df_test : pandas.DataFrame
        The test dataset, including the 'Pothole number' for output.

    Outputs:
    --------
    - Saves predictions in a CSV file named 'predicted_pothole_bags.csv'.
    - Prints the predicted values.
    """
    param_grid = {
        'C': [0.1, 1, 10, 100, 1000],
        'epsilon': [0.001, 0.01, 0.1, 1],
        'gamma': ['scale', 'auto', 0.01, 0.1, 1],
        'kernel': ['rbf']  
    }
    
    model = SVR()
    
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='r2', verbose=2, n_jobs=-1)
    
    grid_search.fit(X, y_train)
    
    best_model = grid_search.best_estimator_
    
    y_hat = best_model.predict(test)
    print(y_hat)

    result_df = pd.DataFrame({
        'Pothole number': df_test['Pothole number'],
        'Bags used': y_hat
    })
    
    result_df.to_csv('predicted_pothole_bags.csv', index=False)

    
def polynomial_regression_model(X_train, X_test, y_train):
    """
    Polynomial Regression with Grid Search.

    Fits a polynomial regression model to the training data using grid search 
    for hyperparameter tuning. The best model is used to predict the target 
    variable on the test data.

    Parameters:
    -----------
    X_train : pandas.DataFrame
        Training features.
    X_test : pandas.DataFrame
        Test features for prediction.
    y_train : pandas.Series
        Training target variable.

    Outputs:
    --------
    - Saves predictions in 'predicted_pothole_bags.csv'.
    """

    pipeline = Pipeline([
        ('scaler', StandardScaler()),       
        ('poly', PolynomialFeatures()),        
        ('linear', LinearRegression())           
    ])

    param_grid = {
        'poly__degree': [2, 3, 4, 5],           
        'linear__fit_intercept': [True, False]   
    }

    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='r2', verbose=2, n_jobs=-1)

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    y_hat = best_model.predict(X_test)
    
    result_df = pd.DataFrame({
        'Pothole number': df_test['Pothole number'],
        'Bags used': y_hat
    })
    
    result_df.to_csv('predicted_pothole_bags.csv', index=False)


def linear_regression_model(X_train, X_test, y_train, y_test):
    """
    Linear Regression Model.

    Trains a linear regression model on the training data and predicts the 
    target variable on the test data.

    Parameters:
    -----------
    X_train : pandas.DataFrame
        Training features.
    X_test : pandas.DataFrame
        Test features for prediction.
    y_train : pandas.Series
        Training target variable.
    y_test : pandas.Series
        Test target variable (not used in this function).

    Outputs:
    --------
    - Saves predictions in 'predicted_pothole_bags.csv'.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_hat = model.predict(X_test)
    
    result_df = pd.DataFrame({
        'Pothole number': df_test['Pothole number'],
        'Bags used': y_hat
    })
    
    result_df.to_csv('predicted_pothole_bags.csv', index=False)


def gradient_boosting(X_train, X_test, y_train, y_test):
    """
    Gradient Boosting Regression with Grid Search.

    Trains a Gradient Boosting Regressor on the provided training data using 
    grid search to optimize hyperparameters. The best model is used to predict 
    the target variable on the test data.

    Parameters:
    -----------
    X_train : pandas.DataFrame
        Training features.
    X_test : pandas.DataFrame
        Test features for prediction.
    y_train : pandas.Series
        Training target variable.
    y_test : pandas.Series
        Test target variable.

    Outputs:
    --------
    - Saves predictions in 'predicted_pothole_bags.csv'.
    """
    param_grid = {
        'n_estimators': [100, 200, 300],            
        'learning_rate': [0.01, 0.05, 0.1, 0.2],        
        'max_depth': [3, 4, 5],                       
        'min_samples_split': [2, 5, 10],               
        'min_samples_leaf': [1, 2, 4],                 
        'subsample': [0.8, 0.9, 1.0]            
    }
    model_gb = GradientBoostingRegressor(random_state=0)
    grid_search = GridSearchCV(estimator=model_gb, param_grid=param_grid, cv=5, scoring='r2', verbose=2, n_jobs=-1)

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    y_hat = best_model.predict(X_test)

    result_df = pd.DataFrame({
        'Pothole number': df_test['Pothole number'],
        'Bags used': y_hat
    })
    
    result_df.to_csv('predicted_pothole_bags.csv', index=False)


svr(X, test, y, df_test)
