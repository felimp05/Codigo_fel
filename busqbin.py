# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:51:41 2022

@author: user
"""

listanum=[1,2,3,4,5,6,7,8,10,11]

def busqueda_bin(listado, buscado):
    inicio=0
    final=len(listado)-1
    contador=0
    while inicio<=final:
        medio=(inicio+final)//2
        if (listado[medio] == buscado):
            return contador
        elif listado[medio]<buscado:
            inicio=medio+1
            contador+=1
        elif listado[medio]>buscado:
            final=medio-1
            contador+=1
    return contador

print(busqueda_bin(listanum,9))

