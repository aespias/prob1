# @ Autor: Angel Manuel Espias Alvarez 

# Combinatorios. Version 9 (Comenzado el 09/09/22) 
# ALL IN ONE (AIO) ---> No divido en modulos, todo va junto, mediante funciones

# Dia actual 24/01/23

# Hecho anteriormente:
# --------------------
# Salida por pantalla a traves del metodo .format
# Agrupare en funciones cada modulo
# Poner la fecha al programa actual
# Darle salida al resultado mediante un archivo de texto
# Salida a traves de una ventana de Windows
# Salida a traves de columnas con la funcion Pandas (Dataframe)
# Colocar cada funcion de inicio y final de tiempo en una funcion cada una, y que cada bloque llame a una y a otra
# Hacer un menu para que pida la opcion a escoger antes de hacer todas las combinaciones
# Agregar la opcion de la combinacion aleatoria normal (sin combinaciones entre columnas)
# Conseguido colocar cada parte en una funcion mediante la funcion "global"
  # 1 - Recordar que solo existen los valores dentro de una funcion pero no fuera de ella
  # 2 - Dentro de una funcion los valores son locales y solo se comparten dentro de esa funcion, fuera de ella NO EXISTEN
  # 3 - Para poder compartir los valores de las funciones con otras funciones usamos la funcion (global)
# Conseguido mejorar la salida por columnas (ya que aparecian los resultados antes que las columnas)
# Añadido el metodo de Lustig - Hiltner (la combinacion que tiene mas probabilidad es la formada por 3 numeros impares y 2 pares)
# Crear dos funciones (una para el Euromillon y otra para la bonoloto)
# Comprobar que en cada eleccion se ejecuta el tiempo inicial y el final
# Dar salida a los resultados en colores para hacerlo mas vistoso con la funcion COLORAMA EN BONOLOTO
# Dar salida a los resultados en colores para hacerlo mas vistoso con la funcion COLORAMA EN BONOLOTO
# Crear un contador de ciclos (Bonoloto y Euromillon) en la comparacion de dos columnas
# Que funcionen todas las opciones de ambos programas (REALIZADO)
# Refrescar la pantalla en los ciclos while para que no se acumulen y se vayan refrescando los resultados
# Hacer el archivo ejecutable (la explicacion esta lineas mas abajo)
# Colocar el numero de combinaciones a combinar (5+2 Euromillones) y (6 bonoloto)
# Ordenar la salida de mayor a menor de la comparacion entre dos combinaciones y que no se repitan
# Convertirlo en ejecutable

# En esta version intentare:
# --------------------------
# 1. Acceso a la pagina de internet de combinaciones de loteria para guardar los datos (NO REALIZADO)
# 2. Mejorar el menu de la ventana de Tkinter (NO REALIZADO)
# 3. Añadir comandos de voz (salida de voz) (NO REALIZADO)
# 4. Crear excepciones a la hora de escoger las opciones (es decir, si marco una opcion incorrecta que me avise) (NO TERMINADO)
# 5. Enviar por Whatsapp el resultado (NO REALIZADO)
# 8. Dividir el programa en modulos y llamarse entre ellos (NO REALIZADO)
# 9. Poner un contador de progreso al iniciar el programa (ya que tarda)
# 10.Crear un ejecutable APK para el movil
# 11. Al hacer el ejecutable evito que se cierre el resultado con un INPUT para regresar al menu principal (REALIZADO)
# 12. Agregar la importacion del modulo WEBSCRAPING a este modulo base (AIO) (NO REALIZADO)


# --------------------------------------------------------------------------------------------------------------------------
# CONVERSION EN ARCHIVO EJECUTABLE:
# En la consola escribir ---> pyinstaller --onefile nombrearchivo.py (pyinstaller ya lo he instalado yo mediante la consola)
# El archivo ha de estar en el directorio donde estan los programas
# Una vez hecho se crearan dos carpetas, BUILD y DIST <--- el ejecutable se encontrara en la carpeta DIST
# NOTA: La orden ---> pyinstaller --windowed --onefile main.py <-- La opcion windowed se utiliza para que no aparezca la consola detrás al ejecutar el programa .exe, 
# si el programa es de uso en consola hay que quitar este comando, si estamos ejecutando un programa con interfaz gráfica (Tkinter) lo dejamos puesto.
# El comando –onefile es para que nos cree un solo archivo, si lo quitamos nos crea una carpeta con mas archivos que deberemos tenerlos junto al .exe para ejecutarlo.
# --------------------------------------------------------------------------------------------------------------------------

from doctest import script_from_examples
from email.utils import localtime # Funcion tiempo
from fileinput import close # Funcion de la libreria creacion archivo de texto
from random import randint # Libreria de funciones aleatorias
from random import * # Libreria de funciones aleatorias
import random # Funciones aleatorias
from random import sample # Con SAMPLE evitaremos que se repitan los numeros al sacar combinaciones
from re import I
from time import * # Funcion tiempo, para crear retardo en este caso
import time
from turtle import back # Funcion tiempo (Dia y hora)
from xml.etree.ElementTree import QName 
import pandas as pd # Funcion para adr salida en formato columnas
import tkinter as tk # Funcion para crear una ventana
import sys # Funcion que permite dar salida al texto de la terminal hacia la ventana Tkinter
import os # Funcion necesaria para poder crear el archivo de texto, incluso borrar pantalla
import random as rd
from os import system
import colorama # Funcion para colorear texto (la descripcion esta un poco mas abajo)
from colorama import *
from colorama import Fore # Importacion de estilos del modulo colorama
from colorama import Style # Importacion de estilos del modulo colorama

# ------------------------------------------------------------------------------------------------------------------------------
# EL MODULO COLORAMA:
# (Expongo la explicacion de este modulo aqui ya que la ire utilizando a lo largo del programa,
#  es muy simple de utilizar, intentar recordar su sintaxis, es facil, recordar que hay que inicializarlo cuando se vaya a usar)

# Colorama es un módulo desarrollado por Arnon Yaari que facilita la aplicación de formatos a las salidas por la consola. 
# Por un lado evita tener que expresar con valores numéricos los estilos y colores. 
# En su lugar, se utilizan sus nombres en inglés que favorecen la lectura del código. 
# y como mejora ofrece la posibilidad de desplazar el cursor a una posición de pantalla antes de aplicar un formato.

# -----------------
# Estilos*	(Style)
# Débil	DIM
# Normal	NORMAL
# Brillante	BRIGHT
# Reset	RESET_ALL
# ------------------

# ---------------------------------
# Colores Texto/Fondo	(Fore/Back)
# Negro	BLACK
# Rojo RED
# Verde	GREEN
# Amarillo YELLOW
# Azul BLUE
# Morado MAGENTA
# Cian	CYAN
# Blanco WHITE
# Reset	RESET
# ---------------------------------

# Después de la línea de "import" se inicializa Colorama con el método init() y, a continuación, 
# se aplican formatos a distintas salidas de texto. 
# También, se utilizan los métodos RESET y RESET_ALL para restablecer estilos y colores. 
# ------------------------------------------------------------------------------------------------------------------------------

colorama.init()

# -----------------------------------------------------------------------------------------------
# ------------------------------------ MENU INICIAL ---------------------------------------------
# -----------------------------------------------------------------------------------------------
def init_menu():
    system ("cls")
    print("")
    print(Fore.YELLOW + Style.BRIGHT + "Selecciona Juego")
    print("----------------" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Bonoloto")
    print(Fore.CYAN + "2. Euromillones")
    print(Fore.CYAN + "3. Salir")
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + "")
    choice_menu_ppal = int(input("Elige una opcion: "))
    if choice_menu_ppal == 1:
        system ("cls")
        print("")
        print(Fore.YELLOW + Style.BRIGHT + "")
        menu_bono()
    elif choice_menu_ppal == 2:
        system ("cls")
        print(Fore.YELLOW + Style.BRIGHT + "" )
        menu_euro()
    elif choice_menu_ppal == 3:
        system("cls")
        print(Fore.RED + "\nSaliendo...")
        sleep(4)
        exit
    else:
        system ("cls")
        print("")
        print(Fore.RED + Style.NORMAL + "¡Opcion incorrecta!" + Style.RESET_ALL)
        sleep(1)
        print("")
        print(Fore.GREEN + Style.BRIGHT + "Regresando al menu principal..." + Style.RESET_ALL)
        sleep(1)
        init_menu()

# -----------------------------------------------------------------------------------------------
# ------------------------------------ MENU BONOLOTO --------------------------------------------
# -----------------------------------------------------------------------------------------------
def menu_bono():
    system("cls")
    print(Fore.YELLOW + Style.BRIGHT + "---------------------------------------------------------------------")
    print("----------------------- MENU BONOLOTO -------------------------------")
    print("----------------------------------------------------------------------\n")
    print(Fore.CYAN + Style.BRIGHT + "1. Generador simple")
    print("2. Metodo Lustig-Hiltner (Mayor probabilidad) (3 impares - 2 pares)")
    print("3. Generador por comparacion entre dos combinaciones")
    print("4. Regresar al menu principal")
    print("5. Salir")
    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + "")
    menu_bono = int(input("Escoge una opcion: "))
    if menu_bono == 1:
        system("cls") # Borramos la pantalla para limpiarla
        time_execution_begin() # Muestra la fecha/hora en la que el programa comienza
        tiempo_ejecucion_inicial()
        generador_ppal_bono() # Ejecuta la funcion principal 
        time_execution_end() # Muestra la fecha/hora en la que el programa termina
        tiempo_ejecucion_final()
    elif menu_bono == 2:
        system("cls")
        print(Fore.YELLOW + Style.NORMAL + "\nAVISO:\nSe calculara la combinacion de Lusting - Hilter entre 3 numeros impares y tres pares")
        sleep(4)
        print(Fore.GREEN + "\nIniciando el programa...")
        sleep(4)
        time_execution_begin()
        metodo_Lusting_Hiltner_Numeros_bono()
    elif menu_bono == 3:
        system("cls")
        print(Fore.YELLOW + Style.BRIGHT + "-------------------------------------------------------")
        print("-------- COMPARACION ENTRE DOS COMBINACIONES ----------")
        print("-------------------------------------------------------" + Style.RESET_ALL)
        print(Fore.CYAN + Style.BRIGHT + "\n1. Impresion del resultado por CONSOLA")
        print("2. Impresion del resultado por COLUMNAS")
        print("3. Impresion del resultado por VENTANA EMERGENTE") #QUEDA POR AÑADIR
        print("4. Regresar al menu principal")
        print("5. Salir del programa" + Style.RESET_ALL)
    
        menu_bono_int = int(input("\nEscoge una opcion: "))
        if menu_bono_int == 1:
            system("cls") # Borramos la pantalla para limpiarla
            time_execution_begin() # Muestra la fecha/hora en la que el programa comienza
            tiempo_ejecucion_inicial() # Empieza a contar el tiempo que tarda en ejecutarse el script
            funcion_de_trabajo_bono() # Ejecuta la funcion principal 
            time_execution_end()
            tiempo_ejecucion_final() # Muestra el tiempo que ha tardado en ejecutarse el script al completo
            print("")
        elif menu_bono_int == 2:
            system("cls") # Borramos la pantalla para limpiarla
            time_execution_begin() # Muestra la fecha/hora en la que el programa comienza
            tiempo_ejecucion_inicial() # Empieza a contar el tiempo que tarda en ejecutarse el script
            frame_en_columnas_bono() # Ejecuta la funcion principal 
            time_execution_end() # Muestra la fecha/hora en la que el programa termina
            tiempo_ejecucion_final() # Muestra el tiempo que ha tardado en ejecutarse el script al completo
        elif menu_bono_int == 3:
            print("Impresion ventana emergente")
        if menu_bono_int == 4:
            system("cls")
            print(Fore.GREEN + Style.BRIGHT + "\nRegresando al menu principal...")
            sleep(2)
            init_menu()
        else:
            system("cls")
            print(Fore.RED + "\nSaliendo...")
            sleep(4)
            exit

    elif menu_bono == 4:
        system("cls")
        print(Fore.GREEN + Style.BRIGHT + "\nRegresando al menu principal...")
        sleep(2)
        init_menu()

    else:
        system("cls")
        print(Fore.RED + Style.BRIGHT + "\nSaliendo...")
        sleep(2)
        exit()

# -----------------------------------------------------------------------------------------------
# ------------------------------------ MENU EUROMILLONES ----------------------------------------
# -----------------------------------------------------------------------------------------------
def menu_euro():
    system("cls")
    print(Fore.YELLOW + Style.BRIGHT + "------------------------------------------------------------")
    print("----------------- MENU EUROMILLONES ------------------------")
    print("------------------------------------------------------------\n" + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + "1. Generador de combinacion simple")
    print("2. Metodo Lustig-Hiltner (Mayor probabilidad) (3 impares - 2 pares)")
    print("3. Generador por comparacion entre dos combinaciones")
    print("4. Regresar al menu principal")
    print("5. Salir\n" + Style.RESET_ALL)
    
    menu_euro = int(input("Escoge una opcion: "))
    if menu_euro == 1:
        system("cls") # Borramos la pantalla para limpiarla
        time_execution_begin() # Muestra la fecha/hora en la que el programa comienza
        tiempo_ejecucion_inicial()
        generador_ppal_euro() # Ejecuta la funcion principal 
        time_execution_end() # Muestra la fecha/hora en la que el programa termina
        tiempo_ejecucion_final()
    elif menu_euro == 2:
        system("cls") # Borramos la pantalla para limpiarla
        time_execution_begin() # Muestra la fecha/hora en la que el programa comienza
        tiempo_ejecucion_inicial()
        nums_stars_Lus_Hil_euro() # Ejecuta la funcion principal 
        time_execution_end() # Muestra la fecha/hora en la que el programa termina
        tiempo_ejecucion_final()
    elif menu_euro == 3:
        system("cls")
        print(Fore.YELLOW + Style.BRIGHT + "--------------------------------------------------")
        print("COMPARACION ENTRE DOS COMBINACIONES (EUROMILLONES)")
        print("---------------------------------------------------" + Style.RESET_ALL)
        print(Fore.CYAN + Style.BRIGHT + "\n1. Impresion del resultado por CONSOLA")
        print("2. Impresion del resultado por COLUMNAS")
        print("3. Impresion del resultado por VENTANA EMERGENTE")
        print("4. Impresion del resultado mediante archivo de texto")
        print("5. Regresar al menu principal")
        print("6. Salir\n" + Style.RESET_ALL)
        menu_euro_int = int(input("Escoge una opcion: "))
        if menu_euro_int == 1:
            system("cls") # Borramos la pantalla para limpiarla
            time_execution_begin() # Muestra la fecha/hora en la que el programa comienza
            tiempo_ejecucion_inicial() # Empieza a contar el tiempo que tarda en ejecutarse el script
            funcion_de_trabajo_euro() # Ejecuta la funcion principal 
            time_execution_end() # Muestra la fecha/hora en la que el programa termina
            tiempo_ejecucion_final() # Muestra el tiempo que ha tardado en ejecutarse el script al completo
        elif menu_euro_int == 2:
            system("cls") # Borramos la pantalla para limpiarla
            time_execution_begin() # Muestra la fecha/hora en la que el programa comienza
            tiempo_ejecucion_inicial() # Empieza a contar el tiempo que tarda en ejecutarse el script
            miframe_euro() # Ejecuta la funcion principal 
            time_execution_end()
            tiempo_ejecucion_final() # Muestra el tiempo que ha tardado en ejecutarse el script al completo
        elif menu_euro_int == 3:
            system("cls") # Borramos la pantalla para limpiarla
            time_execution_begin() # Muestra la fecha/hora en la que el programa comienza
            tiempo_ejecucion_inicial() # Empieza a contar el tiempo que tarda en ejecutarse el script
            windows_out_euro() #Ejecuta la funcion principal 
            time_execution_end() # Muestra la fecha/hora en la que el programa termina
            tiempo_ejecucion_final() # Muestra el tiempo que ha tardado en ejecutarse el script al completo
        elif menu_euro_int == 4:
            system("cls") # Borramos la pantalla para limpiarla
            time_execution_begin() # Muestra la fecha/hora en la que el programa comienza
            tiempo_ejecucion_inicial()
            text_file_euro() #Ejecuta la funcion principal 
            time_execution_end() # Muestra la fecha/hora en la que el programa termina
            tiempo_ejecucion_final()
        elif menu_euro_int == 5:
            system("cls")
            print(Fore.GREEN + Style.BRIGHT + "\nRegresando al menu principal...")
            sleep(2)
            init_menu()
        else:
            system("cls")
            print(Fore.RED + Style.BRIGHT + "\nSaliendo...")
            sleep(2)
            exit() # Salimos
    elif menu_euro == 4:
        system("cls")
        print(Fore.GREEN + Style.BRIGHT + "\nRegresando al menu principal...")
        sleep(2)
        init_menu()
    else:
        system("cls")
        print(Fore.RED + Style.BRIGHT + "\nSaliendo...")
        sleep(2)
        exit()


# ------------------------------------------------------------
# ---------FUNCION TIEMPO DE EJECUCION DE SCRIPT--------------
# ------------------------------------------------------------

# SOLO UTILIZARE EL CALCULO DE TIEMPO DE EJECUCION PARA PROCESOS LARGOS <--- COMBINACIONES ENTRE DOS SERIES

def tiempo_ejecucion_inicial(): # Cuenta el tiempo desde que se inicia el script
    global inicio #uso variable global para compartir el resultado fuera de la funcion
    inicio = time.time() # <--- FUNCION PARA CALCULAR EL TIEMPO DE LA EJECUCION time.time() 

def tiempo_ejecucion_final(): #Cuenta hasta el tiempo que finaliza el script
    global fin # uso variable global para compartir el resultado fuera de la funcion
    fin = time.time() # <--- FUNCION PARA CALCULAR EL TIEMPO DE LA EJECUCION time.time() 
    tiempo_global = fin-inicio # EL TIEMPO TOTAL DE EJECUCION SE OBTIENE RESTANDO EL TIEMPO FINAL DEL INICIAL
    print(Fore.RED + Style.BRIGHT + "Tiempo de ejecucion del script:", round((tiempo_global)/60), "minuto\s")


# ------------------------------------------------------------
# ------------------ FUNCION TIEMPO --------------------------
# ------------------------------------------------------------

def time_execution_begin(): # HORA EN LA QUE SE INICIA EL PROGRAMA
    t_inicial = time.asctime(time.localtime(time.time())) # Utilizamos la funcion time y la incluimos dentro de la variable "tiempo"
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "\nPrograma inicializado el: ", t_inicial, "\n" + Style.RESET_ALL) #Imprimimos cuando comienza el programa (Fecha + Hora)


def time_execution_end(): # HORA EN LA QUE EL PROGRAMA TERMINA
    t_terminacion = time.asctime(time.localtime(time.time()))
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "Programa terminado a las: ", t_terminacion, "\n" + Style.RESET_ALL)


# ***********************************************************************************************************
# ************************************* CUERPO DEL PROGRAMA BONOLOTO ****************************************
# ***********************************************************************************************************
#
# GENERADOR DE COMBINACION PRINCIPAL (BONOLOTO):
# ----------------------------------------------
def generador_ppal_bono():
    print("")
    num = random.sample(range(1,49), 6) # Con la funcion SAMPLE los numeros no se repiten
    conv_cadena_num = str(sorted(num)) # la f(x) SORTED es para ordenarlos, hay que ponerlos STR ya que al utilizar COLORAMA hay que ponerlo asi
    print(Fore.YELLOW + Style.BRIGHT + "Combinacion resultante:")
    print("-----------------------" + Style.RESET_ALL)
    print(Fore.CYAN + Style.DIM + "\nNumeros: ", Fore.GREEN + conv_cadena_num + Style.RESET_ALL)
    print("")


# -------------------------------------------------------------    
# GENERADORES DE COMPARACION ENTRE DOS COMBINACIONES (BONOLOTO)
# -------------------------------------------------------------
def generador_primario_bono(): #Primera funcion generadora de dos numeros aleatorios a comparar con la segunda
    G1 = []
    gen_prim = sorted(sample(range(1,49), 6)) #Agrego este cambio, ya que asi SE GENERAN 5 COMBINACIONES DE NUMEROS POR ORDEN Y SIN REPETIRSE
    G1.append(gen_prim) 
    return G1

def generador_secundario_bono(): # Segunda funcion aleatoria generadora de dos numeros aleatorios a comparar con la primera
    G2 = []
    gen_secun = sorted(sample(range(1,49), 6)) #Agrego este cambio, ya que asi SE GENERAN 5 COMBINACIONES DE NUMEROS POR ORDEN Y SIN REPETIRSE
    G2.append(gen_secun)
    return G2


# ----------------------------------------------------------
# FUNCION DE TRABAJO PRINCIPAL - POR COMPARACION (BONOLOTO):
# ----------------------------------------------------------
def funcion_de_trabajo_bono(): # Funcion de trabajo principal
    global X
    global Y
    X = [] #Lista en la cual se iran almacenando los valores aleatorios
    Y = [] #Segunda lista a comparar con la primera
    opc = False #Es como la opcion de True para hacer un bucle infinito hasta haber coincidencia
    cont = 0 #Hacemos un contador para que nos cuente las combinaciones que se hacen hasta dar con la coincidencia
    system("cls")
    print(Fore.YELLOW + Style.BRIGHT + "Comparacion entre 2 combinaciones" + Style.RESET_ALL)
    while opc != True:
        M = generador_primario_bono() #Metemos la 1a funcion generadora dentro de una variable
        N = generador_secundario_bono() #Hacemos lo mismo con la segunda funcion generadora
        X.append(M) #Vamos agregando a la lista X los valores que se van generando en la funcion generadora primaria
        Y.append(N) #Lo mismo pero con la lista generadora secundaria
        
        # system("cls") <-------- DESBLOQUEAR SI QUEREMOS QUE SE VAYA BORRANDO Y ACTUALIZANDO LA PANTALLA
        
        # NOTA: (he eliminado de la version previa V4 la salida con la funcion format ya que no me permitia usar la galeria colorama,
        # de todos modos dejo en la linea de abajo como era la funcion format que utilizaba previamente)
        # print(Fore.BLUE + "Combinacion 1: \n--------------\n{}\n\nCombinacion 2: \n--------------\n {}\n".format(X, Y))

        print("\t\t\t\t\t\t\t\t" + Back.RED + "Vuelta", cont, "\n" + Style.RESET_ALL)
        print(Fore.CYAN + Style.DIM + "Combinacion 1: ", Fore.GREEN + str(X) + Style.RESET_ALL)
        print("")
        print(Fore.CYAN + Style.DIM + "Combinacion 2: ", Fore.GREEN + str(Y) + Style.RESET_ALL) 
        print("") #A traves de .format es como he encontrado la manera mas vistosa de imprimir, aunque hay mas
        sleep(0.2) #dejamos pasar un intervalo pequeño de tiempo entre cada combinacion
    
        cont += 1 #inicializamos el contador de combinaciones (ANTES DEL BUCLE FOR)
        for i in X: #Iniciamos el bucle, ira comparando ambas listas X e Y hasta que encuentre una coincidencia
            for j in Y:
                if (i == j):
                    print(Fore.CYAN + Style.DIM + "Coincidencia con: ", Fore.GREEN + str(i) + Style.RESET_ALL)
                    print(Fore.CYAN + Style.DIM + "Se han generado", Style.RESET_ALL + Fore.GREEN + str(cont) + Style.RESET_ALL + Fore.CYAN + Style.DIM+  " combinaciones")
                    print(Fore.CYAN + Style.DIM + "La lista tiene una longitud de", Style.RESET_ALL + Fore.GREEN ,len(X+Y), Style.RESET_ALL + Fore.CYAN + Style.DIM + "elementos")
                    
                    #Recordar que len sirve para mostrar la longitud de una cadena, en este caso es el numero de elementos que han hecho falta para encontrar la coincidencia

                    opc = True #Hacemos la parada del ciclo y muestra de los resultados seguidos
                    print("")
                    time_execution_end()
                    sleep(3) #Paramos 3 segundos para imprimir el resultado en columnas
                    final_ask = str(input("\n¿Deseas volver al menu principal? (s/n): "))
                    if final_ask == "s":
                        init_menu()
                    else:
                        exit()
                    

# ----------------------------------------------------------------------------------------------------
# ------------------ FUNCION FRAMEWORK (Resultado en columnas) (BONOLOTO) ----------------------------
# ----------------------------------------------------------------------------------------------------
def frame_en_columnas_bono():
    Z = [] #Lista en la cual se iran almacenando los valores aleatorios
    T = [] #Segunda lista a comparar con la primera
    opc = False #Es como la opcion de True para hacer un bucle infinito hasta haber coincidencia
    cont = 0 #Hacemos un contador para que nos cuente las combinaciones que se hacen hasta dar con la coincidencia

    while opc != True:
        M = generador_primario_bono() #Metemos la 1a funcion generadora dentro de una variable
        N = generador_secundario_bono() #Hacemos lo mismo con la segunda funcion generadora
        Z.append(M) #Vamos agregando a la lista X los valores que se van generando en la funcion generadora primaria
        T.append(N) #Lo mismo pero con la lista generadora secundaria
        sleep(0.2) #dejamos pasar un intervalo pequeño de tiempo entre cada combinacion
        print(Fore.YELLOW + Style.BRIGHT)
        df = pd.DataFrame({"Columna A:":Z, "Columna B:":T}) # Realizamos el Dataframe con la libreria Pandas, como se ve es facil
        system("cls") # Asi evito que se vayan acumulando filas y numeros (sale la lista de una sola vez)
        print(df) # Imprimimos el resultado en columnas, gracias a la funcion DataFrame de la libreria Pandas
        
        cont += 1 #inicializamos el contador de combinaciones (ANTES DEL BUCLE FOR)
        for v in Z: #Iniciamos el bucle, ira comparando ambas listas X e Y hasta que encuentre una coincidencia
            for w in T:
                if (v == w):
                    print(Fore.CYAN + Style.DIM + "\nCoincidencia con:", Style.RESET_ALL + Fore.GREEN, v)
                    print(Fore.CYAN + Style.DIM + "Se han generado", Style.RESET_ALL + Fore.GREEN, cont , Style.RESET_ALL + Fore.CYAN +Style.DIM +"combinaciones")
                    print(Fore.CYAN + Style.DIM + "La lista tiene una longitud de", Style.RESET_ALL + Fore.GREEN, len(Z+T), Style.RESET_ALL + Fore.CYAN + Style.DIM + "elementos") #Recordar que len sirve para mostrar la longitud de una cadena, en este caso es el numero de elementos que han hecho falta para encontrar la coincidencia
                    print("")
                    opc = True #Hacemos la parada del ciclo y muestra de los resultados seguidos
                    sleep(0.5) #Paramos 3 segundos para imprimir el resultado en columnas
                    time_execution_end()
                    exit()
                

# -----------------------------------------------------------------------------------------
# ------------------ METODO DE LUSTING - HILTNER (BONOLOTO) -------------------------------
# -----------------------------------------------------------------------------------------  
# 
# --------------------------------- METODOS -----------------------------------------------
#
# Richard Lustig: En sorteos tipo Euromillones, con cinco números a elegir hasta el 50, 
#                 la suma de todos debe estar entre los 104 y 176.
# Metodo Hiltner: elegir 3 numeros impares y dos pares, 
#                 (el número de combinaciones favorables de esos números es de 690.000, 
#                 mientras que el total de combinaciones posibles en el Euromillones es de 2.118.760).
#                 es decir, que de cada 100 sorteos en los que elijas ese patrón de números en 48 ocasiones aparecerá.
#
# Aplicaremos ambos metodos a la vez


def metodo_Lusting_Hiltner_Numeros_bono():
    pares = [] # Lista en la que almacenaremos los numeros pares
    impares = [] # Lista para almacenar numeros impares

    for i in range(1,49): # Iteramos mediante FOR en el rango que queremos
        if i%2 == 0: # Si el modulo es CERO significa que el numero es PAR
            pares.append(i) # por lo tanto lo agregamos
        else: # de los contrario el numero es impar
            impares.append(i) # y procedemos a agregarlo

    lista_pares = rd.sample(pares, k=3) # SAMPLE -> Para elegir 2 aleatorios en el rango 1 - 52, k=2 <-- saca 2 numeros
    lista_impares = rd.sample(impares, k=3) # elige 3 aleatorios impares, con k=3 extrae 3 aleatorios
    global lista_total
    lista_total = lista_pares + lista_impares # Juntamos los numeros
    global suma_lista_total # La utilizamos como GLOBAL ya que compartiremos su valor fuera de la funcion
    suma_lista_total = sum(lista_total) # Funcion "sum" que suma todos los elementos de una lista
                                        # Aqui tambien utilizamos la funcion "sum", aunque otro modo de hacerlo es a traves
                                        # de un contador, iterando sobre la lista de numeros, quedaria asi:
                                        # suma_pares = 0
                                        # for suma in lista_pares:
                                        # suma_pares  += suma
                                        # print(suma_pares)
    colorama.init()
    
    Conv_cadena_imp = str(sorted(lista_impares))
    Conv_cadena_par = str(sorted(lista_pares))
    Conv_cadena_valor_Lusting = str(suma_lista_total)
    Conv_cadena_lista_total = str(sorted(lista_total))

    print(Fore.YELLOW + Style.BRIGHT + "\t\t--------------------------")
    print("\t\tMETODO DE LUSTIG - HILTNER")
    print(Fore.YELLOW + Style.DIM + "\t\t--------------------------" + Style.RESET_ALL)
    print(Fore.CYAN + Style.DIM + "\nNumeros impares: " + Style.RESET_ALL , Fore.GREEN + Conv_cadena_imp + Style.RESET_ALL) # Lista de numeros impares (3)
    print(Fore.CYAN + Style.DIM + "\nNumeros pares: " + Style.RESET_ALL, Fore.GREEN + Conv_cadena_par + Style.RESET_ALL) # Lista de numeros pares (2)
    print(Fore.CYAN + Style.DIM + "\nSuma de Lusting (Valor comprendido entre 104 -176): " + Style.RESET_ALL, Fore.GREEN + Style.DIM + Conv_cadena_valor_Lusting) # Sumamos sus elementos
    print(Fore.CYAN + Style.DIM + "\nCOMBINACION: " + Style.RESET_ALL, Fore.GREEN + Style.DIM + Conv_cadena_lista_total + Style.RESET_ALL) # Juntamos pares e impares
    print("")
    time_execution_end()
    exit()


# FUNCION PARA CREAR ARCHIVO DE TEXTO Y AGREGAR LOS DATOS (BONOLOTO)
# --------------------------------------------------------------------
def text_file_bono(): # Funcion para agregar numeros generados a un archivo de texto.
    Work_func = funcion_de_trabajo_bono() # Pasamos la funcion de trabajo a una variable
    file1 = open("C:/Users/Espias/Desktop/aleatorios.txt", "a") # La terminacion en "a" es para que agregue los datos y NO los sobreescriba 
    str1 = repr(Work_func) # Pasamos la anterior funcion de trabajo a otra variable
    file1.write(str1) # Escribimos en el archivo
    file1.close() # Una vez escrito LO CERRAMOS

# Para mostrar el texto en la ventana de tkinter, usare un widget Text:
# Como se ve hay definiciones y clases (estudiarlo - comprenderlo) <-- extraido de stackoverflow
# Mediante la funcion mas abajo indicada "windows_out() consigo pasar los datos a la ventana de windows"

# FUNCION PARA CREAR LA VENTANA DE WINDOWS (TKINTER) (BONOLOTO)
# -------------------------------------------------------------
def windows_out_bono():

    class StdOutRedirect:
        def __init__(self,  text: tk.Text) -> None:
            self._text = text

        def write(self,  out: str) -> None:
            self._text.insert(tk.END,  out)
        
        def flush(self): # Con esto evitamos la salida --> 'StdOutRedirect' object has no attribute 'flush'
                         # la cual no influye para el desarrollo del programa pero es molesta.
            pass
#A partir de aqui estoy empezando a practicar con GIT GUI
#añado otra linea de prueba

    class App(tk.Frame):
        def __init__(self, parent, *args, **kwargs):
            super().__init__(parent,  *args, **kwargs)
            self.stdout_text = tk.Text(
                self,  bg="white",  fg="#38B179",  font=("Helvetica", 15))
            self.stdout_text.pack(expand=True, fill=tk.BOTH)
            sys.stdout = StdOutRedirect(self.stdout_text)
        

    if __name__ == "__main__":
        ventana = tk.Tk() # Creamos la ventana
        ventana.title("Generador de Combinaciones") # Titulo de la ventana
        ventana.config(bg="White") # Color de fondo
        App(ventana).pack(expand=True, fill=tk.BOTH)
        funcion_de_trabajo_euro() # Llamamos a la funcion de trabajo para qe muestre los resultados por ventana
        ventana.update
        ventana.mainloop() # Para que la ventana permanezca abierta




# ***********************************************************************************************************
# *********************************** CUERPO DEL PROGRAMA EUROMILLONES **************************************
# ***********************************************************************************************************

# GENERADOR DE COMBINACION PRINCIPAL (EUROMILLON):
# ---------------------------------------------- 
def generador_ppal_euro():
    num_euro = random.sample(range(1,52), 5)
    stars = random.sample(range(1,12), 2)
    print(Fore.YELLOW + Style.BRIGHT + "Combinacion resultante:")
    print("-----------------------" + Style.RESET_ALL)
    print(Fore.CYAN + Style.DIM + "\nNumeros: " +  Fore.GREEN + str(sorted(num_euro))) #Hace falta convertirlo en cadena para obtener el resultado (por eso utilizo str)
    print(Fore.CYAN + Style.DIM + "\nEstrellas: " +  Fore.GREEN + str(sorted(stars)))
    print("")


# --------------------------------------------------------------------------  
# GENERADORES DE COMPARACION ENTRE DOS COMBINACIONES DE NUMEROS (EUROMILLON)
# --------------------------------------------------------------------------
def generador_primario(): #Primera funcion generadora de dos numeros aleatorios a comparar con la secundaria
    global G1
    G1 = []
    gen_prim = sorted(sample(range(1,52), 5)) #Agrego este cambio, ya que asi SE GENERAN 5 COMBINACIONES DE NUMEROS POR ORDEN Y SIN REPETIRSE
    G1.append(gen_prim)
    return G1

def generador_secundario(): # Segunda funcion aleatoria generadora de dos numeros aleatorios a comparar con la primaria
    global G2
    G2 = []
    gen_secun = sorted(sample(range(1,52), 5)) #Agrego este cambio, ya que asi SE GENERAN 5 COMBINACIONES DE NUMEROS POR ORDEN Y SIN REPETIRSE
    G2.append(gen_secun)
    return G2

# ---------------------------------------------------------------------------- 
# GENERADORES DE COMPARACION ENTRE DOS COMBINACIONES DE ESTRELLAS (EUROMILLON)
# ----------------------------------------------------------------------------

def generador_primario_stars(): #Primera funcion generadora de dos numeros aleatorios a comparar con la secundaria
    global G3
    G3 = []
    gen_prim = sorted(sample(range(1,12), 2))
    G3.append(gen_prim)
    return G3

def generador_secundario_stars(): # Segunda funcion aleatoria generadora de dos numeros aleatorios a comparar con la primaria
    global G4
    G4 = []
    gen_secun = sorted(sample(range(1,12), 2))
    G4.append(gen_secun)
    return G4


# FUNCION LUSTIG - HILTNER (ya explicada en el cuerpo del codigo bonoloto, solo que en este caso tambien extraeremos la estrellas)
# --------------------------------------------------------------------------------------------------------------------------------
def nums_stars_Lus_Hil_euro(): # EN ESTA FUNCION AGRUPO OTRAS FUNCIONES <-- MIRAR BIEN, ¡¡FUNCIONA!!
        
        system("cls")
        
        # FUNCION PARA GENERAR LOS 5 NUMEROS
        # ----------------------------------
        def metodo_Lusting_Hiltner_Numeros():
            pares = [] # Lista en la que almacenaremos los numeros pares
            impares = [] # Lista para almacenar numeros impares

            for i in range(1,52): # Iteramos mediante FOR en el rango que queremos
                if i%2 == 0: # Si el modulo es CERO significa que el numero es PAR
                    pares.append(i) # por lo tanto lo agregamos
                else: # de los contrario el numero es impar
                    impares.append(i) # y procedemos a agregarlo

            colorama.init() # Si no lo inicializamos da error
            
            lista_pares = rd.sample(pares, k=2) # SAMPLE -> Para elegir 2 aleatorios en el rango 1 - 52, k=2 <-- saca 2 numeros
            lista_impares = rd.sample(impares, k=3) # elige 3 aleatorios impares, con k=3 extrae 3 aleatorios
            str_lista_pares = str(sorted(lista_pares))
            str_lista_impares = str(sorted(lista_impares))
            global lista_total
            lista_total = lista_pares + lista_impares # Juntamos los numeros
            global suma_lista_total # La utilizamos como GLOBAL ya que compartiremos su valor fuera de la funcion
            suma_lista_total = sum(lista_total) # Funcion "sum" que suma todos los elementos de una lista
                                                # Aqui tambien utilizamos la funcion "sum", aunque otro modo de hacerlo es a traves
                                                # de un contador, iterando sobre la lista de numeros, quedaria asi:
                                                # suma_pares = 0
                                                # for suma in lista_pares:
                                                # suma_pares  += suma
                                                # print(suma_pares)
            print(Fore.YELLOW + Style.BRIGHT + "\t\t--------------------------")
            print("\t\tMETODO DE LUSTIG - HILTNER")
            print("\t\t--------------------------" + Style.RESET_ALL)
            print(Fore.CYAN + Style.DIM + "\nNumeros impares: " + Style.RESET_ALL, Fore.GREEN + str_lista_impares) # Lista de numeros impares (3)
            print(Fore.CYAN + Style.DIM + "\nNumeros pares: " + Style.RESET_ALL, Fore.GREEN + str_lista_pares) # Lista de numeros pares (2)
            print(Fore.CYAN + Style.DIM + "\nSuma de Lusting (Valor comprendido entre 104 -176): " + Style.RESET_ALL, Fore.GREEN + str(suma_lista_total)) # Sumamos sus elementos
            print(Fore.CYAN + Style.DIM + "\nNUMEROS: " + Style.RESET_ALL, Fore.GREEN + str(sorted(lista_total))) # Juntamos pares e impares
            print("")

        
        # FUNCION PARA GENERAR LAS 2 ESTRELLAS
        # ------------------------------------
        def Estrellas():
            stars = rd.sample(range(1,12), 2) # Para utilizar la funcion SAMPLE tenemos que importarla de random
            print(Fore.CYAN + Style.DIM + "ESTRELLAS: " + Style.RESET_ALL, Fore.GREEN + str(sorted(stars)))
            print("")

        metodo_Lusting_Hiltner_Numeros() # Aplicamos la funcion para extraer los numeros
        Estrellas() # F(x) para extraer las estrellas

        while suma_lista_total < 104 or suma_lista_total >176: # CONDICIONAL (para entrar en el rango de Lusting)
            os.system ("cls")
            metodo_Lusting_Hiltner_Numeros()
            if suma_lista_total > 104 or suma_lista_total <176:
                os.system ("cls")
                print(lista_total)


# ----------------------------------------------------------------------
# FUNCION DE TRABAJO PRINCIPAL NUMEROS - POR COMPARACION (EUROMILLONES):
# ----------------------------------------------------------------------

def funcion_de_trabajo_euro(): # Funcion de trabajo principal                     
    
    # RECORDAR QUE UNA VARIABLE SOLO FUNCIONA DENTRO DE LA FUNCION A LA QUE PERTENECE
    # Para poder utilizar los valores de una funcion en otra funcion hay que declarar las variables como GLOBAL
    
    global X # Utilizamos GLOBAL para poder enviar el valor a otras funciones fuera de esta
    global Y # Lo mismo, asi podemos exportar el valor Y a cualquier funcion fuera de esta
    global i # lo mismo con i 
    global cont # lo mismo con el contador

    X = [] #Lista en la cual se iran almacenando los valores aleatorios
    Y = [] #Segunda lista a comparar con la primera
    i = [] # Para inicializar el bucle comparador de numeros
    
    i_s = [] # Para inicializar el bucle comparador de estrellas
    S1_stars = []
    S2_stars = []
    
    opc = False #Es como la opcion de True para hacer un bucle infinito hasta haber coincidencia
    cont = 0 #Hacemos un contador para que nos cuente las combinaciones que se hacen hasta dar con la coincidencia
    cont_s = 0
    system("cls")
    print(Fore.YELLOW + Style.BRIGHT + "Comparacion entre 2 combinaciones" + Style.RESET_ALL)

    while opc != True:
        
        M = generador_primario() #Metemos la 1a funcion generadora dentro de una variable
        N = generador_secundario() #Hacemos lo mismo con la segunda funcion generadora
        X.append(M) #Vamos agregando a la lista X los valores que se van generando en la funcion generadora primaria
        Y.append(N) #Lo mismo pero con la lista generadora secundaria 

        # system("cls") <-- ACTIVANDO ESTA OPCION LA PANTALLA SE REFRESCARA EN CADA CICLO DEL BUCLE
      
        # NOTA: En esta version elimino tal y como comente anteriormente la funcion format, ya que no me permitia usar la libreria colorama
        # print("Combinacion 1: \n--------------\n{}\n\nCombinacion 2: \n--------------\n {}\n".format(X, Y)) #A traves de .format es como he encontrado la manera mas vistosa de imprimir, aunque hay mas
        print("\t\t\t\t\t" + Back.RED + "Vuelta", cont, "\n" + Style.RESET_ALL)
        print(Fore.CYAN + Style.DIM + "Combinacion numeros A: ", Fore.GREEN + str(X) + Style.RESET_ALL)
        print("")
        print(Fore.CYAN + Style.DIM + "Combinacion numeros B: ", Fore.GREEN + str(Y) + Style.RESET_ALL) 
        print("") #A traves de .format es como he encontrado la manera mas vistosa de imprimir, aunque hay mas
        sleep(0.2) #dejamos pasar un intervalo pequeño de tiempo entre cada combinacion

        cont += 1 #inicializamos el contador de combinaciones (ANTES DEL BUCLE FOR)
        for i in X: #Iniciamos el bucle, ira comparando ambas listas X e Y hasta que encuentre una coincidencia
            for j in Y:
                if (i == j):
                        sleep(5)
                        print(Fore.CYAN + Style.DIM + "Coincidencia de numeros con: ", Style.RESET_ALL + Fore.GREEN + str(i),"\n" + Style.RESET_ALL)
                        print(Fore.CYAN + Style.DIM + "Se han generado", Style.RESET_ALL + Fore.GREEN + str(cont) + Style.RESET_ALL + Fore.CYAN + Style.DIM + " combinaciones", "\n" + Style.RESET_ALL)
                        print(Fore.CYAN + Style.DIM + "La lista tiene una longitud de" , Style.RESET_ALL + Fore.GREEN + str(len(X+Y)) + Style.RESET_ALL + Fore.CYAN + Style.DIM +  " elementos", "\n" + Style.RESET_ALL) #Recordar que len sirve para mostrar la longitud de una cadena, en este caso es el numero de elementos que han hecho falta para encontrar la coincidencia
                        opc = True #Hacemos la parada del ciclo y muestra de los resultados seguidos
                        
                        print(Fore.LIGHTYELLOW_EX + "\nProcesando estrellas...")
                        sleep(4)
    funcion_de_trabajo_euro_stars()
                        

# ----------------------------------------------------------------------
# FUNCION DE TRABAJO PRINCIPAL ESTRELLAS - POR COMPARACION (EUROMILLONES):
# ----------------------------------------------------------------------

def funcion_de_trabajo_euro_stars(): # Funcion de trabajo principal para generar estrellas                  
                                     # Es igual que la funcion anterior para los numeros, de hecho invoco a esta funcion al final
                                     # de la anterior para que saque el resultado

    # RECORDAR QUE UNA VARIABLE SOLO FUNCIONA DENTRO DE LA FUNCION A LA QUE PERTENECE
    # Para poder utilizar los valores de una funcion en otra funcion hay que declarar las variables como GLOBAL

    global S2_stars
    global S1_stars
    global i_s
    global cont_s
    global z
    global t

    S1_stars = [] #Lista en la cual se iran almacenando los valores aleatorios M
    S2_stars = [] #Segunda lista a comparar con la primera N
    i_s = [] # Para inicializar el bucle comparador de numeros
    cont_s = 0
  
    opc = False #Es como la opcion de True para hacer un bucle infinito hasta haber coincidencia
    
    system("cls")
    print(Fore.YELLOW + Style.BRIGHT + "RESULTADO ESTRELLAS" + Style.RESET_ALL)

    while opc != True:
        S1 = generador_primario_stars()
        S2 = generador_secundario_stars()
        S1_stars.append(S1)
        S2_stars.append(S2)

        # NOTA: En esta version elimino tal y como comente anteriormente la funcion format, ya que no me permitia usar la libreria colorama
        # print("Combinacion 1: \n--------------\n{}\n\nCombinacion 2: \n--------------\n {}\n".format(X, Y)) #A traves de .format es como he encontrado la manera mas vistosa de imprimir, aunque hay mas
        print("\t\t\t\t\t\t\t\t" + Back.RED + "Vuelta", cont_s, "\n" + Style.RESET_ALL)
        print(Fore.CYAN + Style.DIM + "Combinacion Estrellas A: ", Fore.GREEN + str(S1_stars) + Style.RESET_ALL)
        print("")
        print(Fore.CYAN + Style.DIM + "Combinacion Estrellas B: ", Fore.GREEN + str(S2_stars) + Style.RESET_ALL) 
        print("") #A traves de .format es como he encontrado la manera mas vistosa de imprimir, aunque hay mas
        sleep(0.2) #dejamos pasar un intervalo pequeño de tiempo entre cada combinacion

        cont_s += 1 #inicializamos el contador de combinaciones (ANTES DEL BUCLE FOR)
        for z in S1_stars: #Iniciamos el bucle, ira comparando ambas listas X e Y hasta que encuentre una coincidencia
            for t in S2_stars:
                if (z == t):
                        print(Fore.CYAN + Style.DIM + "Coincidencia de estrellas con: ", Style.RESET_ALL + Fore.GREEN + str(z) +"\n" + Style.RESET_ALL)
                        print(Fore.CYAN + Style.DIM + "Se han generado", Style.RESET_ALL + Fore.GREEN + str(cont_s) + Style.RESET_ALL + Fore.CYAN + Style.DIM + " combinaciones", "\n" + Style.RESET_ALL)
                        print(Fore.CYAN + Style.DIM + "La lista tiene una longitud de" , Style.RESET_ALL + Fore.GREEN + str(len(S1_stars+S2_stars)) + Style.RESET_ALL + Fore.CYAN + Style.DIM +  " elementos", "\n" + Style.RESET_ALL) #Recordar que len sirve para mostrar la longitud de una cadena, en este caso es el numero de elementos que han hecho falta para encontrar la coincidencia
                        opc = True #Hacemos la parada del ciclo y muestra de los resultados seguidos
                        sleep(4)
    Global_Result_nums_stars()

# -------------------------------------------------------------------------------------------------
# FUNCION PARA IMPRIMIR EL RESULTADO GLOBAL (NUMEROS Y ESTRELLAS) - POR COMPARACION (EUROMILLONES):
# -------------------------------------------------------------------------------------------------

def Global_Result_nums_stars():
    print(Fore.YELLOW + Style.BRIGHT + "\n\n----------------")
    print("Resultado Global:")
    print("----------------\n" + Style.RESET_ALL)
    print(Fore.CYAN + Style.DIM + "Coincidencia de numeros con: ", Fore.GREEN + str(i) + Style.RESET_ALL) 
    print(Fore.CYAN + Style.DIM + "Coincidencia de estrellas con: ", Fore.GREEN + str(z)+ Style.RESET_ALL)
    print(Fore.CYAN + Style.DIM + "Se han generado: " + Style.RESET_ALL, Fore.GREEN + str(cont) + Style.RESET_ALL, Fore.CYAN + Style.DIM + "combinaciones de numeros y " + Style.RESET_ALL, Fore.GREEN + str(cont_s) + Style.RESET_ALL, Fore.CYAN + Style.DIM + "de estrellas" )
    print(Fore.CYAN + Style.DIM + "La lista tiene una longitud de " , Fore.GREEN + str(len(X+Y)), Style.RESET_ALL + Fore.CYAN + Style.DIM + "numeros y de" , Style.RESET_ALL +Fore.GREEN + str(len(S1_stars+S2_stars)), Style.RESET_ALL + Fore.CYAN + Style.DIM + "estrellas")
    sleep(5)
    print("")
    final_ask = str(input(Fore.LIGHTWHITE_EX + Style.BRIGHT + "\n¿Deseas volver al menu principal? (s/n): "))
    if final_ask == "s":
        init_menu()
    elif final_ask == "n":
        exit()
    print("")
                 

# DATAFRAME MEDIANTE EL CUAL IMPRIMIREMOS EL RESULTADO POR COLUMNAS (EUROMILLON)
# ------------------------------------------------------------------------------
def miframe_euro():
    
    os.system ("cls") #Borramos la pantalla ya que sino mostraria los resultados y lo ultimo las columnas
    Lista_A_Euro = []
    Lista_B_Euro = []
    opc_euro = False
    cont_euro = 0

    while opc_euro != True:
        Var_1_Euro = generador_primario()
        Var_2_Euro = generador_secundario()
        Lista_A_Euro.append(Var_1_Euro)
        Lista_B_Euro.append(Var_2_Euro)
        sleep(0.2)
        print(Fore.YELLOW + Style.BRIGHT)
        df_euro = pd.DataFrame({"Columna A:":Lista_A_Euro, "Columna B:":Lista_B_Euro})
        system("cls")
        print(df_euro)

        cont_euro += 1
        for C1 in Lista_A_Euro:
            for C2 in Lista_B_Euro:
                if (C1 == C2):
                    print(Fore.CYAN + Style.DIM + "\nCoincidencia con:", Style.RESET_ALL + Fore.GREEN, C1)
                    print(Fore.CYAN + Style.DIM + "Se han generado", Style.RESET_ALL + Fore.GREEN, cont_euro, Style.RESET_ALL + Fore.CYAN + Style.DIM + "combinaciones")
                    print(Fore.CYAN + Style.DIM + "La lista tiene una longitud de", Style.RESET_ALL + Fore.GREEN, len(Lista_A_Euro+Lista_B_Euro), Style.RESET_ALL + Fore.CYAN + Style.DIM + "elementos")
                    print("")
                    opc_euro = True
                    sleep(0.5)
                    time_execution_end()

    
# FUNCION PARA CREAR ARCHIVO DE TEXTO Y AGREGAR LOS DATOS (EUROMILLON)
# --------------------------------------------------------------------
def text_file_euro(): # Funcion para agregar numeros generados a un archivo de texto.
    Work_func = funcion_de_trabajo_euro() # Pasamos la funcion de trabajo a una variable
    file1 = open("C:/Users/Espias/Desktop/aleatorios.txt", "a") # La terminacion en "a" es para que agregue los datos y NO los sobreescriba 
    str1 = repr(Work_func) # Pasamos la anterior funcion de trabajo a otra variable
    file1.write(str1) # Escribimos en el archivo
    file1.close() # Una vez escrito LO CERRAMOS


# Para mostrar el texto en la ventana de tkinter, usare un widget Text:
# Como se ve hay definiciones y clases (estudiarlo - comprenderlo) <-- extraido de stackoverflow
# Mediante la funcion mas abajo indicada "windows_out() consigo pasar los datos a la ventana de windows"

# FUNCION PARA CREAR LA VENTANA DE WINDOWS (TKINTER) (EUROMILLON)
# ---------------------------------------------------------------
def windows_out_euro():

    class StdOutRedirect:
        def __init__(self,  text: tk.Text) -> None:
            self._text = text

        def write(self,  out: str) -> None:
            self._text.insert(tk.END,  out)
        
        def flush(self): # Con esto evitamos la salida --> 'StdOutRedirect' object has no attribute 'flush'
                         # la cual no influye para el desarrollo del programa pero es molesta.
            pass


    class App(tk.Frame):
        def __init__(self, parent, *args, **kwargs):
            super().__init__(parent,  *args, **kwargs)
            self.stdout_text = tk.Text(
                self,  bg="white",  fg="#38B179",  font=("Helvetica", 15))
            self.stdout_text.pack(expand=True, fill=tk.BOTH)
            sys.stdout = StdOutRedirect(self.stdout_text)
        

    if __name__ == "__main__":
        ventana = tk.Tk() # Creamos la ventana
        ventana.title("Generador de Combinaciones") # Titulo de la ventana
        ventana.config(bg="White") # Color de fondo
        App(ventana).pack(expand=True, fill=tk.BOTH)
        funcion_de_trabajo_euro() # Llamamos a la funcion de trabajo para qe muestre los resultados por ventana
        ventana.update
        ventana.mainloop() # Para que la ventana permanezca abierta

init_menu() # FUNCION PARA EJECUTAR EL MENU PRINCIPAL DE EUROMILLONES Y A TRAVES DE EL TODAS LAS FUNCIONES