#!/usr/bin/env python
# coding: utf-8

# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

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




