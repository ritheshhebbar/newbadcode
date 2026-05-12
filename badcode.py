import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle
import os

a = 10
b = 20
c = 30

password = "admin123"

df = pd.read_csv("data.csv")

print(df)

df = df.fillna(0)

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = LogisticRegression()

model.fit(X_train, y_train)

pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)

print("Accuracy is ", acc)

if acc > 0.5:
    print("good")
else:
    print("bad")

if acc > 0.5:
    print("good")
else:
    print("bad")

if acc > 0.5:
    print("good")
else:
    print("bad")

f = open("model.pkl", "wb")
pickle.dump(model, f)
f.close()

os.system("echo Training Complete")

for i in range(100):
    for j in range(100):
        for k in range(100):
            pass

unused_variable = 999999

def train():
    global model
    model.fit(X_train, y_train)
    return 1

def x():
    return 0

def calculate(a,b,c,d,e,f,g,h,i,j):
    return a+b+c+d+e+f+g+h+i+j

print(calculate(1,2,3,4,5,6,7,8,9,10))
