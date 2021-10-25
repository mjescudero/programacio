# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import matplotlib.pyplot as plt

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

image_file = "C:/Users/MJ/Documents/python/aprendiz-data-science-master/images/california.jpg"
#leer foto como array
photo_data=mpimg.imread(image_file)
# esta función carga la imagen en modo lectura 
#si es vol modificar s'ha de fer una copy del array

print( type(photo_data) ) 
plt.imshow(photo_data)
print(photo_data.shape)
n=photo_data.size
n

#######################################
image_file = "C:/Users/MJ/Documents/python/aprendiz-data-science-master/images/california.jpg"
import imageio
img=imageio.imread(image_file)
#permet modificar la imatge
type(img)
plt.figure(figsize=(10,10))
plt.imshow(img)
##############################################


#filtrar valores de la imagen que tengan colores menores del 125, en cualquiera de su array de colores
low_value_filter = photo_data < 125
print("Shape of low_value_filter:", low_value_filter.shape)
low_value_filter[1,1]

###################

total_rows, total_cols, total_layers = photo_data.shape
#total_rows, total_cols, total_layers = (12, 12, 3)
print("photo_data = ", photo_data.shape)

#arrays d'indexos:  files i columnes X, Y

X, Y = np.ogrid[:total_rows, :total_cols]
print("X = ", X.shape, " and Y = ", Y.shape)


# calculem el centre dels indexos: punts mitjos dels eixos
center_row, center_col = total_rows / 2, total_cols / 2
print("center_row = ", center_row, "AND center_col = ", center_col)
print(X - center_row)
print(Y - center_col)

# calculem el quadrat de la distància al centre de la imatge
dist_from_center = (X - center_row)**2 + (Y - center_col)**2
print(dist_from_center)

#tenim una array de distàncies al quadrat, eleven el radi al quadrat
radius = (total_rows / 2)**2
print("Radius = ", radius)

circular_mask = (dist_from_center > radius)
print(circular_mask)

photo_data[circular_mask] = 125
plt.figure(figsize=(15,15))
plt.imshow(photo_data)


# asignar 0 a los valores de colores que cumplen mi filto True, False, False
# se modifica la intensidad del pixel, assignant el color negre a tots 
# aquells que el color es menor que 125
photo_data[low_value_filter] = 0
plt.figure(figsize=(5,5))
plt.imshow(photo_data)



#exemple  subplot3D ##########################################################

from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt


# imports specific to the plots in this example
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data

# Twice as wide as it is tall.
fig = plt.figure(figsize=plt.figaspect(0.5))

#---- First subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
ax.set_zlim3d(-1.01, 1.01)

fig.colorbar(surf, shrink=0.5, aspect=10)

#---- Second subplot
ax = fig.add_subplot(1, 2, 2, projection='3d')
X, Y, Z = get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()


#############mostra la imatge##########################################################

from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cbook import get_sample_data
from matplotlib._png import read_png
fn = get_sample_data("lena.png", asfileobj=False)
#img = read_png(fn)
x, y = ogrid[0:img.shape[0], 0:img.shape[1]]
R = np.sqrt(x**2 + y**2)
z = np.sin(R)
ax = gca(projection='3d')
ax.plot_surface(x, y, z, rstride=5, cstride=5, facecolors=img/255.0)
show()


################funciona#################################################
image= "C:/Users/MJ/Pictures/bigdata2.png"
img2=imageio.imread(image)

x, y = ogrid[0:img2.shape[0], 0:img2.shape[1]]
R = np.sqrt(x**2 + y**2)
z = np.sin(R)
ax = gca(projection='3d')
ax.plot_surface(x, y, z, rstride=5, cstride=5, facecolors=img2)
show()
































print(scipy.__version__)
pip install -U scipy
# actualitzar totes les llibreries mab pip
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U