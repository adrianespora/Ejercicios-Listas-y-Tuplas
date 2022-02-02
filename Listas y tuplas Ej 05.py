#!/usr/bin/env python
# coding: utf-8

# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

# In[1]:


print("Ingrese 10 numeros: ")
n = ()
i=0
m = [] #lista donde se guardan los numeros
for i in range(10):
	n = int(input("Ingrese el numero : "))
	i = i+1
	m = m + [n] #agrega cada valor ingresado en la lista m
for j in reversed(m): #va leyendo valor por valor de atras a adelante
	print((j), end=",") #muestra los valores de la cadena separados por coma


# In[ ]:




