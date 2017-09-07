#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 22:36:46 2017

@author: karlmaier
"""

#imports un order to read in data, plot, and linear regression 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

#using pandas, reda in the csv
sl = pd.read_csv('CSV Data Set Files for Code/ACI - SL.csv')#read in the sea level csv from our csv folder 
other = pd.read_csv('CSV Data Set Files for Code/ACI - CDD.csv')#read in the cdd csv from csv folder 


for j in range(4):# for loop that loops through the every season of each year
    for i in range(13):# for loop that loops through the entire list of regions for every season since it is within the season for loop
        sl_list = sl[sl.columns[i+2]].tolist()# create a sea level list that holds all data for the sea level except the headers
        other_list = other[other.columns[i+2]].tolist()#create a list of the other csv used except the headers

        xo = sl_list[j::4]#gets every 4th starting at j. If j = 0 that is every first season 
        #if j =1 that is the second and so on
        yo = other_list[j::4]

        x = np.array(xo).reshape(-1,1)#reshape the array data for linear regression
        y = np.array(yo).reshape(-1,1)

        x_train = x[:43]#data split for our training set 80%
        y_train = y[:43]

        x_test = x[43:]#data split for our test set 20%
        y_test = y[43:]

        regr = linear_model.LinearRegression()#linear regression call to actually run linear regression

        regr.fit(x_train, y_train)#fits the linear model
        
        #Plot the data
        plt.title(str(list(other)[i+2])+ " vs " + str(list(sl)[i+2]) + " Season " + str(j+1))
        #add the title off the other list with region vs sea level list with region and season
        plt.xlabel(str(list(other)[i+2]))#add the x axis label to be the other list without the headers of the data
        plt.ylabel(str(list(sl)[i+2]))#add the y axis label to be the sea level list without the headers of the data
        
        
        #compute the R squared values using regr.score to see how the line created differs in error
        print("R-Squared: " + str(list(other)[i+2]) + " " + str(regr.score(x_test,y_test)))
        
        #show the plot with the line colored blue
        plt.scatter(x, y, color='black')
        plt.plot(x_test, regr.predict(x_test), color='blue', linewidth=3)
        plt.show()
