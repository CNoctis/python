import pyodbc
from tabulate import tabulate

#Clase articulo con la que se trabajará todos los objetos.
class articulo:

    def obtener(self):
        """Conecta con la base de datos para obtener la tabla en la que se esta trabajando de la Base de Datos

    :param objeto a trabajar

    :return: Tabla con los datos de la tabla
    """
        #Datos de la DB
        #Driver = driver según tu SQL.
        driver ='{ODBC Driver 17 for SQL Server}'
        
        #Server = (IP del servidor o alojamiento, Puerto de entrada del servidor o alojamiento) en caso de usar Servicio de alojamiento dedicado o Servidor privado)
        #Server = (Nombre de tu servidor SQL en otros casos)
        server = 'Host, Port'
        #Database = Nombre de la base de datos con la que se trabajará
        database = 'DB'
        #Usuario = Usuario creado del SQL
        username = 'Usuario'
        #Password = Contraseña de acceso de respetiva cuenta.
        password = 'Contraseña'

        #Crear una conexion
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        #Cursor/Fuente de acciones
        cursor = cnxn.cursor()

        #Do-while
        continuar = 1
        
        #Lista para el resultado de todos los articulos
        lista = list()
        
        #Lista para el resultado espesifico buscado.
        lista_busqueda = list()
        while continuar == 1:
            print ("-"*30 + 'Bienvenido al motor de busqueda' + "-"*30)
            print ('''
Opcion#1: Obtener todo los datos de los articulos existentes
Opción#2: Busqueda por Nombre
Opcion#3: Busqueda por Marca
Opción#4: Busqueda por Precio de Compra
Opcion#5: Busqueda por ID del Articulo
Opcion#6: Busqueda por cantidad de Articulos
Opción#7: Salir
''')
            print ("\n")
            
            op = int(input("Ingrese una opción de busqueda: "))

                
            if op == 1:
                #Cursor.exectue = Ejecuta una acción determinada mandando en forma de string la instrucción a ejecutar en el SQL
                cursor.execute('SELECT *  FROM DB.dbo.Tabla')
                for row in cursor:
                    lista.append(row)
                #Uso de tabulate por estetica y ordenamiento del resultado.)
                print(tabulate(lista, headers=["ID", "Nombre del Articulo", "Marca del Articulo","ID del Articulo","Precio de Compra", "Cantidad de Articulos"]))
                print ("\n")
                continuar = int(input("Precione 1 si desea realizar otra BUSQUEDA, de lo contrario precione otra tecla: "))
                print ("\n")

                    
            elif op == 2:
                busqueda = input ("Ingrese el NOMBRE del articulo a buscar: ")
                
                #Cargar = acción a realizar donde ""?"" son los valores que se cargaran para realizar la busqueda exitosa.
                cargar =('SELECT *  FROM DB.dbo.Tabla WHERE Nombre_Articulo =?')
                #Se llama a los valores de "cargar,busqueda" donde busqueda es el nombre que se buscará y reemplazará el "?" escrito en el string de cargar.
                cursor.execute(cargar, busqueda)
                for row in cursor:
                    lista_busqueda.append(row)
                print(tabulate(lista_busqueda, headers=["ID", "Nombre del Articulo", "Marca del Articulo","ID del Articulo","Precio de Compra", "Cantidad de Articulos"]))
                print ("\n")
                continuar = int(input("Precione 1 si desea realizar otra BUSQUEDA, de lo contrario precione otra tecla: "))
                print ("\n")

                    
                    
            elif op == 3:
                busqueda = input ("Ingrese la MARCA del articulo a buscar: ")
                cargar =('SELECT *  FROM DB.dbo.Tabla WHERE Nombre_Marca =?')
                cursor.execute(cargar, busqueda)
                for row in cursor:
                    lista_busqueda.append(row)
                print(tabulate(lista_busqueda, headers=["ID", "Nombre del Articulo", "Marca del Articulo","ID del Articulo","Precio de Compra", "Cantidad de Articulos"]))
                print ("\n")
                continuar = int(input("Precione 1 si desea realizar otra BUSQUEDA, de lo contrario precione otra tecla: "))
                print ("\n")


                    
            elif op == 4:
                busqueda = int (input ("Ingrese el PRECIO de compra: "))
                cargar =('SELECT *  FROM DB.dbo.Tabla WHERE Precio_Articulo_Compra =?')
                cursor.execute(cargar, busqueda)
                for row in cursor:
                    lista_busqueda.append(row)
                print(tabulate(lista_busqueda, headers=["ID", "Nombre del Articulo", "Marca del Articulo","ID del Articulo","Precio de Compra", "Cantidad de Articulos"]))
                print ("\n")
                continuar = int(input("Precione 1 si desea realizar otra BUSQUEDA, de lo contrario precione otra tecla: "))
                print ("\n")
                

                    
            elif op == 5:
                busqueda = int (input ("Ingrese el ID del articulo: "))
                cargar =('SELECT *  FROM DB.dbo.Tabla WHERE ID_Articulo =?')
                cursor.execute(cargar, busqueda)
                for row in cursor:
                    lista_busqueda.append(row)
                print(tabulate(lista_busqueda, headers=["ID", "Nombre del Articulo", "Marca del Articulo","ID del Articulo","Precio de Compra", "Cantidad de Articulos"]))
                print ("\n")
                continuar = int(input("Precione 1 si desea realizar otra BUSQUEDA, de lo contrario precione otra tecla: "))
                print ("\n")


                    
            elif op == 6:
                busqueda = input ("Ingrese la CANTIDAD de articulos que desea buscar: ")
                cargar =('SELECT *  FROM DB.dbo.Tabla WHERE Cantidad_Articulo =?')
                cursor.execute(cargar, busqueda)
                for row in cursor:
                    lista_busqueda.append(row)
                print(tabulate(lista_busqueda, headers=["ID", "Nombre del Articulo", "Marca del Articulo","ID del Articulo","Precio de Compra", "Cantidad de Articulos"]))
                print ("\n")
                continuar = int(input("Precione 1 si desea realizar otra BUSQUEDA, de lo contrario precione otra tecla: "))
                print ("\n")

                
            elif op == 7:
                print ("*"*30+"Programa finalizado" + "*"*30)
                print ("\n")
                continuar = 0

            else:
                print("Valor invalido! intente nuevamente")
                continuar = 1
                
                
        print ("\n")

        
                
    def cargar (self):
        """Conecta con la base de datos y carga los datos ingresados

    :param objeto a trabajar

    :return: Nada
    """
        driver ='{ODBC Driver 17 for SQL Server}'
        server = 'Host, Port' 
        database = 'DB' 
        username = 'Usuario' 
        password = 'Contraseña' 
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        
        #acción a realizar donde "?" es igual a cada valor a cargar en este caso son 5 valores a cargar por lo tanto son 5 "?"
        cargar=('INSERT INTO DB.dbo.Tabla (Nombre_Articulo,Marca_Articulo, ID_Articulo, Precio_Articulo_Compra, Cantidad_Articulo)'
                       'VALUES (?,?,?,?,?)')
        Nombre_Articulo= input ("Ingrese el nombre del articulo: ")
        Marca_Articulo= input ("Ingrese la marca del articulo: ")
        ID_Articulo= int (input ("Ingrese el ID del articulo: "))
        Precio_Articulo_Compra= int (input ("Ingrese el precio de compra del articulo: "))
        Cantidad_Articulo = int (input ("Ingrese la cantidad de articulos: "))

        
        cursor.execute(cargar,[Nombre_Articulo,Marca_Articulo, ID_Articulo, Precio_Articulo_Compra, Cantidad_Articulo])
        
        #confirma los cambios realizados en caso de no confirmar con .commit() ningún cambio será realizado.
        cursor.commit()

        
        print ("Los datos fueron cargados con éxito")
        print ("\n")

        

    def modificar (self):
        """Conecta con la base de datos realizar la busqueda y modificación de los datos a modificar.

    :param objeto a trabajar

    :return: Nada
    """
        driver ='{ODBC Driver 17 for SQL Server}'
        server = 'Host, Port' 
        database = 'DB' 
        username = 'Usuario' 
        password = 'Contraseña' 
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()

        continuar = 1

        while continuar == 1:
            print ('''
LOS CAMPOS DISPONIBLES DE BUSQUEDA PARA MODIFICAR SON:

Opción#1: Buscar por Nombre del Articulo
Opción#2: Buscar por Marca del Articulo
Opción#3: Buscar por ID del Articulo
Opción#4: Buscar por Precio de Compra del Articulo
Opción#5: Buscar por Cantidad de Articulos
Opción#6: Salir
''')
            print ("\n")

            
            op = int (input ("Ingrese la opción de busqueda: "))

            #Acciones de busqueda por NOMBRE
            if op == 1:
                nombre_articulo = input ("Ingrese el NOMBRE del articulo que desea modificar: ")
                print ("\n")
                print ('''
LOS CAMPOS DISPONIBLES A MODIFICAR SON:

Opción#1: Modificar Nombre del Articulo
Opción#2: Modificar Marca del Articulo
Opción#3: Modificar ID del Articulo
Opción#4: Modificar Precio de compra del Articulo
Opción#5: Modificar Cantidad de Articulos
Opción#6: Salir
''')
                print ("\n")
                
                continuar_modf =1
                while continuar_modf ==1:
                    modf = int(input("Ingrese cual campo desea modificar del producto: "))

                    #Modificacion del NOMBRE del producto
                    if modf == 1:
                        nombre_articulo_n = input ("Ingrese el nuevo NOMBRE del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Nombre_Articulo =? WHERE Nombre_Articulo =?')
                        cursor.execute(cargar, nombre_articulo_n, nombre_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Modificacion de la MARCA del producto  
                    elif modf == 2:
                        nombre_marca_n = input ("Ingrese la nueva MARCA del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Marca_Articulo =? WHERE Nombre_Articulo =?')
                        cursor.execute(cargar, nombre_marca_n, nombre_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Modificacion del ID del producto 
                    elif modf == 3:
                        id_articulo_n= input ("Ingrese el nuevo ID de compra del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET ID_Articulo =? WHERE Nombre_Articulo =?')
                        cursor.execute(cargar, id_articulo_n, nombre_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))
                        

                    #Modificacion del PRECIO del producto   
                    elif modf  == 4:
                        precio_articulo_compra_n = input ("Ingrese el nuevo PRECIO de compra del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Precio_Articulo_Compra =? WHERE Nombre_Articulo =?')
                        cursor.execute(cargar, precio_articulo_compra_n, nombre_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        

                    #Modificacion de la CANTIDAD del prodcuto    
                    elif modf == 5:
                        cantidad_articulo_n = input ("Ingrese la nueva CANTIDAD de articulos: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Cantidad_Articulo =? WHERE Nombre_Articulo =?')
                        cursor.execute(cargar, cantidad_articulo_n, nombre_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Finalizar programa    
                    elif modf == 6:
                        continuar_modf = 0
                        
                    #Solicitar datos correctos
                    else:
                        print ("Valor invalido ingrese alguno de los valores del menu de opciones")
                        print ("\n")

                        
                    print ("*"*30+"MENU DE MODIFICACIÓN DEL PRODUCTO FINALIZADO" + "*"*30)
                    print ("\n")





                        
            #Acciones de Busqueda por MARCA        
            elif op == 2:
                marca_articulo = input ("Ingrese la MARCA del articulo que desea modificar: ")
                print ("\n")
                print ('''
LOS CAMPOS DISPONIBLES A MODIFICAR SON:

Opción#1: Modificar Nombre del Articulo
Opción#2: Modificar Marca del Articulo
Opción#3: Modificar ID del Articulo
Opción#4: Modificar Precio de compra del Articulo
Opción#5: Modificar Cantidad de Articulos
Opción#6: Salir
''')
                print ("\n")
                
                continuar_modf =1
                while continuar_modf ==1:
                    modf = int(input("Ingrese cual campo desea modificar del producto: "))

                    #Modificacion del NOMBRE del producto
                    if modf == 1:
                        nombre_articulo_n = input ("Ingrese el nuevo NOMBRE del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Nombre_Articulo =? WHERE Marca_Articulo =?')
                        cursor.execute(cargar, nombre_articulo_n, marca_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Modificacion de la MARCA del producto  
                    elif modf == 2:
                        nombre_marca_n = input ("Ingrese la nueva MARCA del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Marca_Articulo =? WHERE Marca_Articulo =?')
                        cursor.execute(cargar, nombre_marca_n, marca_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Modificacion del ID del producto 
                    elif modf == 3:
                        id_articulo_n= input ("Ingrese el nuevo ID de compra del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET ID_Articulo =? WHERE Marca_Articulo =?')
                        cursor.execute(cargar, id_articulo_n, marca_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))
                        

                    #Modificacion del PRECIO del producto   
                    elif modf  == 4:
                        precio_articulo_compra_n = input ("Ingrese el nuevo PRECIO de compra del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Precio_Articulo_Compra =? WHERE Marca_Articulo =?')
                        cursor.execute(cargar, precio_articulo_compra_n, marca_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        

                    #Modificacion de la CANTIDAD del prodcuto    
                    elif modf == 5:
                        cantidad_articulo_n = input ("Ingrese la nueva CANTIDAD de articulos: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Cantidad_Articulo =? WHERE Marca_Articulo =?')
                        cursor.execute(cargar, cantidad_articulo_n, marca_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Finalizar programa    
                    elif modf == 6:
                        continuar_modf = 0
                        
                    #Solicitar datos correctos
                    else:
                        print ("Valor invalido ingrese alguno de los valores del menu de opciones")
                        print ("\n")

                        
                    print ("*"*30+"MENU DE MODIFICACIÓN DEL PRODUCTO FINALIZADO" + "*"*30)
                    print ("\n")
                    


            #Acciones de busqueda por ID
            elif op == 3:
                id_articulo = input ("Ingrese la ID del articulo que desea modificar: ")
                print ("\n")
                print ('''
LOS CAMPOS DISPONIBLES A MODIFICAR SON:

Opción#1: Modificar Nombre del Articulo
Opción#2: Modificar Marca del Articulo
Opción#3: Modificar ID del Articulo
Opción#4: Modificar Precio de compra del Articulo
Opción#5: Modificar Cantidad de Articulos
Opción#6: Salir
''')
                print ("\n")
                
                continuar_modf =1
                while continuar_modf ==1:
                    modf = int(input("Ingrese cual campo desea modificar del producto: "))

                    #Modificacion del NOMBRE del producto
                    if modf == 1:
                        nombre_articulo_n = input ("Ingrese el nuevo NOMBRE del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Nombre_Articulo =? WHERE ID_Articulo =?')
                        cursor.execute(cargar, nombre_articulo_n, id_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Modificacion de la MARCA del producto  
                    elif modf == 2:
                        nombre_marca_n = input ("Ingrese la nueva MARCA del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Marca_Articulo =? WHERE ID_Articulo =?')
                        cursor.execute(cargar, nombre_marca_n, id_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Modificacion del ID del producto 
                    elif modf == 3:
                        id_articulo_n= input ("Ingrese el nuevo ID de compra del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET ID_Articulo =? WHERE ID_Articulo =?')
                        cursor.execute(cargar, id_articulo_n, id_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))
                        

                    #Modificacion del PRECIO del producto   
                    elif modf  == 4:
                        precio_articulo_compra_n = input ("Ingrese el nuevo PRECIO de compra del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Precio_Articulo_Compra =? WHERE ID_Articulo =?')
                        cursor.execute(cargar, precio_articulo_compra_n, id_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        

                    #Modificacion de la CANTIDAD del prodcuto    
                    elif modf == 5:
                        cantidad_articulo_n = input ("Ingrese la nueva CANTIDAD de articulos: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Cantidad_Articulo =? WHERE Marca_Articulo =?')
                        cursor.execute(cargar, cantidad_articulo_n, id_articulo)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Finalizar programa    
                    elif modf == 6:
                        continuar_modf = 0
                        
                    #Solicitar datos correctos
                    else:
                        print ("Valor invalido ingrese alguno de los valores del menu de opciones")
                        print ("\n")

                        
                    print ("*"*30+"MENU DE MODIFICACIÓN DEL PRODUCTO FINALIZADO" + "*"*30)
                    print ("\n")



                    
            #Acciones de busqueda por PRECIO    
            elif op == 4:
                precio_articulo_compra = input ("Ingrese el PRECIO de compra del articulo que desea modificar: ")
                print ("\n")
                print ('''
LOS CAMPOS DISPONIBLES A MODIFICAR SON:

Opción#1: Modificar Nombre del Articulo
Opción#2: Modificar Marca del Articulo
Opción#3: Modificar ID del Articulo
Opción#4: Modificar Precio de compra del Articulo
Opción#5: Modificar Cantidad de Articulos
Opción#6: Salir
''')
                print ("\n")
                
                continuar_modf =1
                while continuar_modf ==1:
                    modf = int(input("Ingrese cual campo desea modificar del producto: "))

                    #Modificacion del NOMBRE del producto
                    if modf == 1:
                        nombre_articulo_n = input ("Ingrese el nuevo NOMBRE del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Nombre_Articulo =? WHERE Precio_Articulo_Compra =?')
                        cursor.execute(cargar, nombre_articulo_n, precio_articulo_compra)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Modificacion de la MARCA del producto  
                    elif modf == 2:
                        nombre_marca_n = input ("Ingrese la nueva MARCA del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Marca_Articulo =? WHERE Precio_Articulo_Compra =?')
                        cursor.execute(cargar, nombre_marca_n, precio_articulo_compra)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Modificacion del ID del producto 
                    elif modf == 3:
                        id_articulo_n= input ("Ingrese el nuevo ID de compra del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET ID_Articulo =? WHERE Precio_Articulo_Compra =?')
                        cursor.execute(cargar, id_articulo_n, precio_articulo_compra)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))
                        

                    #Modificacion del PRECIO del producto   
                    elif modf  == 4:
                        precio_articulo_compra_n = input ("Ingrese el nuevo PRECIO de compra del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Precio_Articulo_Compra =? WHERE Precio_Articulo_Compra =?')
                        cursor.execute(cargar, precio_articulo_compra_n, precio_articulo_compra)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        

                    #Modificacion de la CANTIDAD del prodcuto    
                    elif modf == 5:
                        cantidad_articulo_n = input ("Ingrese la nueva CANTIDAD de articulos: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Cantidad_Articulo =? WHERE Precio_Articulo_Compra =?')
                        cursor.execute(cargar, cantidad_articulo_n, precio_articulo_compra)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Finalizar programa    
                    elif modf == 6:
                        continuar_modf = 0
                        
                    #Solicitar datos correctos
                    else:
                        print ("Valor invalido ingrese alguno de los valores del menu de opciones")
                        print ("\n")

                        
                    print ("*"*30+"MENU DE MODIFICACIÓN DEL PRODUCTO FINALIZADO" + "*"*30)
                    print ("\n")



                    
            #Acciones de busqueda por CANTIDAD de articulos
            elif op == 5:
                cantidad_articulos = input ("Ingrese el PRECIO de compra del articulo que desea modificar: ")
                print ("\n")
                print ('''
LOS CAMPOS DISPONIBLES A MODIFICAR SON:

Opción#1: Modificar Nombre del Articulo
Opción#2: Modificar Marca del Articulo
Opción#3: Modificar ID del Articulo
Opción#4: Modificar Precio de compra del Articulo
Opción#5: Modificar Cantidad de Articulos
Opción#6: Salir
''')
                print ("\n")
                
                continuar_modf =1
                while continuar_modf ==1:
                    modf = int(input("Ingrese cual campo desea modificar del producto: "))

                    #Modificacion del NOMBRE del producto
                    if modf == 1:
                        nombre_articulo_n = input ("Ingrese el nuevo NOMBRE del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Nombre_Articulo =? WHERE Cantidad_Articulo =?')
                        cursor.execute(cargar, nombre_articulo_n, cantidad_articulos)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Modificacion de la MARCA del producto  
                    elif modf == 2:
                        nombre_marca_n = input ("Ingrese la nueva MARCA del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Marca_Articulo =? WHERE Cantidad_Articulo =?')
                        cursor.execute(cargar, nombre_marca_n, cantidad_articulos)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Modificacion del ID del producto 
                    elif modf == 3:
                        id_articulo_n= input ("Ingrese el nuevo ID de compra del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET ID_Articulo =? WHERE Cantidad_Articulo =?')
                        cursor.execute(cargar, id_articulo_n, cantidad_articulos)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))
                        

                    #Modificacion del PRECIO del producto   
                    elif modf  == 4:
                        precio_articulo_compra_n = input ("Ingrese el nuevo PRECIO de compra del producto: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Precio_Articulo_Compra =? WHERE Cantidad_Articulo =?')
                        cursor.execute(cargar, precio_articulo_compra_n, cantidad_articulos)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        

                    #Modificacion de la CANTIDAD del prodcuto    
                    elif modf == 5:
                        cantidad_articulo_n = input ("Ingrese la nueva CANTIDAD de articulos: ")
                        cargar = ('UPDATE DB.dbo.Tabla SET Cantidad_Articulo =? WHERE Cantidad_Articulo =?')
                        cursor.execute(cargar, cantidad_articulo_n, cantidad_articulos)
                        cursor.commit()
                        print ("Modificación realizada con exito")
                        print ("\n")
                        continuar_modf = int (input ("Ingrese 1 si desea continuar modificando este prodcuto o otro número para finalizar la modificación del producto: "))

                        
                    #Finalizar programa    
                    elif modf == 6:
                        continuar_modf = 0
                        
                    #Solicitar datos correctos
                    else:
                        print ("Valor invalido ingrese alguno de los valores del menu de opciones")
                        print ("\n")

                        
                    print ("*"*30+"MENU DE MODIFICACIÓN DEL PRODUCTO FINALIZADO" + "*"*30)
                    print ("\n")



                    
            elif op == 6:
                print ("*"*30+"Programa finalizado" + "*"*30)
                print ("\n")
                continuar = 0

            else:
                print ("Opción invalida invalida! intente nuevamente")
                
        print ("*"*30 + "Finalización de MODIFICACIÓN"+"*"*30)
        print ("\n")




        

    def eliminar(self):
        """Conecta con la base e elimina toda información en la tabla selecionada.

    :param objeto a trabajar

    :return: Nada
    """
        #Advertencia: al aplicar "DELETE" en SQL Sever se alteran los valores del INDEX por lo que debe tenerlo en cuenta.
        driver ='{ODBC Driver 17 for SQL Server}'
        server = 'Host, Port' 
        database = 'DB' 
        username = 'Usuario' 
        password = 'Contraseña' 
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        
        continuar = 1
        while continuar == 1:
            print ("¡"*10+"¡ADVERTENCIA!"+"!"*10 +" Los datos eliminados son inrecuperables.")
            print ('''


Las opciones para ELIMINAR son:

Opcion#1: Borrar TODOS LOS DATOS
Opción#2: Buscar por Nombre del Articulo para borrar TODOS LOS DATOS de ese articulo
Opción#3: Buscar por Marca del Articulo para borrar TODOS LOS DATOS de ese articulo
Opción#4: Buscar por ID del Articulo para borrar TODOS LOS DATOS de ese articulo
Opción#5: Buscar por Precio de Compra del Articulo para borrar TODOS LOS DATOS de ese articulo
Opción#6: Buscar por Cantidad de Articulos para borrar TODOS LOS DATOS de ese articulo
Opción#7: Salir
''')
            print ("\n")

            op = int (input ("Ingrese la opción de busqueda: "))

            #Borrar todos los DATOS
            if op == 1:
                cargar = ('DELETE FROM DB.dbo.Tabla')
                cursor.execute(cargar)
                cursor.commit()
                print ("TODOS LOS DATOS DE LA TABLA FUERON ELIMINADOS CON ÉXITO")
                print ("\n")

            #Borrar todos los DATOS que incluyan el NOMBRE DEL ARTICULO
            elif op == 2:
                nombre = input ("Ingrese el NOMBRE del articulo que desea eliminar de la tabla")
                cargar = ('DELETE FROM DB.dbo.Tabla WHERE Nombre_Articulo =?')
                cursor.execute(cargar, nombre)
                cursor.commit()
                print ("TODOS LOS ARCHIVOS CONCORDANTE CON LA BUSQUEDA FUERON ELIMINADOS")
                print ("\n")
                

            #Borrar todos los DATOS que incluyan la MARCA DEL ARTICULO
            elif op == 3:
                marca = input ("Ingrese la MARCA del articulo que desea eliminar de la tabla")
                cargar = ('DELETE FROM DB.dbo.Tabla WHERE Marca_Articulo =?')
                cursor.execute(cargar, marca)
                cursor.commit()
                print ("TODOS LOS ARCHIVOS CONCORDANTE CON LA BUSQUEDA FUERON ELIMINADOS")
                print ("\n")


            #Borrar todos los DATOS que incluyan la ID DEL ARTICULO
            elif op == 4:
                id_articulo = input ("Ingrese la ID del articulo que desea eliminar de la tabla")
                cargar = ('DELETE FROM DB.dbo.Tabla WHERE ID_Articulo =?')
                cursor.execute(cargar, id_articulo)
                print ("TODOS LOS ARCHIVOS CONCORDANTE CON LA BUSQUEDA FUERON ELIMINADOS")
                print ("\n")

            #Borra todos los DATOS que incluyan el PRECIO de compra del ARTICULO
            elif op == 5:
                compra = input ("Ingrese el PRECIO de compra del articulo que desea eliminar de la tabla")
                cargar = ('DELETE FROM DB.dbo.Tabla WHERE Precio_Articulo_Compra =?')
                cursor.execute(cargar, compra)
                cursor.commit()
                print ("TODOS LOS ARCHIVOS CONCORDANTE CON LA BUSQUEDA FUERON ELIMINADOS")
                print ("\n")


            #Borra todos los DATOS que incluyan la cantidad de articulos
            elif op == 6:
                compra = input ("Ingrese la cantidad de articulos del articulo que desea eliminar de la tabla")
                cargar = ('DELETE FROM DB.dbo.Tabla WHERE Precio_Articulo_Compra =?')
                cursor.execute(cargar, compra)
                cursor.commit()
                print ("TODOS LOS ARCHIVOS CONCORDANTE CON LA BUSQUEDA FUERON ELIMINADOS")
                print ("\n")

            elif op == 7:
                continuar = 0

            else:
                print ("Opción invalida intente nuevamente")
                print ("\n")

        print ("*"*30 +"Fin del menu de eliminar"+"*"*30)
        print ("\n")
                
