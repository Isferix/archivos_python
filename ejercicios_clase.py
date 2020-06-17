#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import re


def contar_lineas(archivo):
    '''Cuenta la cantidad de lineas de un archivo

    @archivo Archivo donde se contaran las lineas
    (puede que no funcione correctamente en archivos .csv)
    '''
    contador = 0
    with open(archivo, 'r') as fi:
        contador = len(fi.readlines())
    print("Hay", contador, "lineas en el texto")
    return contador


def generador_inventario(archivo, item):
    '''Generador de inventarios con formato:
    Elemento - Stock

    @param erchivo: Archivo idealmente .csv donde se guardara la informacion\n
    @param item: String y nombre del elemento que servira para armar el encabezado 
    '''
    csvfile = open(archivo, 'w', newline='')
    header = [item , 'stock']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    elementos_agregados = []
    while True:
        elemento = input('Introduzca el/la {}:\n'.format(item))
        if elemento == 'FIN':
            input("Cerrando programa")
            break
        if elemento in elementos_agregados:
            print('Este/a {} ya ha sido anadido/a al inventario'.format(item))
            continue
        else:
            elementos_agregados.append(elemento)

        stock = input('Introduzca el stock disponible:\n')
        
        writer.writerow({item: elemento, 'stock': stock})

    csvfile.close   


def buscador_inventario(archivo, item):
    '''Buscador de items dentro de un inventario con formato:
    Elemento - Stock

    @param archivo: Archivo idealmente .csv donde se buscara el elemento\n
    @param item: String y nombre del elemento que se buscara

    IMPORTANTE: Es necesario que el @param item sea obligatoriamente igual que 
    su correspondiente nombre en el encabezado para que no halla errores, en caso 
    de confusion, utilice esta funcion en conjunto con la correspondiente para generar
    inventarios proveida en este archivo
    '''
    csvfile = open(archivo, 'r', newline='')
    data = list(csv.DictReader(csvfile))

    while True:
        elemento = input('Introduzca el/la {} que busca:\n'.format(item))
        if elemento == 'FIN':
            break
        elemento_encontrado = [diccionario for diccionario in data if diccionario[item] == elemento]
        if len(elemento_encontrado) > 0:
            print('Se ha encontrado el/la {} que busca'.format(item))
            print('{}: {}'.format(elemento_encontrado[0][item], elemento_encontrado[0]['stock']))
        else:
            print('Elemento no encontrado')
            print('Por favor, intente nuevamente')
                
    csvfile.close     


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea alinea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''
    #cantidad_lineas = 
    contar_lineas('notas.txt')


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura.

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    # fi = open('nota.txt', 'r')
    # fo = open(.......)

    # Recuerde cerrar los archivos al final ;)
    fi = open('notas.txt', 'r')
    fo = open('escritura.txt', 'w')

    Lineas = fi.readlines()
    for linea in Lineas:
        fo.write(linea)


    fi.close()
    fo.close()


def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrer dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
    with open('propiedades.csv') as csvfile:
        ambientes_2 = 0
        ambientes_3 = 0
        data = list(csv.DictReader(csvfile)) 
        for i in data:
            if i.get('ambientes') == '2':
                ambientes_2 += 1
            if i.get('ambientes') == '3':
                ambientes_3 += 1
        print("Hay {} departamentos de 2 ambientes".format(ambientes_2))
        print("Hay {} departamentos de 3 ambientes".format(ambientes_3))    


def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario el par:
    <fruta>:<cantidad>
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    Al finalizar el bucle anterior, debe generar otro bucle
    en donde se pida ingresar la fruta o verdura que desea
    conocer su estado de stock.
    Deberá imprimir en pantalla la cantidad de esa fruta en
    inventario, y en caso de no exista ese elemento en nuestro
    inventario se debe imprimir en pantalla "Elemento no encuentrado"
    NOTA: Proponemos utilizarel método "get" que devuelve "None" si el
    elemeto no existe en el diccionario.

    Se debe terminar ese segundo bucle cuando se ingrese la palabra FIN
    '''
    # 1) Bucle 1
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"
    generador_inventario('inventario.csv', 'fruta')
    # 2) Bucle 2
    # Ingresar por consola la fruta que desea conocer en stock
    # Finalizar cuando la fruta ingresada sea igual a "FIN"
    buscador_inventario('inventario.csv', 'fruta')

    
def ej5():
    # Ejercicios con archivos CSV
    inventario = {}

    '''
    Basado en el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario que utilizaremos para escribir en el archivo CSV

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})
    generador_inventario('inventarioFoV.csv', 'fruta/verdura')



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
