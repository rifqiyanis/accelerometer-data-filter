# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:49:00 2021

@author: rifqi
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('7.csv')
X = df.iloc[:, 1]

def mvaFilter(data,window_size):
  hasil = data.rolling(window=window_size).mean()
  return hasil

mvaFilter(X,50).plot(label ='MVA')
plt.plot(X, label='X', alpha = 0.5)