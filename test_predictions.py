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
# df.columns = df.columns.str.strip()
df = pd.read_csv('filtered_potholes_mm_out.csv')

# df_test['ratio_width'] = df_test['width_0']/df_test['width_1']
# df_test['ratio_height'] = df_test['height_0']/df_test['height_1']

# df= df[df['pothole_area']!=0.0]
# count_0_5 = df[df['Bags used'] == 0.5].shape[0]

# # Determine how many rows to remove, for example, remove 50% of them
# rows_to_remove = int(count_0_5 * 0.5)  # Adjust the percentage as needed

# indices_to_remove = df[df['Bags used'] == 0.5].sample(n=rows_to_remove, random_state=42).index

# df = df.drop(indices_to_remove)
df.columns = df.columns.str.strip()

# df['ratio_width'] = df['width_0']/df['width_1']
# df['ratio_height'] = df['height_0']/df['height_1']

X = df[['pothole_area']]
y = df['Bags used']

test=df_test[['pothole_area']]

def svr(X, test, y_train, y_test, df_test):
    param_grid = {
        'C': [0.1, 1, 10, 100, 1000],
        'epsilon': [0.001, 0.01, 0.1, 1],
        'gamma': ['scale', 'auto', 0.01, 0.1, 1],
        'kernel': ['rbf']  
    }
    
    model = SVR()
    
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='r2', verbose=2, n_jobs=-1)
    
    grid_search.fit(X_train, y_train)
    
    best_model = grid_search.best_estimator_
    
    y_hat = best_model.predict(test)
    print(y_hat)

    result_df = pd.DataFrame({
        'Pothole number': df_test['Pothole number'],
        'Bags used': y_hat
    })
    
    result_df.to_csv('predicted_pothole_bags.csv', index=False)

    
def polynomial_regression_model(X_train, X_test, y_train):

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

# svr(X_train, test, y_train, y_test, df_test)
polynomial_regression_model(X, test, y)

def linear_regression_model(X_train, X_test, y_train, y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_hat = model.predict(X_test)
    
    result_df = pd.DataFrame({
        'Pothole number': df_test['Pothole number'],
        'Bags used': y_hat
    })
    
    result_df.to_csv('predicted_pothole_bags.csv', index=False)
    
# linear_regression_model(X_train, test, y_train, y_test)

def gradient_boosting(X_train, X_test, y_train, y_test):
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
    
# svr(X_train, test, y_train, y_test, df_test)


