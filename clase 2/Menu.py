# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 08:53:10 2022

@author: HP
"""
"""
crear un programa que registe nuevos alumnos, liste los actuales alumno
borre un alumno, el alumno tiene nombre y apellido
"""
# crear una list
list = []
salir = False
while salir !=True:
  
    
  
    
   print("------------Menu----------------")
   print("1.- Listar alumnos")
   print("2.- Registrar alumno") 
   print("3.- Quitar alumno")
   print("4.- Salir")
   print("----------------------------")
    
   option = int(input("Seleccione una opcion [1-2-3-4]"))

option = int(input("selecione una opcion [1-2-3-4]:"))
#opcion 1 list alumno
if option == 1:
        print("La lista de alumnos es: ")
        for alumno in list:
         print(alumno)
            
#opcion 2 agrega alumno
elif option == 2:
    new_alumno = input("Ingrese Nombre Completo de Alumno:")
    list.append(new_alumno)

#opcion 3 quitar alumno

        
elif option == 3:
        alum_quitar = input("Ingrese nombre completo del alumno que se eliminara:")
        list.remove(alum_quitar)
        print("Se quitó de la lista a ", alum_quitar)
# opcion 4 salir        
elif option == 4: 
        print("bye")
        salir = True

else:
    print ("Porfavor ingrese una opcion valida [1, 2, 3, 4]")
    
    
print (f'La opcion selecciona es : {option}')
    
    