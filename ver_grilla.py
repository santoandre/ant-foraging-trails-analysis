# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:35:46 2021

@author: Santiago Santoandre https://twitter.com/santisantoandre
"""
import pandas
import cv2

def pinta_cuadrantes(img, xmin, xmax, ymin, ymax, z):
    cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,255,0),1)
    cv2.putText(img, str(z), (xmin, ymin+10), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 0, 0), 1)

def recorrermapa(img, df):
    z=1
    for i in range(len(df["xmin"])):
        xmin = df["xmin"][i]
        xmax = df["xmax"][i]
        ymin = df["ymin"][i]
        ymax = df["ymax"][i]
        pinta_cuadrantes(img, xmin, xmax, ymin, ymax, z)
        z=z+1

# datos: archivos armar la grilla usa la primera imagen listada en filename.csv
fn = pandas.read_csv('filename.csv')
filename = fn["filename"][0] #primera imagen listada en filename.csv
ubicacion = "./images/" + str(filename)
img = cv2.imread(ubicacion)

# datos: archivos a analizar y grilla
df = pandas.read_csv('grilla_automatica.csv')

ejecutar= recorrermapa(img, df) 

cv2.imshow("My first OpenCV window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
