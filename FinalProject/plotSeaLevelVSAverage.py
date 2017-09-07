#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:43:39 2017

@author: katiekessler
"""

import pandas as pd
import matplotlib.pyplot as plt

sl = pd.read_csv('CSV Data Set Files for Code/ACI - SL.csv') #get sea level data
avg = pd.read_csv('CSV Data Set Files for Code/ACI - avg.csv') #get avg data

for j in range(4): #go through every season
    for i in range(13): #go through every region
        sl_list = sl[sl.columns[i+2]].tolist() #get sea level for a certain region 
        avg_list = avg[avg.columns[i+2]].tolist() #get avg for same region
        
        plt.title("AVG " + str(list(avg)[i+2])+ " vs " + str(list(sl)[i+2]) + " Season " + str(j+1))
        plt.xlabel("AVG " + str(list(avg)[i+2]))
        plt.ylabel(str(list(sl)[i+2]))
        
        plt.scatter(avg_list[j::4], sl_list[j::4], color='black') #plot avg vs sea level
        plt.show()


