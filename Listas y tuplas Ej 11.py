#!/usr/bin/env python
# coding: utf-8

# Ejercicio 11
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

# In[13]:


vector1 = (1,2,3)
vector2 = (-1,0,2)
vectorx = ""
vectorY = ""
vectorZ = ""
vectorx = vector1[0]*vector2[0]
vectory = vector1[1]*vector2[1]
vectorz = vector1[2]*vector2[2]
productoescalar = vectorx+vectory+vectorz
print("Lista de vectores1 :", vector1)
print("Lista de vectores2 :", vector2)
print("El producto escalar de los vectores es: ",productoescalar)


# In[ ]:




