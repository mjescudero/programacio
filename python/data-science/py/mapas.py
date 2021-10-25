# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:38:19 2020

@author: MJ
"""
import folium
import pandas as pd


country_geo = 'C:/Users/MJ/documents/python/aprendiz-data-science-master/datasets/world-countries.json'
print(country_geo)

data = pd.read_csv('C:/Users/MJ/documents/python/aprendiz-data-science-master/datasets/world-development-indicators/Indicators.csv')
data.shape

# Seleccionamos los Datos
hist_indicator = 'CO2 emissions \(metric'
hist_year = 2011

# Creamos los Filtros
mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['Year'].isin([hist_year])

# Aplicamos los Filtros
stage = data[mask1 & mask2]
stage.head()

plot_data = stage[['CountryCode','Value']]
#filter_a = stage['CountryCode'] == 'CHN'
#filter_b = stage['CountryCode'] == 'IND'
#plot_data = stage[(stage['CountryCode'] == 'CHN') | (stage['CountryCode'] == 'IND')] 
plot_data.head()


# Seleccionamos la Etiqueta para el Diagrama
hist_indicator = stage.iloc[0]['IndicatorName']
print(hist_indicator)

#leer fichero gjon 
paisos=pd.read_json(country_geo)
print(type(paisos))
#data frame paisos

paisos.head()
#la columna features: geometries dels paisos
paisos.features

#cada fila es objecte de tipo diccionari
print(type(paisos.features[1]))
paisos.features[1].keys()

print('type: '+ paisos.features[1]['type'])
print('Properties: ', paisos.features[1]['properties'])
print('Id: ' + paisos.features[1]['id'])
print('Geometry: ', paisos.features[1]['geometry'])


# el codi del pais està al camp id, per unir-lo al df data (ContryCode)
cod_paisos=list()
for dicc in paisos.features:
    cod_paisos.append(dicc["id"])    
print(cod_paisos[0:20])
len(cod_paisos)


# creamos mapa con folium
map = folium.Map(location=[-9.034818,41.880571], zoom_start=1.5)
map

#Parametres choropleth
#ubicación → Latitud y longitud del mapa.
#zoom_start → Nivel de zoom inicial para el mapa.
#mosaicos → mosaicos de mapa.
#geo_data → Nombre del archivo json. Este archivo debe estar ubicado en el directorio de trabajo.
#data → Nombre del marco de datos que contiene los datos.
#columnas → Columnas empleadas para generar el mapa de coropletas.
#key_on → Ingrese el archivo json que contiene el nombre del país.
#fill_color → Esquema de color utilizado en la visualización.
#fill_opacity → Opacidad de relleno del área, rango 0–1 (por defecto 0.6).
#line_opacity → Opacidad de la línea de geopath GeoJSON, rango 0–1 (predeterminado 1).
#legend_name → Título de la leyenda (cadena vacía predeterminada).
#smooth_factor → Cuánto simplificar la polilínea en cada nivel de zoom.


folium.Choropleth(geo_data=country_geo, data=plot_data,
             columns=['CountryCode', 'Value'],
             key_on='feature.id',
             fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
             legend_name=hist_indicator).add_to(map)
map

# Asociar los Datos en el DataFrame con la Geometría definida en el JSON
map.choropleth(geo_data=country_geo, data=plot_data,
             columns=['CountryCode', 'Value'],
             key_on='feature.id',
             fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
             legend_name=hist_indicator)


# Crear el Mapa HTML
map.save('plot_data2.html')

# Importar el Mapa HTMP Interactivo
from IPython.display import HTML
HTML('<iframe src=plot_data2.html width=700 height=450></iframe>')




regions_geo = 'C:/Users/MJ/documents/python/aprendiz-data-science-master/datasets/spain-communities.geojson'
regions=pd.read_json(regions_geo)
print(type(regions))
regions.head()

regions.features[1].keys()
regions.features[1]['properties']

regions_map = folium.Map(location=[40.2085 ,-3.713], zoom_start=5) 



