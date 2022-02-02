#!/usr/bin/env python
# coding: utf-8

# Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

# In[1]:


## Ejercicio 8
##Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Ingrese una palabra para saber si es un Palindromo: ")
revez  = ""
i=-1
for i in palabra:
	revez = letra
	
	
print(revez)


# In[2]:


word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")


# In[12]:


palabra = input("Introduce una palabra: ")
palabrainversa = palabra #almacena la palabra en otra variable
palabra = list(palabra) #crea una lista para la palabra ingresada
palabrainversa = list(palabrainversa) #crea una lista para la palabra guardada
palabrainversa.reverse() #Invierte el orden de las letras de la lista nombrada
if palabra == palabrainversa: # si la palabra ingresada es igual a la dada vuelta
    print("Es un palindromo") # imprime esto
else: # si no
    print("No es un palindromo")# imprime esto


# In[ ]:




