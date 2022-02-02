#!/usr/bin/env python
# coding: utf-8

# Ejercicio 9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

# In[19]:


palabra = input("Ingrese una palabra para contar sus vocales: ")
vocales = ['a','e','i','o','u']
cuentaA = 0
cuentaE = 0
cuentaI = 0
cuentaO = 0
cuentaU = 0
for letra in palabra:
    if letra == "a":
        cuentaA = cuentaA +1
    if letra == "e":
        cuentaE = cuentaE +1
    if letra == "i":
        cuentaI = cuentaI +1
    if letra == "o":
        cuentaO = cuentaO +1
    if letra == "u":
        cuentaU = cuentaU +1
if cuentaA > 0:
    print("La palabra tiene",cuentaA, "a")
if cuentaE > 0:
    print("La palabra tiene",cuentaE, "e")
if cuentaI > 0:
    print("La palabra tiene",cuentaI, "i")
if cuentaO > 0:
    print("La palabra tiene",cuentaO, "o")
if cuentaU > 0:
    print("La palabra tiene",cuentaU, "u")


# In[ ]:




