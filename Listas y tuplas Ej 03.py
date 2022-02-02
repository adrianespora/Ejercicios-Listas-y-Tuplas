#!/usr/bin/env python
# coding: utf-8

# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario

# In[1]:


lista = ["Matematicas","Historia","Lengua","Ingles"]
mate = int(input("Que nota sacaste en Matematicas? : "))
histo = int(input("Que nota sacaste en Historia? : "))
lengua = int(input("Que nota sacaste en Lengua? : "))
ingles = int(input("Que nota sacaste en Ingles? : "))
notas = [mate,histo,lengua,ingles]
i = 0
for mats in lista:
	print("En ", mats, "has sacado ", notas[i])
	i = i+1
	


# In[ ]:




