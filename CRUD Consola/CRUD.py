import pyodbc
import CRUDbackend

''' El presente programa tiene como objetivo realizar acciones basicas de SQL
(Agregar, obtener, modificar y eliminar datos) desde un programa de consola de Python
Para que el presente programa funcione correctamente debe estar junto a CRUDbacken.py en la misma carpeta.
'''


#Inicio de Do-While
continuar = 1

while continuar == 1:
    
    #Creación del menú de opciones.
    print ("="*10 + " Bienvenido al CRUD " +"="*10)
    print ('''
Opción #1: Cargar Datos
Opción #2: Obtener datos
Opción #3: Modificar Datos
Opcion #4: Eliminar Datos
Opcion #5: Salir
            ''')
    try:
        op = int(input("Selecione una opción: "))
        print ("\n")
    except ValueError:
        op = 6
        print ("Ingrese una opción valida")
        print ("\n")
        
    if op == 1:
        print ("Ha ingresado a la opción de cargar")
        print ("Esto puede tardar uno segundos")
        print ("\n")
        #Agrega al articulo la clase "articulo"
        articulo = CRUDbackend.articulo()
        #Articulo ahora llama a la función "cargar" que se encuentra en la clase articulo y así con cada opción.
        articulo.cargar()

    elif op == 2:
        print ("Has ingresado a la opción de obtener datos")
        print ("Esto puede tardar uno segundos")
        print ("\n")
        articulo = CRUDbackend.articulo()
        articulo.obtener()

    elif op == 3:
        print ("Has ingresado a la opción de modificar datos")
        print ("Esto puede tardar uno segundos")
        print ("\n")
        articulo = CRUDbackend.articulo()
        articulo.modificar()
        
    elif op == 4:
        print ("Ha ingresado a eliminar datos")
        print ("Esto puede tardar uno segundos")
        print ("\n")
        articulo = CRUDbackend.articulo()
        articulo.eliminar()

    elif op == 5:
        continuar = 0

    else:
        print ("Opción invalida intente nuevamente")
        print ("\n")

        
print ("*"*30+"Programa finalizado" + "*"*30)
    
