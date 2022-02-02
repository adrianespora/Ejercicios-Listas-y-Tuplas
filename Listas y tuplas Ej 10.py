#!/usr/bin/env python
# coding: utf-8

# Ejercicio 10
# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# In[4]:


lista = (50,75,46,22,80,65,8,60)
menor = 1000000
mayor = 0
for numero in lista:
    if menor > numero:
        menor = numero
    if mayor < numero:
        mayor = numero

print("El menor numero de la lista es" ,menor, "y el mayor es",mayor)


# In[ ]:




