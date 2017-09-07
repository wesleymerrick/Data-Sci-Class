#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:16:00 2017

@author: katiekessler
"""


import pandas as pd
import matplotlib.pyplot as plt

sl = pd.read_csv('CSV Data Set Files for Code/ACI - SL.csv') #get sea level data
rx5 = pd.read_csv('CSV Data Set Files for Code/ACI - rx5.csv') #get rx5 data

for j in range(4): #go through every season
    for i in range(13): #go through every region
        sl_list = sl[sl.columns[i+2]].tolist() #get sea level for a certain region 
        rx5_list = rx5[rx5.columns[i+2]].tolist() #get rx5 for same region
        
        plt.title(str(list(rx5)[i+2])+ " vs " + str(list(sl)[i+2]) + " Season " + str(j+1))
        plt.xlabel(str(list(rx5)[i+2]))
        plt.ylabel(str(list(sl)[i+2]))
        
        plt.scatter(rx5_list[j::4], sl_list[j::4], color='black') #plot rx5 vs sea level
        plt.show()
