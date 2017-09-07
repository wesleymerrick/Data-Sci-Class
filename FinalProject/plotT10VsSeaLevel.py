#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:27:15 2017

@author: katiekessler
"""


import pandas as pd
import matplotlib.pyplot as plt

sl = pd.read_csv('CSV Data Set Files for Code/ACI - SL.csv') #get sea level data
t10 = pd.read_csv('CSV Data Set Files for Code/ACI - t10.csv') #get t10 data

for j in range(4): #go through every season
    for i in range(13): #go through every region
        sl_list = sl[sl.columns[i+2]].tolist() #get sea level for a certain region 
        t10_list = t10[t10.columns[i+2]].tolist() #get t10 for same region
        
        plt.title(str(list(t10)[i+2])+ " vs " + str(list(sl)[i+2]) + " Season " + str(j+1))
        plt.xlabel(str(list(t10)[i+2]))
        plt.ylabel(str(list(sl)[i+2]))
        
        plt.scatter(t10_list[j::4], sl_list[j::4], color='black') #plot t10 vs sea level
        plt.show()
