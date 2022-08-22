# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:41:25 2022

@author: HP EliteBook 2470p
"""
#import numpy as np
#import matplotlib
#import matplotlib.pyplot as plt
#import matplotlib.colors as colors
#import os
#import snappy
#from snappy import Product
#from snappy import ProductIO
#from snappy import ProductUtils
#from snappy import WKTReader
#from snappy import HashMap
#from snappy import GPF
# Para leer shapefiles
#import shapefile
#import pygeoif

import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
from tkinter.messagebox import showinfo

#Creacion del tamaño y tema de la ventana
#crecion de ventana o pantalla
vent = tk.Tk()
vent.geometry('1200x600')

#creacion etiqueta de titulo
vent.title('MAPEAR INUNDACIONES')   
vent.config(bg= 'turquoise')

# Widget 1 #

#etiqueta 1
etiqueta_1 = tk.Label(vent, text='1. Selecionar imagen a utilizar.', bg='Teal',  fg='white', font = 'Double 8')
etiqueta_1.grid(row = 0, column = 0, pady = (3))

# caja de texo 1
caja_1 = tk.Text(vent, height = 1, font = 'Double 8', bg = 'white', fg = 'black', highlightthickness = 3)                                
caja_1.grid(row = 2, column = 0, padx = (10,10))
#funcion para abrir imagen
def abrir_imagen():
    imagen_abierta=filedialog.askopenfilename(initialdir = "/", title = "Seleccione la imagen.",filetypes = (("zip files","*.zip"),("all files","*.*")))
    print (imagen_abierta)
    caja_1.insert(tk.END, imagen_abierta)
    
#Creacion boton 1
boton_1 = tk.Button(text="Seleccionar imagen", font = 'Double 8',  bg="white",command=abrir_imagen)
boton_1.grid(row = 1, column = 0, padx = (10,10))

# Widget 2 #

#etiqueta 2
etiqueta_2 = tk.Label(vent, text='2. Seleccionar un shapefile para analizar.', font = 'Double 8', bg='Teal', fg='White')
etiqueta_2.grid(row = 0, column = 1)

#caja de texo 2
caja_2 = tk.Text(vent, height = 1, font = 'Double 8', bg = 'white', fg = 'black', highlightthickness = 3)                                     
caja_2.grid(row = 2, column = 1, padx = (10,10))

#funcion para abrir imagen
def abrir_shape():
    shape_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione shapefile",filetypes = (("shapefile files","*.shp"),
                ("all files","*.*")))
    print (shape_abierto)
    caja_2.insert(tk.END, shape_abierto)
    
#creacion boton 2
boton_2 = tk.Button(text="Seleccione el shapefile ", font = 'Double 8', bg="white", command = abrir_shape)
boton_2.grid(row = 1, column = 1)
# Widget 3 #

#etiqueta 3
etiqueta_3 = tk.Label(vent, text='3. Proceda a pre-procesar la imagen.', font = 'Double 8', bg='Teal',  fg='White')
etiqueta_3.grid(row = 5, column = 0)


#creacion boton 3
boton_3 = tk.Button(text="Pre-procesar la imagen", font = 'Double 8', bg="white")
boton_3.grid(row = 6, column = 0)

# Widget 4 #

#etiqueta 4
etiqueta_4 = tk.Label(vent, text='4. Definir umbral para la máscara de agua.', font = 'Double 8', bg='Teal',  fg='White')
etiqueta_4.grid(row = 5, column = 1)

#Agregar caja de texto
caja_4 = tk.Entry(vent, font= 'Double 8', justify = 'center', highlightthickness = 3)
caja_4.grid(row = 6, column = 1, pady = (3))
#creacion boton 4
boton_4 = tk.Button(text="Aplicar la mascara", font = 'Double 8', bg="white")
boton_4.grid(row = 7, column = 1, pady =(3))

# Widget 5 #

#etiqueta 5
etiqueta_5 = tk.Label(vent, text='5. Crea la imagen GeoTIFF.', font = 'Double 8', bg='Teal', fg='White')
etiqueta_5.grid(row = 10, column = 0)

Resultado_mapa = tk.Canvas(vent, width = 600, height = 300, bg = 'white', highlightthickness = 10)
Resultado_mapa.grid(row = 12, column = 0, rowspan = 14, pady =(30))

#Creacion boton 5
boton_5 = tk.Button(text="Crear el archivo", font = 'Double 8', bg="white")
boton_5.grid(row = 11, column = 0)

vent.mainloop()