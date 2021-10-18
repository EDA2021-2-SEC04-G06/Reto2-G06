"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def initCatalog():
    return controller.initCatalog()


def loadData(catalog):
    controller.loadData(catalog)


def printMenu():
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar Cronologicamente los artistas en un rango")
    print("3- Listar Cronologicamente las adquisiciones")
    print("4- Clasificar obra de un artista por tecnica")
    print("5- Clasificar obras por la nacionalidad de sus crreadores")
    print("6- Transportar obras de un departamento")


def printPrimeros3Artistas(lista, size):
    if size >= 3:
        print("\nLos primeros 3 Artistas son: ")
        i = 1
        while i <= 3:
            artistas = lt.getElement(lista, i)
            nombre = artistas['DisplayName']
            anho_nacimiento = artistas['BeginDate']
            anho_fallecido = artistas['EndDate']
            nacionalidad = artistas['Nationality']
            genero = artistas['Gender']
            if anho_fallecido == "0":
                anho_fallecido = "Sigue vivo o se desconoce su muerte"
            print(str(i)+". " + "Artista: " + nombre + ", Año de Nacimiento: "
                  + anho_nacimiento + ", Año de Fallecimiento: " + anho_fallecido
                  + ", Nacionalidad: " + nacionalidad + ", Genero: " + genero)
            i += 1
        print("...")

    elif size >= 1:
        if size == 1:
            print("\nEl primer Artista es: ")
        if size == 2:
            print("\nLos primeros 2 Artistas son: ")
        i = 1
        while i <= size:
            artistas = lt.getElement(lista, i)
            nombre = artistas['DisplayName']
            anho_nacimiento = artistas['BeginDate']
            anho_fallecido = artistas['EndDate']
            nacionalidad = artistas['Nationality']
            genero = artistas['Gender']
            if anho_fallecido == "0":
                anho_fallecido = "Sigue vivo o se desconoce su muerte"
            print(str(i)+". " + "Artista: " + nombre + ", Año de Nacimiento: "
                  + anho_nacimiento + ", Año de Fallecimiento: " + anho_fallecido
                  + ", Nacionalidad: " + nacionalidad + ", Genero: " + genero)
        print("...")

    else:
        return None

def ultimos3Artistas(lista, size):
    if size >= 3:
        print("Los últimos 3 Artistas son: ")
        i = size-2
        while i <= size:
            artistas = lt.getElement(lista, i)
            nombre = artistas['DisplayName']
            anho_nacimiento = artistas['BeginDate']
            anho_fallecido = artistas['EndDate']
            nacionalidad = artistas['Nationality']
            genero = artistas['Gender']
            if anho_fallecido == "0":
                anho_fallecido = "Sigue vivo o se desconoce su muerte"
            print(str(i)+". " + "Artista: " + nombre + ", Año de Nacimiento: "
                  + anho_nacimiento + ", Año de Fallecimiento: " + anho_fallecido
                  + ", Nacionalidad: " + nacionalidad + ", Genero: " + genero)
            i += 1

    elif size >= 1:
        if size == 1:
            print("El último Artista es: ")
        if size == 2:
            print("Los últimos 2 Artistas son: ")
        i = 1
        while i <= size:
            artistas = lt.getElement(lista, i)
            nombre = artistas['DisplayName']
            anho_nacimiento = artistas['BeginDate']
            anho_fallecido = artistas['EndDate']
            nacionalidad = artistas['Nationality']
            genero = artistas['Gender']
            if anho_fallecido == "0":
                anho_fallecido = "Sigue vivo o se desconoce su muerte"
            print(str(i)+". " + "Artista: " + nombre + ", Año de Nacimiento: "
                  + anho_nacimiento + ", Año de Fallecimiento: " + anho_fallecido
                  + ", Nacionalidad: " + nacionalidad + ", Genero: " + genero)
    else:
        return None

def printResultadoLab(resultado):
    size=lt.size(resultado)
    i=1
    while i<=size:
        obra=lt.getElement(resultado,i)
        titulo=obra['Title']
        fecha=obra['Date']
        print(str(i)+". Titulo: "+titulo+", Fecha: "+fecha)
        i+=1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)

    elif int(inputs[0]) == 2:
        anho_inicial =input("\nIngrese el año inicial: ")
        anho_final = input("Ingrese el año final: ")
        resultado = controller.rangoArtistas(catalog,anho_inicial,anho_final)
        print('\nHay '+str(resultado[1])+' artistas nacidos entre '+str(anho_inicial)+" y "+str(anho_final))
        printPrimeros3Artistas(resultado[0], resultado[1])
        ultimos3Artistas(resultado[0],resultado[1])
        


    elif int(inputs[0]) == 3:
        nacionalidad=input('Ingrese una nacionalidad: ')
        resultado=controller.req2lab(catalog, nacionalidad)
        print(resultado)

    elif int(inputs[0]) == 4:
        numObras = int(input('\nNumero de obras mas antiguas a buscar: '))
        medio = input('Medio especifico: ')
        resultado = controller.reqlab(catalog,numObras,medio)
        print("\nCantidad de Obras para "+ str(medio) + ": "+str(numObras))
        printResultadoLab(resultado)
        pass

    else:
        sys.exit(0)
sys.exit(0)
