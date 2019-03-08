# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 21:34:54 2019

@author: PERSONALISE NOTEBOOK
"""

# Import Library 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import all of data 
dataset = pd.read_csv('TestsetTugas1ML.csv')
datatrain = pd.read_csv('TrainsetTugas1ML.csv')

greater50 = datatrain[datatrain['income'] == '>50K']
less50 = datatrain[datatrain['income'] == '<=50K']

probGreat = len(greater50) / len(datatrain)
probLess = len(less50) / len(datatrain)

# Make function probabilistic every value in every atribut
def countProb(col, val1, val2, val3):
    matriks = []
    temp = []
    temp.append(len(greater50[greater50[col] == val1]) / len(greater50))
    temp.append(len(greater50[greater50[col] == val2]) / len(greater50))
    temp.append(len(greater50[greater50[col] == val3]) / len(greater50))
    
    matriks.append(temp)
    temp = []
    
    temp.append(len(less50[less50[col] == val1]) / len(less50))
    temp.append(len(less50[less50[col] == val2]) / len(less50))
    temp.append(len(less50[less50[col] == val3]) / len(less50))
    matriks.append(temp)
    
    matriks = pd.DataFrame(matriks, columns=[val1,val2,val3])
    matriks = matriks.rename(index={matriks.index[0]: '>50K', matriks.index[1]: '<=50K'})
    
    return matriks

# Count function probabilistic every value in every atribut in datatrain
age = countProb('age', 'young', 'adult','old')
workclass = countProb('workclass', 'Self-emp-not-inc', 'Private','Local-gov')
education = countProb('education', 'HS-grad', 'Some-college','Bachelors')
marital = countProb('marital-status', 'Never-married', 'Married-civ-spouse','Divorced')
occupation = countProb('occupation', 'Craft-repair', 'Exec-managerial','Prof-specialty')
relationship = countProb('relationship', 'Not-in-family', 'Husband','Own-child')
hours = countProb('hours-per-week', 'low', 'many','normal')

# Make function to classify the result
def classify(arr) :
    great = 1
    less = 1
    for j in range (len(arr)) :
        great *= arr[j][0]
        less *= arr[j][1]
    great *= probGreat
    less *= probLess
    if great > less : return '>50K'
    else : return '<=50K'

matriksResult = []    
temp = []
for i in range (len(dataset)) :
    temp.append(age[dataset.iloc[i][1]])
    temp.append(workclass[dataset.iloc[i][2]])
    temp.append(education[dataset.iloc[i][3]])
    temp.append(marital[dataset.iloc[i][4]])
    temp.append(occupation[dataset.iloc[i][5]])
    temp.append(relationship[dataset.iloc[i][6]])
    temp.append(hours[dataset.iloc[i][7]])
    matriksResult.append(classify(temp))
    temp = []

matriksResult = pd.DataFrame(matriksResult)      
matriksResult.to_csv("TebakanTugas1ML.csv", sep=',')
