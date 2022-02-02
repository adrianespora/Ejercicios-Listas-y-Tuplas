#!/usr/bin/env python
# coding: utf-8

# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# In[1]:


print("Ingrese los 6 numeros ganadores de la loteria!")
n = ()
i=0
m = [] #lista donde se guardan los numeros
for i in range(6):
	n = int(input("Ingrese el numero : "))
	i = i+1
	m = m + [n] #agrega cada valor ingresado en la lista m
m.sort()
print(m)


# In[ ]:




