#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 13:51:46 2017

@author: katiekessler
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

sl = pd.read_csv('CSV Data Set Files for Code/ACI - SL.csv')
avg = pd.read_csv('CSV Data Set Files for Code/ACI - avg.csv')

for j in range(4): #go through every season
    for i in range(13): #go through every region
        sl_list = sl[sl.columns[i+2]].tolist() #get sea level for a certain region
        avg_list = avg[avg.columns[i+2]].tolist() #get avg for the same region
        
        xo1 = sl_list[j::4] #split the data by season j
        yo1 = avg_list[j::4] #split the data by season j

        #linear regression
        x = np.array(xo1).reshape(-1,1) #shape the data from linear regression
        y = np.array(yo1).reshape(-1,1)

        x_train = x[:43] #split data for training set to be %20
        y_train = y[:43]

        x_test = x[43:] #split data for test set to be %80
        y_test = y[43:]

        regr = linear_model.LinearRegression() #perform linear regression on training set

        regr.fit(x_train, y_train)

        print("R-squared: avg " + str(list(avg)[i+2]) + " " + str(regr.score(x_test,y_test))) #print r-squared value

        
        plt.title("avg " + str(list(avg)[i+2])+ " vs " + str(list(sl)[i+2]) + " Season " + str(j+1))
        plt.xlabel("avg " + str(list(avg)[i+2]))
        plt.ylabel(str(list(sl)[i+2]))
        
        plt.scatter(avg_list[j::4], sl_list[j::4], color='black') #plot data and linear regression line
        plt.plot(x_test, regr.predict(x_test), color='blue', linewidth=3)
        plt.show()
