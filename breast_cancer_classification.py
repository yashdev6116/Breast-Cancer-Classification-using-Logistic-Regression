# -*- coding: utf-8 -*-
"""Breast Cancer Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TbjwaQhmWc7qKflDEEVWGAN_0BSBRkhY
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import numpy as np
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data0=pd.read_csv("/content/data.csv")

data0.head()

#OR WE CAN ALSO USE DATASET FROM SKLEARN AND THIS ONE ONLY I WILL BE USING TN THIS PROJECT"
data=sklearn.datasets.load_breast_cancer()

print(data)

#loading the data to a data frame
df=pd.DataFrame(data.data,columns=data.feature_names)

df.head()

df['label']=data.target

df.head()

df.shape

df.info()

df.isnull().sum()

df['label'].value_counts()

df.groupby('label').mean()

X=df.drop(columns='label',axis=1)
Y=df['label']
print(X)

print(Y)

x_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,x_train.shape,X_test.shape)

model=LogisticRegression()

model.fit(x_train,Y_train)

x_train_prediction=model.predict(x_train)
training_data_accuracy=accuracy_score(Y_train,x_train_prediction)

print("Accuracy on Training Data: ",training_data_accuracy)

X_test_prediction=model.predict(X_test)
training_data_accuracy=accuracy_score(Y_test,X_test_prediction)
print("Accuracy on Test Data: ",training_data_accuracy)

input_data=(20.57,17.77,132.9,1326,0.08474,0.07864,0.0869,0.07017,0.1812,0.05667,0.5435,0.7339,3.398,74.08,0.005225,0.01308,0.0186,0.0134,0.01389,0.003532,24.99,23.41,158.8,1956,0.1238,0.1866,0.2416,0.186,0.275,0.08902)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
  print("The Breast Cancer is Malignant")
else:
  print("The Breast Cancer is Benign")