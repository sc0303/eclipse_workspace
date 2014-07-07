#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#coding=utf-8  
#import os 
from pylab import *
# import matplotlib.plot
# from matplotlib import all
from pandas import Series,DataFrame
import pandas as pd

'''
Created on 2014年6月30日

@author: Alance
'''
  
 
if __name__ == '__main__':
    print  'hello'
    
    x = linspace( 0, 10, 100 )
    plot(x, sin(x) )
#     show()
    
    s = Series([1,2,3.0,'abc'])
    print s
    print '中文'
    pass