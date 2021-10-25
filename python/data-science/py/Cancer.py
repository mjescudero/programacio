# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:39:26 2021

@author: MJ
"""

import matplotlib.pyplot as plt
import  numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn.metrics import  confusion_matrix, r2_score
from sklearn.model_selection import train_test_split


diabetes=datasets.load_diabetes()
df= pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

df.describe()
 
m_corr = df.corr()
 
 # pintar la matriu de corr
 import seaborn as sbnsbn.heatmap(m_corr, annot=True)
 sbn.heatmap(m_corr, annot=True)
 plot.show()
 
 
  sbn.jointplot( data=df, x= "s3", y="s4", kind="hex", color= 'red')
  
  sbn.jointplot( data=df, x= "s3", y="s4", kind="kde", color= 'red')
  
  x_vars=["age"]
  y_vars=["bmi","bp"]
  
g=sbn.pairplot(df,x_vars=x_vars,y_vars=y_vars,hue='target',diag_kind="auto", palette='pastel')
g.fig.legend(labels=breast.target_names)

 g=sbn.pairplot(df,x_vars=x_vars,y_vars=y_vars,diag_kind="auto", palette='pastel', hue='sex')
g.fig.legend(labels=)

from datetime import datetime
