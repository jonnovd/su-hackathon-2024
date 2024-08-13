import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv('model_data.csv')
# Correcting for potential whitespace
df.columns = df.columns.str.strip()
print(df.head())
# Adjusting the column name if it's slightly different
X = df.drop(['Bags used'], axis=1)

y = df['Bags used']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model_lr = LinearRegression()
model_rf = RandomForestRegressor(n_estimators=1000, random_state=0)

model_lr.fit(X_train,y_train)
model_rf.fit(X_train, y_train)

y_pred_lr = model_lr.predict(X_test)
y_pred_rf = model_rf.predict(X_test)

mse_lr = mean_squared_error(y_test,y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test,y_pred_rf)

print(f'Mean Squared Error on Linear Regression model: {mse_lr:.2f}')
print(f'R-squared on Linear Regression model: {r2_lr:.2f}')
print(f'Mean Squared Error on RF model: {mse_rf:.2f}')
print(f'R-squared on RF model: {r2_rf:.2f}')

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_lr, color='blue', edgecolor='k', alpha=0.6, label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Ideal Fit')

# Labeling the plot
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Predicted vs. Actual Values')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
