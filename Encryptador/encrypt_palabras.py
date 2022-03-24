import os

''' El presente programa tiene como objetivo encryptar es decir ocultar los 
    mensajes enviados atraves del documento texto.txt
'''

path_folder_file = r"C:\Users\Cristian\Documents\Python"
os.chdir(path_folder_file)


def convertir_texto_ascii(texto):
    """Devuelve texto en una lista de caracteres ascii

    :param texto: Texto a convertir

    :return: Lista con los caracteres en codificación ascii
    """
    return [ord(caracter) for caracter in texto]  # usamos list comprehension


def convertir_ascii_a_texto(lista_texto_ascii: list, encriptar: True) -> str:
    """Codifica/Decodifica una lista de texto ascii y devuelve con texto

    :param lista_texto_ascii: Texto a convertir
    :param encriptar: Boolean para codificar o decodificar

    :return: Texto de una lista ascii
    """
    cadena_texto = ""
    i = 1
    for caracter_ascii in lista_texto_ascii:
        if encriptar:
            cadena_texto += chr(caracter_ascii + i)
        else:
            cadena_texto += chr(caracter_ascii - i)
        i += 1
    return cadena_texto

def abrir():
    with open('texto.txt', 'r',encoding="utf8") as archivo:
        file = archivo.read()
        
                                            
        return file

def guardar_encrypt(texto_encryptado):
        """Crea un documento texto_encryptado.txt

    :param lista_texto_encryptado: Texto encryptado
    :return: archivo (.txt)
        """
        with open ('texto_encryptado.txt', 'w', encoding="utf8") as encrypt:
            archivo_encrypt = texto_encryptado
            encrypt.write(archivo_encrypt)


def guardar_desencrypt(texto_desencryptado):
            """Crea un documento texto_desencryptado.txt

    :param lista_texto_encryptado: Texto desencryptado
    :return: archivo (.txt)
        """
            with open ('texto_desencryptado.txt', 'w', encoding = "utf8") as desencryptado:
                archivo_desencryptado = texto_desencryptado
                desencryptado.write(archivo_desencryptado)
    
    


def main():
    texto_ingresado = abrir()

    """Acciones para encryptar"""
    lista_ascii = convertir_texto_ascii(texto_ingresado)
    texto_encryptado = convertir_ascii_a_texto(lista_ascii, True)
    guardar_archivo_encryptado = guardar_encrypt(texto_encryptado)
    
    """ Accciones para desencryptar"""
    lista_ascii_encryptado = convertir_texto_ascii(texto_encryptado)
    texto_desencryptado = convertir_ascii_a_texto(lista_ascii_encryptado, False)
    guardar_archivo_desencryptado = guardar_desencrypt(texto_desencryptado)




if __name__ == "__main__":
    main()
