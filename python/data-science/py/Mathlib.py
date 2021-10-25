# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 19:53:40 2020

@author: MJ
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

#pwd 'C:\\Users\\MJ\\documents\\python\\aprendiz-data-science-master\\notebooks'
data= pd.read_csv('../datasets/world-development-indicators/Indicators.csv')
data.shape

countries= data['CountryName'].unique().tolist()
indicators= data['IndicatorName'].unique().tolist()

#247 paisos
len(countries)
#1344 indicadors
len(indicators)
#56 anys 
len(data.Year.unique())

#filtre 1
yearsFilter=[2010, 2011, 2012, 2013, 2014]

#Filtre 2 dos paisos a l'atzar
countryFilter= random.sample(countries,2)
countryFilter

#filtre 3, l'indicador

indicatorFilter= random.sample(indicators, 1)
indicatorFilter

#no tots el paisos tenen dades pel tots els indicadors i anys

filterMesh= (data['CountryName'] == countryFilter[0]) & (data['IndicatorName'].isin(indicatorFilter)) & (data['Year'].isin(yearsFilter))
country1_data = data.loc[filterMesh]
len(country1_data)


filterMesh2= (data['CountryName'] == countryFilter[1]) & (data['IndicatorName'].isin(indicatorFilter)) & (data['Year'].isin(yearsFilter))
country2_data = data.loc[filterMesh2]
len(country2_data)

#no tots els paisos tenen dades per tots els indicador ni tots els anys, consultem quins
filtercountry= ((data['IndicatorName'].isin(indicatorFilter)) & (data['Year'].isin(yearsFilter)))
countries_years= data.loc[filtercountry]
len(countries_years.CountryName.unique())

data[['IndicatorName', 'CountryName']]\
    .groupby('CountryName').count()
    
data[['IndicatorName', 'CountryName','Year']]\
    .groupby(['CountryName', 'IndicatorName']).count()


data.loc[data.CountryName=='Afghanistan'].IndicatorName.unique()
data.loc[lambda df: df['CountryName']=='Afghanistan']

#recollim numes els indicadors y paisos que tenen dades pel mateis rang d'anys

filteredData1 = []
filteredData2 = []

# problem - not all countries have all indicators so if you go to visualize, it'll have missing data.
# randomly picking two indicators and countries, do these countries have valid data over those years.
# brings up the discussion of missing data/ missing fields
# until we find full data

while(len(filteredData1) < len(yearsFilter)-1):
    # pick new indicator
    indicatorsFilter = random.sample(indicators, 1)
    countryFilter    = random.sample(countries, 2)
    # how many rows are there that have this country name, this indicator, and this year.  Mesh gives bool vector
    filterMesh = (data['CountryName'] == countryFilter[0]) & (data['IndicatorName'].isin(indicatorsFilter)) & (data['Year'].isin(yearsFilter))
    # which rows have this condition to be true?
    filteredData1 = data.loc[filterMesh]
    filteredData1 = filteredData1[['CountryName','IndicatorName','Year','Value']]

    # need to print this only when our while condition is true
    if(len(filteredData1) < len(yearsFilter)-1):
        print('Skipping ... %s since very few rows (%d) found' % (indicatorsFilter, len(filteredData1)))

indicatorsFilter

countryFilter

filterMesh.sum()

filteredData1


plt.scatter(filteredData1['Year'], filteredData1['Value'])

filteredData1[[ 'Value', 'Year']].plot(x='Year', y='Value',figsize=(10,5), grid=True)
# Label the axes
plt.xlabel('Year')
plt.ylabel(indicatorsFilter[0])
plt.xticks(yearsFilter)
#label the figure
plt.title('Evolución indicador en '+ countryFilter[0])
plt.show()



'''
Country 2
'''

while(len(filteredData2) < len(filteredData1)-1):
    filterMesh = (data['CountryName'] == countryFilter[1]) & (data['IndicatorName'].isin(indicatorsFilter)) & (data['Year'].isin(yearsFilter))
    filteredData2 = data.loc[filterMesh]
    filteredData2 = filteredData2[['CountryName','IndicatorName','Year','Value']]
    #pick new indicator
    old = countryFilter[1]
    countryFilter[1]    = random.sample(countries, 1)[0]
    
    if(len(filteredData2) < len(filteredData1)-1):
        print('Skipping ... %s, since very few rows (%d) found' % (old, len(filteredData2)))


filteredData2[[ 'Value', 'Year']].plot(x='Year', y='Value',figsize=(10,5), color='green',grid=True)
plt.xlabel('Year')
plt.ylabel(indicatorsFilter[0])
plt.xticks(yearsFilter)
#label the figure
plt.title('Evolución indicador en '+ filteredData2['CountryName'].iloc[0] )
plt.show()



plt.plot(filteredData1['Year'].values, filteredData1['Value'].values, 'g-', label=countryFilter[0])
plt.legend()

#para ver mejos los datos comparados hemos multiplicadi por 3000  para cambiar la escala
plt.plot(filteredData2['Year'].values, filteredData2['Value'].values,'r-',label=countryFilter[1])
plt.legend()
# Etiquetamos los ejes
plt.xlabel('Year')
plt.ylabel(indicatorsFilter[0])
plt.xticks(yearsFilter)

plt.show()


if len(filteredData1) < len(filteredData2):
    small = len(filteredData1)
else:
    small = len(filteredData2)

filteredData1=filteredData1[0:small]
filteredData2=filteredData2[0:small]



fig, axis = plt.subplots()
axis.yaxis.grid(True)
# axis.grid(True) 
axis.set_title(indicatorsFilter[0])
axis.set_xlabel(filteredData1['CountryName'].iloc[0],fontsize=10)
axis.set_ylabel(filteredData2['CountryName'].iloc[0],fontsize=10)

X = filteredData1['Value']
Y = filteredData2['Value']

axis.scatter(X, Y)

# directament plot
plt.scatter(filteredData1['Value'],filteredData2['Value'],edgecolors='red')
plt.legend()
plt.grid(True, axis='y')
plt.xlabel(filteredData1['CountryName'].iloc[0])
plt.ylabel(filteredData2['CountryName'].iloc[0])
plt.title(indicatorsFilter[0])



fig, ax = plt.subplots(figsize=(20, 10))

ax.set_ylim( min(0,filteredData1['Value'].min()) , 2*filteredData1['Value'].max())
ax.set_title('Indicator Name : ' + indicatorsFilter[0])

ax.plot(filteredData1['Year'], filteredData1['Value'] , 'r--', label=filteredData1['CountryName'].unique()) 

legend=plt.legend(loc = 'upper center', 
                    shadow=True,
                    prop={'weight':'roman','size':'xx-large'})
# Rectangle around the legend
frame = legend.get_frame()
frame.set_facecolor('.95')
plt.show()


#plot country2
fig, ax = plt.subplots(figsize=(20, 10))

# Adjust the lower and upper limit to bring the graph at center
ax.set_ylim(min(0,filteredData2['Value'].min()), 2*filteredData2['Value'].max())

ax.set_title('Indicator Name : ' + indicatorsFilter[0])
ax.plot(filteredData2['Year'], filteredData2['Value'] ,
         label=filteredData2['CountryName'].unique(),
         color="purple", lw=1, ls='-', 
         marker='s', markersize=20, 
         markerfacecolor="yellow", markeredgewidth=4, markeredgecolor="blue") 

# Add the legend
legend = plt.legend(loc = 'upper left', 
                    shadow=True,
                    prop={'weight':'roman','size':'xx-large'})

# Rectangle around the legend
frame = legend.get_frame()
frame.set_facecolor('lightgreen')
plt.show()

# random datasets
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

countof_angles = 36
countof_radii  = 8

# array - radii
array_rad = np.linspace(0.125, 1.0, countof_radii)

# array - angles
array_ang = np.linspace(0, 2*np.pi, countof_angles, endpoint=False)

# crea una matriu de valors de angles repetits 8 vegades, per cada fila,
# 36x8 on el valor de cada dila del array_ang, es repetis 8 cops per fila, 
# primer en de convertir array_ang en matriu de 36 files i 1 columna amb 
# array_ang[...,np.newaxis]
matriu_ang = np.repeat(array_ang[...,np.newaxis], countof_radii, axis=1)

# from polar (radii, angles) coords to cartesian (x, y) coords
x = np.append(0, (array_rad*np.cos(matriu_ang)).flatten())
y = np.append(0, (array_rad*np.sin(matriu_ang)).flatten())

# saddle shaped surface
z = np.sin(-x*y)
fig = plt.figure(figsize=(20,10))
ax  = fig.gca(projection='3d')
ax.plot_trisurf(x, y, z, cmap=cm.autumn, linewidth=0.2)
plt.show()







fig, ax = plt.subplots(3,2,figsize=(20, 10))

ax[0,0].set_ylim( min(0,filteredData1['Value'].min()) , 2*filteredData1['Value'].max())
ax[0,0].set_title('Indicator Name : ' + indicatorsFilter[0])
ax[0,0].plot(filteredData1['Year'], filteredData1['Value'] , 'r--', label=filteredData1['CountryName'].unique()) 
legend=ax[0,0].legend(loc = 'upper center', 
                    shadow=True,
                    prop={'weight':'roman','size':'xx-large'})
# Rectangle around the legend
frame = legend.get_frame()
frame.set_facecolor('.95')

ax[0,1].set_ylim(min(0,filteredData2['Value'].min()), 2*filteredData2['Value'].max())
ax[0,1].set_title('Indicator Name : ' + indicatorsFilter[0])
ax[0,1].plot(filteredData2['Year'], filteredData2['Value'] ,
         label=filteredData2['CountryName'].unique(),
         color="purple", lw=1, ls='-', 
         marker='s', markersize=20, 
         markerfacecolor="yellow", markeredgewidth=4, markeredgecolor="blue") 

# Add the legend
legend = ax[0,1].legend(loc = 'upper left', 
                    shadow=True,
                    prop={'weight':'roman','size':'xx-large'})
# Rectangle around the legend
frame = legend.get_frame()
frame.set_facecolor('lightgreen')
plt.show()




# un atra forma de crear subpolts de diferents mides
fig = plt.figure()
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
fig.tight_layout()
