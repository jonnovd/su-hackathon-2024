import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('model_data.csv')
df.columns = df.columns.str.strip()

X = df.drop(['Bags used'], axis=1)

y = df['Bags used']

y_class = pd.Categorical(y).codes

X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=0)

softmax_reg = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
softmax_reg.fit(X_train, y_train)

rf_class = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
rf_class.fit(X_train,y_train)

y_pred_soft = softmax_reg.predict(X_test)
y_pred_rf = rf_class.predict(X_test)

accuracy_soft = accuracy_score(y_test, y_pred_soft)
print(f'Accuracy on Softmax: {accuracy_soft:.2f}')
print("\nClassification Report:")
print(classification_report(y_test, y_pred_soft))

accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f'Accuracy on RF: {accuracy_rf:.2f}')
print("\nClassification Report:")
print(classification_report(y_test, y_pred_rf))