#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 13:52:33 2017

@author: katiekessler
@author of RandomForest Regressor code: tobes898
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor

#Can be used for every file, just need to change the file names below
sl = pd.read_csv('CSV Data Set Files for Code/ACI - SL.csv')
rx5 = pd.read_csv('CSV Data Set Files for Code/ACI - rx5.csv')

for j in range(4): #go through every season
    for i in range(13): #go through every region
        sl_list = sl[sl.columns[i+2]].tolist()
        rx5_list = rx5[rx5.columns[i+2]].tolist() #

        xo1 = sl_list[j::4]
        yo1 = rx5_list[j::4]

       #builiding the random forest regressor
        x = np.array(xo1).reshape(-1,1)
        y = np.array(yo1).ravel()

        #Making train sets
        x_train = x[:-43]
        y_train = y[:-43]

        #Making test sets
        x_test = x[-43:]
        y_test = y[-43:]

        #declaring the actual Random Forest Regressor
        regr = RandomForestRegressor()

        #fitting the graphs to the sets
        regr.fit(x_train, y_train)

        #Printing out the data as well as the graphs
        print("R-squared: " + str(list(rx5)[i+2]) + " " + str(regr.score(x_test,y_test)))

        plt.title(str(list(rx5)[i+2])+ " vs " + str(list(sl)[i+2]) + " Season " + str(j+1))
        plt.xlabel(str(list(rx5)[i+2]))
        plt.ylabel(str(list(sl)[i+2]))

        plt.scatter(rx5_list[j::4], sl_list[j::4], color='black')
        plt.plot(x_test, regr.predict(x_test), color='blue', linewidth=3)
        plt.show()







    


