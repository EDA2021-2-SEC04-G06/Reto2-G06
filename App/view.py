﻿"""
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
    print("2- Numero de obras mas antiguas para un medio especifico")
    print("3- Obras por Nacionalidad especifica")

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
        print(catalog['Nationality'])

    elif int(inputs[0]) == 2:
        numObras = int(input('\nNumero de obras mas antiguas a buscar: '))
        medio = input('Medio especifico: ')
        resultado = controller.reqlab(catalog,numObras,medio)
        print("\nCantidad de Obras para "+ str(medio) + ": "+str(numObras))
        printResultadoLab(resultado)

    elif int(inputs[0]) == 3:
        nacionalidad=input('Ingrese una nacionalidad: ')
        resultado=controller.req2lab(catalog, nacionalidad)
        print(resultado)
        pass

    else:
        sys.exit(0)
sys.exit(0)
