#!/usr/bin/env python
# coding: utf-8

# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

# In[1]:


abc = ['a','b','c','d','e','f','g','h','i','h','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']
for letra in range(len(abc), 1, -1): #recorre valor por valor de principio a fin)
	if letra %3==0 :#si el numero de la posicion del valor dividido por 3 tiene resto 0
		abc.pop(letra-1) #borra el valor de la posicion
print(abc) #muestra la lista sin los elementos borrados por pop


# In[ ]:




