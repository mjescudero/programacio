# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:55:55 2021

@author: MJ
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import sklearn.metrics as m

np.random.seed(0)
X = np.random.random(size=(20, 1))
print(X)

y = 3 * X.squeeze() + 2 + np.random.randn(20)
print(y)

#plt.scatter(X,Y)
plt.plot(X,y, 'o')

modelo_reg= LinearRegression()
modelo_reg.fit(X,y)

X_fit = np.linspace(0, 1, 20)[:, np.newaxis]
y_fit = modelo_reg.predict(X_fit)

# si cambiamos el modelo hay que ver que coeficientes tiene cada modelo
print("Coefficients: \n", modelo_reg.coef_)
print("Intercept: \n", modelo_reg.intercept_)

modelo_reg.coef_*X_fit[0] + modelo_reg.intercept_== y_fit[0]


plt.plot(X.squeeze(), y, 'o')
plt.plot(X_fit.squeeze(), y_fit)
plt.grid()

error = mean_squared_error(y_fit, y)
error = np.sqrt(error)
print(error)


# R^2 (coefficient of determination) regression score function.
m.r2_score(y, y_fit)


# Random forest

modelo_rforest= RandomForestRegressor()
modelo_rforest.fit(X,y)
X_fit = np.linspace(0, 1, 20)[:, np.newaxis]
y_fit = modelo_rforest.predict(X_fit)

plt.plot(X.squeeze(), y, 'o')
plt.plot(X_fit.squeeze(), y_fit)
plt.grid()

error = mean_squared_error(y_fit, y)
error = np.sqrt(error)
print(error)


len(modelo_rforest.estimators_)

 modelo_rforest.estimators_[0].feature_importances_
 modelo_rforest.estimators_[1].feature_importances_

import sklearn.metrics as m

# best score 1 
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score
# multioutput default=’uniform_average
m.r2_score(y, y_fit)

#from sklearn.metrics import confusion_matrix
