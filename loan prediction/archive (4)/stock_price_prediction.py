import pandas as pd 
import numpy as np 
from sklearn import metrics 
import matplotlib. pyplot as pit

dataset = pd.read_csv("A_data.csv")
print(dataset.head(101))

# setting the format of date month/date/year
dataset['date'] = pd.to_datetime(dataset.date)

print("(Total rows, Total coloumns) = ", dataset.shape)

#checking the null values 
print(dataset.isnull().sum())

print(dataset.describe())

#dataset['close'].plot(figsize=(16,6))
 
x = dataset[['open', 'high', 'low', 'volume']]
y = dataset['close']

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(x ,y , random_state = 0)

print(X_train.shape)
print(X_test.shape)

from sklearn. linear_model import LinearRegression
from sklearn. metrics import confusion_matrix, accuracy_score
regressor = LinearRegression()
regressor.fit(X_train,y_train)
print(regressor.coef_)
print (regressor. intercept_)
predicted=regressor. predict (X_test)
print(X_test)

dframe=pd.DataFrame(y_test, predicted)
dfr=pd.DataFrame ({f'Actual Price' : y_test, 'Predicted Price' : predicted})
print(dfr.head(25))

graph = dfr.head(20)
graph.plot.bar()

                