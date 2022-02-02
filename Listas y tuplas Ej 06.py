#!/usr/bin/env python
# coding: utf-8

# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# In[1]:


i = 0
notas = [] #almacenara las notas
reprobado =[] #almacenara los reprobados
materias = ("matematicas", "lengua", "historia", "ingles")#lista de materias
for materia in materias: #recorre la lista de materias
	notas = int(input("Ingresa la nota de " + (materias[i] ) + ": "))#cargo los datos a notas, para que apar3zca el nombre de la materia agrego entre "+" la lista
	i = i+1
	if notas <=5: # Si el valor de Notas es menos onigual a 5
		reprobado.append(materia) # agrega a la lista el valor
print("Debes repetir : ", (reprobado), end=",")


# In[ ]:




