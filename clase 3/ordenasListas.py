# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 07:54:50 2022

@author: HP
"""

A = [85, 86 ,32 ,12 ,82 ,43]
# i, j
# [12,32,43,55,82,86]
# obtener el tamaño de la lista
num = len (A)
i=0
while i < num :
    j=i
    while j < num :
        if (A[i]> A[j]):
           aux= A[i]
           A[i]=A[j]
           A[i]=aux
        j=j+1
    i=i+1
print ("lista ordenada")
print (A)
listDeNumeros = [34, 12, 4, 10]
print ("lista original")
print (listDeNumeros)
listDeNumeros.sort()
print ("lista ordenada")
print (listDeNumeros)





           
         
