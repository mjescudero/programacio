# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:42:16 2021

@author: MJ
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#scikit-learn Machine Learning in Python

#importar dataset ejemplo
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

digits=datasets.load_digits()

dir(digits)

digits.DESCR

type(digits.images)

digits.images.shape
#1797 filas ( imagenes) de 8*8= 64 pixeles
digits.images[0]
digits.images[0].shape

num=digits.images[0]
num.reshape(1,64)
type(num.reshape(1,64))
num.reshape(1,64).shape

#datos preparados en data, 1797 imagenes de 64 pixeles
digits.data.shape
digits.data[0]


# datos objetivo, valor objetivo
digits.target.shape

digits.target[0:20]

#nombre valores objetivo
digits.target_names

# Dividir los datos para Entrenar y Evaluar el Modelo de Aprendizaje


data_train,data_test, target_train, target_test= train_test_split(digits.data, digits.target, random_state=2)

print(data_train.shape, data_test.shape)
print(target_train.shape, target_test.shape)


#entrenamos el modelo

#modelo_regresion = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)

modelo_regresion = LogisticRegression()
modelo_regresion.fit(data_train, target_train)

type(modelo_regresion)

#provamos el modelo

target_pred = modelo_regresion.predict(data_test)

target_pred.shape

target_pred[0:10]

target_test[0:10]

(target_pred ==target_test).sum()


metrics.accuracy_score(target_test,target_pred)

correct_pred = np.sum(target_test == target_pred)
total_pred = len(target_test)
print("{0} / {1} predicciones correctas".format(correct_pred, total_pred))

mat_con=metrics.confusion_matrix(target_test, target_pred)
print(mat_con)

plt.imshow(mat_con,cmap='Blues', interpolation='nearest')
plt.grid(False)
plt.ylabel('test')
plt.xlabel('predicted')

#Visualizar datos y predicciones

fig, axes = plt.subplots(4,2, figsize=(8,8))
fig.subplots_adjust(hspace=0.1, wspace=0.1)

# axes.flat iterador dels subplots
for i, ax in enumerate(axes.flat):
    ax.imshow(data_test[i].reshape(8, 8), cmap='binary')
    ax.text(0.05, 0.05, target_pred[i], 
            transform=ax.transAxes,# posicio low/lef
            color='green' if (target_test[i] == target_pred[i]) else 'red')
    ax.set_xticks([])
    ax.set_yticks([])
    


from sklearn.cluster import KMeans
# crear model d'agrupació

model= KMeans(n_clusters=10)

clusters = model.fit_predict(digits.data)

clusters.shape
    
model.cluster_centers_.shape    
    
fig = plt.figure(figsize=(8, 3))
for i in range(10):
    ax = fig.add_subplot(2, 5, 1 + i, xticks=[], yticks=[])
    ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap='binary')
    
    
    
    