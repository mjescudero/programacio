#!/usr/bin/env python
# coding: utf-8

# # Folium: librería para la visualización de datos en mapas
#  instalar la libreia con: pip install folium

# # Visualización de las Emisiones de CO2 en Mapas

# In[1]:


#pip install folium


# In[2]:


import pandas as pd


# In[3]:


import folium


# ### Mapas de los Países del Mundo
# 
# https://github.com/phermar/aprendiz-data-science/blob/master/datasets/world-countries.json

# In[4]:


country_geo = '../datasets/world-countries.json'
print(country_geo)


# In[5]:


paisos=pd.read_json(country_geo)
print(type(paisos))
paisos.head()


# In[6]:


type(paisos.features)


# In[7]:


print(type(paisos.features[1]))
paisos.features[1].keys()


# In[8]:


print('type: '+ paisos.features[1]['type'])
print('Properties: ', paisos.features[1]['properties'])
print('Id: ' + paisos.features[1]['id'])
print('Geometry: ', paisos.features[1]['geometry'])


# In[9]:


#for clau, valor in paisos.features[1].items(): print('clave: ',clau, ' valor: ',valor)


# In[10]:


cod_paisos=list()
for dicc in paisos.features:
    cod_paisos.append(dicc["id"])    
print(cod_paisos[0:20])
len(cod_paisos)


# In[11]:


paisos.features[0].get('id')


# In[12]:


data = pd.read_csv('../datasets/world-development-indicators/Indicators.csv')
data.shape


# In[13]:


data.head()


# ## Consultamos las Emisiones de CO2 para todos los Países en 2011

# In[14]:


# Seleccionamos los Datos
hist_indicator = 'CO2 emissions \(metric'
hist_year = 2011

# Creamos los Filtros
mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['Year'].isin([hist_year])

# Aplicamos los Filtros
stage = data[mask1 & mask2]
stage.head()


# In[15]:


#paisos.features[1]['ValorCO2']
cod_pais=paisos.features[1]['id']
p=stage[stage['CountryCode']==cod_pais]
p.iloc[0]['Value']


# In[16]:


paisos.features[1]


# In[17]:




# recorrer fitxer de paisos i agefir la clau IndicadorCO2, amb el valor del CO2 de data frame i despre mostrsr-ho al tooltip
for dicc in paisos.features :
    cod_pais=dicc['id']
    if (stage['CountryCode']==cod_pais).any():
        dicc['properties']['EmisionesCO2']= stage[stage['CountryCode']==cod_pais].iloc[0]['Value']
 


# In[18]:


paisos.features[1]['properties'].keys()


# ## Seleccionamos los datos para el diagrama

# In[19]:


plot_data = stage[['CountryCode','Value']]
#filter_a = stage['CountryCode'] == 'CHN'
#filter_b = stage['CountryCode'] == 'IND'
#plot_data = stage[(stage['CountryCode'] == 'CHN') | (stage['CountryCode'] == 'IND')] 
plot_data.head(10)


# In[20]:


# Seleccionamos la Etiqueta para el Diagrama
hist_indicator = stage.iloc[0]['IndicatorName']
print(hist_indicator)


# # Visualize CO2 emissions per capita using Folium
# 
# Folium provides interactive maps with the ability to create sophisticated overlays for data visualization

# In[21]:


# Visualizamos las Emisiones de CO2


# In[22]:


# Crear un Mapa, ponemos una de las coordenadas del json para españa
map = folium.Map(location=[-9.034818,41.880571], zoom_start=1.5)


# In[23]:


map


# In[24]:


cp=folium.Choropleth(geo_data=country_geo, data=plot_data,
             columns=['CountryCode', 'Value'],
             key_on='feature.id',
             fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
             legend_name=hist_indicator)


# In[25]:


cp.geojson.add_child(folium.features.GeoJsonTooltip(fields=['name'],aliases=['País']))


# In[26]:


cp.add_to(map)
map


# In[27]:



map.save("mymap.html")


# In[28]:


# Importar el Mapa HTMP Interactivo
from IPython.display import HTML
HTML('<iframe src=mymap.html width=700 height=450></iframe>')


# In[29]:


# Crear un Mapa, ponemos una de las coordenadas del json para españa
map = folium.Map(location=[-9.034818,41.880571], zoom_start=1.5)

# utilizamos la funcion choropelts del mapa, en lugar de la classe foluim.choropleth anterior
map.choropleth(geo_data=country_geo, data=plot_data,
             columns=['CountryCode', 'Value'],
             key_on='feature.id',
             fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
             legend_name=hist_indicator)
map


# In[30]:


# Crear el Mapa HTML
map.save('plot_data.html')


# In[31]:


# Importar el Mapa HTMP Interactivo
from IPython.display import HTML
HTML('<iframe src=plot_data.html width=700 height=450></iframe>')


# In[32]:


## Visualizamos las Emisiones de CO2 en el tooltip del mapa temático


# In[33]:


#el json lo leemos de otra forma será un diccionario no un dataframe
import json
nou_json= json.load(open(country_geo))
print(type(nou_json))
type(nou_json['features'])


# In[34]:



for dicc in nou_json['features']:
    cod_pais=dicc['id']
    if (stage['CountryCode']==cod_pais).any():
        dicc['properties']['EmisionesCO2']= stage[stage['CountryCode']==cod_pais].iloc[0]['Value'].round(3)
    
nou_json['features'][0]['properties']
  


# In[ ]:



  


# In[35]:


# Crear un Mapa, ponemos una de las coordenadas del json para españa
map = folium.Map(location=[-9.034818,41.880571], zoom_start=1.5)
cp=folium.Choropleth(geo_data=nou_json, data=plot_data,
             columns=['CountryCode', 'Value'],
             key_on='feature.id',
             fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2,
             legend_name=hist_indicator)

cp.geojson.add_child(folium.features.GeoJsonTooltip(fields=['name','EmisionesCO2'],aliases=['País','Emisiones CO2']))

cp.add_to(map)
map


# In[36]:


#mapa comunidades de españa
regions_geo = '../datasets/spain-communities.geojson'
print(regions_geo)


# In[37]:


regions=pd.read_json(regions_geo)
print(type(regions))
regions.head()


# In[38]:


regions.features[1].keys()


# In[39]:


regions.features[1]['properties']


# In[ ]:





# In[40]:


regions.features[1]['geometry']['coordinates'][1:4]


# In[41]:


# Crear un Mapa, ponemos una de las coordenadas del json para españa
map = folium.Map(location=[40.2085 ,-3.713], zoom_start=5) 

#‘YlOrRd,
#{"weight":2, 'color':'black','fillColor': 'lightblue',}
#
style ={'fillColor': 'green'}
geo=folium.GeoJson(
    regions_geo,
    name='geojson',
    style_function= lambda x:{"weight":1, 'color':'green','fillColor': 'lightgreen',}, 
    highlight_function= lambda x:{"weight":4,'fillColor': 'red','color':'darkblue'},
).add_to(map)
map


# In[42]:


geo.add_child(folium.features.GeoJsonTooltip(fields=['name'],aliases=['CA: '],style=('background-color: grey; color: white; font_weight: bold;')))


# In[43]:


map


# In[44]:


print(geo)


# In[45]:


## Otros ejemplos de Folium
https://nbviewer.jupyter.org/github/python-visualization/folium/tree/master/examples/


# ## Manual de Folium
# https://python-visualization.github.io/folium/docs-v0.6.0/
