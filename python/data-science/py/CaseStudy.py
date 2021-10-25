# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:49:33 2020

@author: MJ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pwd='C:/Users/MJ/documents/codi/python/aprendiz-data-science-master/notebooks'
data = pd.read_csv('C:/Users/MJ/documents/codi/python/data-science/datasets/world-development-indicators/Indicators.csv')
data.shape


countries = data['CountryName'].unique().tolist()
len(countries)

countryCodes = data['CountryCode'].unique().tolist()
len(countryCodes)

indicators = data['IndicatorName'].unique().tolist()
len(indicators)

years = data['Year'].unique().tolist()
len(years)

data['CountryCode'].value_counts()[:20].plot(kind='bar')

Indicator_mean=data[['Value','IndicatorName']].groupby("IndicatorName").agg({'Value':np.mean})



mask = data['IndicatorName'].str.contains('CO2')
indicators = data[mask]
print(indicators['IndicatorName'].head())

indCO2= data[data['IndicatorName'].str.contains('CO2')]['IndicatorName'].unique()
len(indCO2)

#Seleccionamos un país y un indicador para explorar:
hist_indicator = 'CO2 emissions \(metric tons per capita\)'
hist_country = 'ESP'
mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['CountryCode'].str.contains(hist_country) 
stage = data[mask1 & mask2]

stage.plot(x="Year", y='Value',figsize=(10,8), title='CO2 Emissions')

stage[['Year', 'Value']].plot(x= 'Year', y='Value',kind ='scatter')

stage.plot( x="Year", y='Value',figsize=(10,8),kind ='line',
           xticks=range(stage["Year"].min(),stage["Year"].max(),5))

plt.plot(stage['Year'].values, stage['Value'].values,'r.')

#També podeu crear aquests altres gràfics utilitzant els mètodes DataFrame.plot.<kind>
#en lloc de proporcionar l' kindargument de paraula clau. Això fa que sigui més fàcil 
#descobrir els mètodes de trama i els arguments específics que utilitzen:
#df.plot.area     df.plot.barh     df.plot.density  df.plot.hist     df.plot.line     df.plot.scatter
#df.plot.bar      df.plot.box      df.plot.hexbin   df.plot.kde      df.plot.pie


plt.bar(stage['Year'], stage['Value'])

# Consultamos los años
years = stage['Year'].values
# Consultamos los valores de CO2
co2 = stage['Value'].values

# Creamos un Diagrama de Barras
plt.bar(years,co2)
plt.show()


# switch to a line plot
plt.plot(stage['Year'].values, stage['Value'].values)

# Label the axes
plt.xlabel('Year')
plt.ylabel(stage['IndicatorName'].iloc[0])

#label the figure
plt.title('Emisiones de CO2 en España')

# Podemos seleccionar el rango de datos que queremos representar 
#xmim, ymax, ymin,ymax

#plt.axis([1950, 2012,0,13])

# o por separado
plt.xticks(range(stage["Year"].min(),stage["Year"].max(),5))
plt.yticks(range(0,16,2))
plt.show()


#distribució valors
stage.boxplot(column='Value')

plt.hist(co2, 10, normed=False, facecolor='green')

plt.xlabel(stage['IndicatorName'].iloc[0])
plt.ylabel('# of Years')
plt.title('Histogram Example')

plt.grid(True)

plt.show()


################comparamos con otros paises###################

# select CO2 emissions for all countries in 2011
hist_indicator = 'CO2 emissions \(metric'
hist_year = 2011

mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['Year'].isin([hist_year])

# apply our mask
co2_2011 = data[mask1 & mask2]
co2_2011.count()

co2_2011.loc[co2_2011["CountryCode"]=='ESP']

# Histograma con las emisiones per capita por país


# subplots returns a touple with the figure, axis attributes.
fig, ax = plt.subplots()

ax.annotate("ESP",
            xy=(6, 60), xycoords='data',
            xytext=(18, 90), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )

plt.hist(co2_2011['Value'], 10, normed=False, facecolor='green')

plt.xlabel(co2_2011['IndicatorName'].iloc[0])
plt.ylabel('# of Countries')
plt.title('Histogram of CO2 Emissions Per Capita')

#plt.axis([10, 22, 0, 14])
plt.grid(True)

plt.show()


plt.hist(co2_2011['Value'], [0,5,10,20,30,40], normed=False, facecolor='green')
plt.hist(co2_2011['Value'], range(0,40,5), normed=False, facecolor='green')



# Seleccionamos Indicador y País
hist_indicator = 'GDP per capita \(constant 2005'
hist_country = 'ESP'

mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['CountryCode'].str.contains(hist_country)

# Consultamos los Datos aplicando los filtros definidos
gdp_stage = data[mask1 & mask2]


#Creamos un Diagrama verde linea y rojo puntos

plt.plot(gdp_stage['Year'].values, gdp_stage['Value'].values, 'g-')

#para ver mejos los datos comparados hemos multiplicadi por 3000  para cambiar la escala
plt.plot(stage['Year'].values, stage['Value'].values*3000,'r.')

# Etiquetamos los ejes
plt.xlabel('Year')
plt.ylabel(gdp_stage['IndicatorName'].iloc[0])

# Definimos el título del Diagrama
plt.title('PIB per capita ESP')

# Definimos los ejes del diagrama
#plt.axis([1959, 2011,0,25])

plt.show()


############################### amb 2 subplots################
fig = plt.figure(figsize=plt.figaspect(0.5))

axis = fig.add_subplot(1, 2, 1)

axis.yaxis.grid(True)
axis.set_title('GDP \(per capita\)',fontsize=10)
axis.set_xlabel("Year")
axis.set_ylabel(gdp_stage['IndicatorName'].iloc[0])

axis.plot(gdp_stage['Year'].values, gdp_stage['Value'].values, 'g-')

# añadimos el segundo plot con las emisiones de CO2

axis = fig.add_subplot(1, 2, 2)
axis.yaxis.grid(True)
# Etiquetamos los ejes
axis.set_xlabel('Year')
axis.set_ylabel(stage['IndicatorName'].iloc[0])

# Definimos el título del Diagrama
axis.set_title('CO2 Emissions')

axis.plot(stage['Year'].values, stage['Value'].values,'r.')

plt.show()

#######################################




# Consultamos el Rango de Años con Datos Disponibles
print("GDP Min Year = ", gdp_stage['Year'].min(), "max: ", gdp_stage['Year'].max())
print("CO2 Min Year = ", stage['Year'].min(), "max: ", stage['Year'].max())

# Tenemos que igualar el número de valores para crear un Diagrama de Dispersión,  necesitamos el mismo numero de registros
gdp_stage_trunc = gdp_stage[gdp_stage['Year'] < 2012]
print(len(gdp_stage_trunc))
print(len(stage))




fig, axis = plt.subplots()
# Grid lines, Xticks, Xlabel, Ylabel

axis.yaxis.grid(True)
axis.set_title('CO2 Emissions vs. GDP \(per capita\)',fontsize=10)
axis.set_xlabel(gdp_stage_trunc['IndicatorName'].iloc[0],fontsize=10)
axis.set_ylabel(stage['IndicatorName'].iloc[0],fontsize=10)

X = gdp_stage_trunc['Value']
Y = stage['Value']

axis.scatter(X, Y)
plt.show()


##### igual pero sense subplots
plt.scatter(gdp_stage_trunc['Value'],stage['Value'])
# Etiquetamos los ejes
plt.xlabel(gdp_stage_trunc['IndicatorName'].iloc[0],fontsize=10)
plt.ylabel(stage['IndicatorName'].iloc[0],fontsize=10)

# Definimos el título del Diagrama
plt.title('CO2 Emissions vs. GDP \(per capita\)',fontsize=10)

plt.show()


# Calculemos la Correlación entre PIB y Emisiones de CO2
np.corrcoef(gdp_stage_trunc['Value'],stage['Value'])





fig, axis = plt.subplots()

axis.bar(stage['Year'].values,stage['Value'].values)

plt.show()

