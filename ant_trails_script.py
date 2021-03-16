# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 18:47:55 2021

@author: Santiago Santoandre https://twitter.com/santisantoandre
"""

import pandas
import numpy as np
import cv2



def cutimage(img, xmin, xmax, ymin, ymax):
    imgCropped = img[ymin:ymax, xmin:xmax]
    mask = cv2.inRange(imgCropped, gris, blanco)
    cont= cv2.countNonZero(mask) #calcula el numero de pixeles blancos
    height = mask.shape[0] #medidas del cuadrante
    width = mask.shape[1] #medidas del cuadrante
    dimensiones = height*width #calcula el numero de pixeles de la imagen
    proptracks = 1-(cont/dimensiones) #calcula la proporcion de pixeles oscuros
    return proptracks

def recorrermapa(img, df, actividad):
    for i in range(len(df["xmin"])):
        xmin = df["xmin"][i]
        xmax = df["xmax"][i]
        ymin = df["ymin"][i]
        ymax = df["ymax"][i]
        ptracks = cutimage(img, xmin, xmax, ymin, ymax)
        actividad.append(ptracks)
    return actividad
        
def paratodoslosarchivos(fn):        
    for i in range (len(fn["filename"])):
        filename = fn["filename"][i]
        ubicacion = "./images/" + str(filename)
        img = cv2.imread(ubicacion)
        actividad=[]
        recorrermapa(img, df, actividad)
        tabla_act = np.array(actividad).reshape(mapa_columnas, mapa_filas) #aqui va el numero de filas y columnas del mapa
        np.savetxt("./results/" + str(filename) + ".csv", tabla_act, delimiter=",")
        

# datos: archivos a analizar y grilla
fn = pandas.read_csv('filename.csv')
df = pandas.read_csv('grilla_automatica.csv')

######### Datos a definir ##########
# Tamano de la grilla del mapa, datos ver la consola cuando se ejecuta grilla.py
mapa_filas = 49
mapa_columnas = 28

#Aca va el umbral de deteccion de las zonas sin tracks valor max y min
blanco = np.array([255,255,255])
gris = np.array([125, 125, 125])
#####################################

#ejecutar script
ejecutar= paratodoslosarchivos(fn)
