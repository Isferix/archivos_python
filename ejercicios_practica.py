#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import re


def decordador_Ironman(funcion):
    def decorar(*args, **kwargs):
        retorno = funcion(*args, **kwargs)

        print('''

************************
Analisis Categoria {}
************************
'''.format(retorno[0]))
        print('''
******
*Swim*
******

#Tiempo Promedio:   {}
#Mejor tiempo:      {} por {}
#Peor Tiempo:       {} por {}
'''.format(retorno[1][0], retorno[1][1], retorno[1][2], retorno[1][3], retorno [1][4]), end='')

        print('''
******
*Bike*
******

#Tiempo Promedio:   {}
#Mejor tiempo:      {} por {}
#Peor Tiempo:       {} por {}     

 '''.format(retorno[2][0], retorno[2][1], retorno[2][2], retorno[2][3], retorno [2][4]), end='')

        print('''
*****
*Run*
*****

#Tiempo Promedio:   {}
#Mejor tiempo:      {} por {}
#Peor Tiempo:       {} por {}     
'''.format(retorno[3][0], retorno[3][1], retorno[3][2], retorno[3][3], retorno [3][4]))
    return decorar


def hora_a_segundo(fecha):
    diccionario_segundos = {}
    for valor, i in enumerate(fecha):
        horas = int(i[0:2]) * 3600
        minutos = int(i[3:5]) * 60
        segundos = int(i[6:8]) + minutos + horas
        diccionario_segundos[segundos] = fecha[valor]
    return diccionario_segundos


def segundo_a_hora(segundos):
    minutos = int(segundos // 60)
    segundos_resto = int(segundos % 60)
    horas = int(minutos // 60)
    minutos_resto = int(minutos % 60)
    if horas < 10:
        resultado = '0{}:{}:{}'.format(horas, minutos_resto, segundos_resto)
        return resultado
    else:
        resultado = ('{}:{}:{}'.format(horas, minutos_resto, segundos_resto))
        return resultado


def analizar_categorias(Data, Categoria):
    '''Parte de la funcion analizar_Ironman, se encarga de
    analizar y retornar los datos analizados de cada categoria
    
    @param Data: Lista con los corredores y sus tiempos
    @param Categoria: String que indica la categoria a analizar'''

    tiempos_categoria_fechas = [corredor[Categoria] for corredor in Data if len(corredor[Categoria]) > 0]
    tiempos_categorias_segundos = hora_a_segundo(tiempos_categoria_fechas)
    tiempo_maximo = tiempos_categorias_segundos.get(max(tiempos_categorias_segundos.keys()))
    autor_maximo = [corredor['Name'] for corredor in Data if corredor[Categoria] == tiempo_maximo]
    tiempo_minimo = tiempos_categorias_segundos.get(min(tiempos_categorias_segundos.keys())) 
    autor_minimo = [corredor['Name'] for corredor in Data if corredor[Categoria] == tiempo_minimo]
    tiempo_promedio = segundo_a_hora(sum(tiempos_categorias_segundos.keys()) / len(tiempos_categorias_segundos.keys()))
    return tiempo_promedio, tiempo_minimo, autor_minimo, tiempo_maximo, autor_maximo


@decordador_Ironman
def analizar_Ironman(Archivo, Division):
    '''Analizador de carreras Ironman, devuelve el mejor tiempo en cada categoria de
    una division

    @param Archivo: Archivo .csv de donde se recogera la info\n
    @param Division: Division que se analizara
    '''
    with open(Archivo) as csvfile:
        data = list(csv.DictReader(csvfile))    
        division = [corredor for corredor in data if corredor['Division'] == Division]
        Swim = analizar_categorias(division, 'Swim')
        Bike = analizar_categorias(division, 'Bike')
        Run = analizar_categorias(division, 'Run')
        return Division, Swim, Bike, Run


def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "texto.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    with open('texto.txt', 'r') as fi:
        caracteres = 0
        for linea in fi:
            caracteres += len(linea)
        print("Hay un total de", caracteres, "caracteres")

def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    with open('texto_2.txt', 'w') as fi:
        caracteres_ingresados = 0
        while True:
            texto = input('Escriba el texto a transcribir\n')
            if texto == '':
                break
            else:
                fi.write("{}\n".format(texto))
                caracteres_ingresados += len(texto)
        print('Se ha escrito un total de', caracteres_ingresados, 'caracteres en total sin contar espacios')
            
def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = 2

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
        ambientes = input('Ingrese la cantidad de ambientes para analizar: ')
        analisis = [departamento for departamento in data if departamento['ambientes'] == ambientes if departamento['moneda'] == 'ARS']
        valores = [float(i['precio']) for i in analisis]
        valor_promedio = sum(valores) / len(valores)
        valor_max = max(valores)
        valor_min = min(valores)
        print('''
Departamento de {} ambiente/s
----------------------------
Valor promedio: {}
Valor Maximo:   {}
Valor Minimo:   {}'''.format(ambientes, valor_promedio, valor_max, valor_min))

def ej4():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    '''
    analizar_Ironman('dataset_Ironman_Championship.csv', 'MPRO')
    analizar_Ironman('dataset_Ironman_Championship.csv', 'M45-49')
    analizar_Ironman('dataset_Ironman_Championship.csv', 'M25-29')
    analizar_Ironman('dataset_Ironman_Championship.csv', 'M18-24')


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
