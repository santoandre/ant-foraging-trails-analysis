Author: Santiago Santoandre - https://twitter.com/santisantoandre
#################################################################
Ants Track
#################################################################

A partir de tracks de hormigas sobre una imagen (mapa de bits)
y usando una grilla permite estimar el uso de cada celda de la
grilla.

El resultado es la una tabla por cada imagen en la cual se
observa el porcentaje de cobertura de camino (track)
en cada celda de la grilla.

Se genera un archivo csv por archivo de imagen.
---------------------------
generar_grilla.py : Crea la grilla. 

Se deben definir los siguientes parametros:
#Tamano : Numero de pixeles de lado (largo) de la celda de la grilla
x = 60 (por ejemplo)
#Coordenadas de la Xmin e Ymin de la primer celda de la grilla (arriba a la izquierda)
x0 = 10 (por ejemplo)
y0 = 5 (por ejemplo) 

Este Script usa la primer imagen listada en filename.csv y busca la imagen dentro la carpeta image
---------------------------
ver_grilla.py: Muestra una imagen con la grilla superpuesta.

Este Script usa la grilla (grilla_automatica.csv) y la primer imagen listada en filename.csv 
y busca la imagen dentro la carpeta image
---------------------------
ants_track_script.py: A partir de tracks de hormigas sobre una imagen (mapa de bits)
y usando una grilla permite estimar el uso de cada celda de la
grilla. El resultado es la una tabla por cada imagen en la cual se
observa el porcentaje de cobertura del camino
en cada celda de la grilla. Se genera un archivo csv por imagen, en la carpeta results.

Se deben definir los siguientes parametros, estos valores figuran en la consola cuando se ejecuta grilla.py:
# Tamano de la grilla del mapa
mapa_filas = 7  (por ejemplo)
mapa_columnas = 7  (por ejemplo)
#EN CASO NECESARIO: Cambiar el umbral de deteccion de las zonas sin tracks valor max y min
blanco = np.array([255,255,255])
gris = np.array([125, 125, 125])

Este Script usa la grilla (grilla_automatica.csv) y el listado de imagenes filename.csv y busca las imagenes dentro la carpeta image
---------------------------

Supuestos:
La grilla es fija, cada celda refiere a un area fisica real 
en el campo.
El ancho de la linea de tracks debe ser fijo para todas
las imagenes.
Las imagenes tienen que ser con fondo blanco y tracks en negro (preferentemente)

filename.csv: lista de archivos de imagenes a evaluar

grilla.csv: mapa global, coordenadas de cada celda de la grilla.   

