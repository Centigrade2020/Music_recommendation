import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from joblib import load, dump


def suggestions(age, gender):
    model = load('trained.joblib')
    return model.predict([[age, gender]])
