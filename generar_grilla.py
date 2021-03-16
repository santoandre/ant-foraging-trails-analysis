# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:48:14 2021

@author: Santiago Santoandre https://twitter.com/santisantoandre
"""
### solucionar problema con la grilla tiene orden vertical y requiere que sea horizontal
import pandas
import numpy as np
import cv2

def make_grilla(x, x0, y0, xtotal, ytotal):
    grilla = []
    w = (xtotal - x0)/x
    j = (ytotal - y0)/x
    i=1
    while i<w:
        v=1
        while v<j:
          grilla.append(y0 + (x *(v-1)))
          grilla.append(y0 + (x * v))
          grilla.append(x0 + (x *(i-1)))
          grilla.append(x0 + (x * i))
          
          v = v+1
        i= i+1
    celdas = ((i-1)*(v-1)) # numero de celdas de la grilla
    tabla_grilla = np.array(grilla).reshape(celdas,4)
    dataframe_grilla = pandas.DataFrame(tabla_grilla, columns=["xmin", "xmax", "ymin", "ymax"])
    dataframe_grilla.to_csv("grilla_automatica.csv")
    print("Poner estos datos en ant_track_script.py")
    print("Numero de filas: " + str(v-1))
    print("Numero de columnas: " + str(i-1))
    return tabla_grilla    
    
# datos: archivos armar la grilla usa la primera imagen listada en filename.csv
fn = pandas.read_csv('filename.csv')
filename = fn["filename"][0] #primera imagen listada en filename.csv
ubicacion = "./images/" + str(filename)
img = cv2.imread(ubicacion)
xtotal = img.shape[0] #medidas de la imagen
ytotal = img.shape[1] #medidas de la imagen

#### Datos a definir manualmente ################
#Numero de pixeles de lado (largo) de la celda de la grilla
x = 20 
#Coordenadas de la Xmin e Ymin de la primer celda de la grilla
x0 = 10
y0 = 5
#################################################

#ejecuta el Script
tabla_grilla = make_grilla(x, x0, y0, xtotal, ytotal)