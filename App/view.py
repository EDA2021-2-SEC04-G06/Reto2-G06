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
    print("5- Clasificar obras por la nacionalidad de sus creadores")
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


def printprimeros3artistasyobras(lista, size):
    if size >= 3:
        print("\nLas primeras 3 Obras son: ")
        i = 1
        while i <= 3:
            obra = lt.getElement(lista, i)
            titulo = obra['Title']
            fecha = obra['Date']
            medio = obra['Medium']
            dimensiones = obra['Dimensions']
            cadenaArtista = ""
            for artistas in lt.iterator(obra['artists']):
                artista = artistas['DisplayName']
                if cadenaArtista == "":
                    cadenaArtista += artista
                else:
                    cadenaArtista += ", "+artista
            if fecha == "":
                fecha = "Unknown"
            if medio == "":
                medio = "Unknown"
            if dimensiones == "":
                dimensiones = 'Unknown'
            if cadenaArtista == "":
                cadenaArtista = "Unknown"

            print(str(i)+". " + "Titulo: " + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
                  + fecha + ", Medio: " + medio
                  + ", Dimensiones: " + dimensiones)
            i += 1
        print('...')

    elif size >= 1:
        if size == 1:
            print("\nLa primera obra es: ")
        if size == 2:
            print("\nLas primeras 2 Artistas son: ")
        i = 1
        while i <= size:
            obra = lt.getElement(lista, i)
            titulo = obra['Title']
            fecha = obra['Date']
            medio = obra['Medium']
            dimensiones = obra['Dimensions']
            cadenaArtista = ""
            for artistas in lt.iterator(obra['artists']):
                artista = artistas['DisplayName']
                if cadenaArtista == "":
                    cadenaArtista += artista
                else:
                    cadenaArtista += ", "+artista

            if fecha == "":
                fecha = "Unknown"
            if medio == "":
                medio = "Unknown"
            if dimensiones == "":
                dimensiones = 'Unknown'
            if cadenaArtista == "":
                cadenaArtista = "Unknown"

            print(str(i)+". " + "Titulo:" + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
                  + fecha + ", Medio: " + medio
                  + ", Dimensiones: " + dimensiones)
            i += 1
        print('...')

    else:
        return None


def printUltimos3ArtistasyObras(lista, size):
    if size >= 3:
        print("Los últimos 3 Artistas son: ")
        i = size-2
        while i <= size:
            obra = lt.getElement(lista, i)
            titulo = obra['Title']
            fecha = obra['Date']
            medio = obra['Medium']
            dimensiones = obra['Dimensions']
            cadenaArtista = ""
            for artistas in lt.iterator(obra['artists']):
                artista = artistas['DisplayName']
                if cadenaArtista == "":
                    cadenaArtista += artista
                else:
                    cadenaArtista += ", "+artista

            if fecha == "":
                fecha = "Unknown"
            if medio == "":
                medio = "Unknown"
            if dimensiones == "":
                dimensiones = 'Unknown'
            if cadenaArtista == "":
                cadenaArtista = "Unknown"

            print(str(i)+". " + "Titulo:" + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
                  + fecha + ", Medio: " + medio
                  + ", Dimensiones: " + dimensiones)
            i += 1
    elif size >= 1:
        if size == 1:
            print("La última Obra es: ")
        if size == 2:
            print("Los últimos 2 Artistas son: ")
        i = 1
        while i <= size:
            obra = lt.getElement(lista, i)
            titulo = obra['Title']
            fecha = obra['Date']
            medio = obra['Medium']
            dimensiones = obra['Dimensions']
            cadenaArtista = ""
            for artistas in lt.iterator(obra['artists']):
                artista = artistas['DisplayName']
                if cadenaArtista == "":
                    cadenaArtista += artista
                else:
                    cadenaArtista += ", "+artista

            if fecha == "":
                fecha = "Unknown"
            if medio == "":
                medio = "Unknown"
            if dimensiones == "":
                dimensiones = 'Unknown'
            if cadenaArtista == "":
                cadenaArtista = "Unknown"

            print(str(i)+". " + "Titulo:" + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
                  + fecha + ", Medio: " + medio
                  + ", Dimensiones: " + dimensiones)
            i += 1
    else:
        None


def printTOP10(lista):
    size = lt.size(lista)
    if size > 10:
        print("\nLos primeros ", str(10),
              " paises ordenados por su número de obras son: ")
        i = 1
        while i <= 10:
            nacionalidades = lt.getElement(lista, i)
            nacionalidad = nacionalidades['Nacionalidad']
            conteo = nacionalidades['contador']
            print(str(i)+"." + nacionalidad + ': ' + str(conteo))
            i += 1


def printPrimeras3ObrasNacionalidad(lista):
    primeraNacionalidad = lt.getElement(lista, 1)
    print('\nEn el primer lugar se encuentra la nacionalidad '+primeraNacionalidad['Nacionalidad']+' con un total de ' +
          str(primeraNacionalidad['contador'])+' obras.')
    i = 1
    while i <= 3:
        obra = lt.getElement(primeraNacionalidad['artworks'], i)
        titulo = obra['Title']
        fecha = obra['Date']
        medio = obra['Medium']
        dimensiones = obra['Dimensions']
        cadenaArtista = ''
        for artistas in lt.iterator(obra['artists']):
            artista = artistas['DisplayName']
            if cadenaArtista == "":
                cadenaArtista += artista
            else:
                cadenaArtista += ", "+artista
        print(str(i)+'. '+"Titulo: " + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
              + fecha + ", Medio: " + medio
              + ", Dimensiones: " + dimensiones)
        i += 1
    print('...')


def printUltimas3obrasNacionalidad(lista):
    primeraNacionalidad = lt.getElement(lista, 1)
    size = lt.size(primeraNacionalidad['artworks'])
    i = size-2
    while i <= size:
        obra = lt.getElement(primeraNacionalidad['artworks'], i)
        titulo = obra['Title']
        fecha = obra['Date']
        medio = obra['Medium']
        dimensiones = obra['Dimensions']
        cadenaArtista = ''
        for artistas in lt.iterator(obra['artists']):
            artista = artistas['DisplayName']
            if cadenaArtista == "":
                cadenaArtista += artista
            else:
                cadenaArtista += ", "+artista
        print(str(i)+'. '+"Titulo: " + titulo + ", Artista(s): " + cadenaArtista + ", Fecha: "
              + fecha + ", Medio: " + medio
              + ", Dimensiones: " + dimensiones)
        i += 1


catalog = None


def printResultadoLab(resultado):
    size = lt.size(resultado)
    i = 1
    while i <= size:
        obra = lt.getElement(resultado, i)
        titulo = obra['Title']
        fecha = obra['Date']
        print(str(i)+". Titulo: "+titulo+", Fecha: "+fecha)
        i += 1


def printprimeros3(resultado):
    i = 0
    while i <= 2:
        print('\n'+str(resultado[i]))
        i += 1


def printultimos3(resultado):
    i = 0
    n = 0
    while i <= 2:
        print('\n'+str(resultado[n-1]))
        i += 1
        n -= 1


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
        i=0
        

    elif int(inputs[0]) == 2:
        anho_inicial = input("\nIngrese el año inicial: ")
        anho_final = input("Ingrese el año final: ")
        resultado = controller.rangoArtistas(catalog, anho_inicial, anho_final)
        print('\nHay '+str(resultado[1])+' artistas nacidos entre ' +
              str(anho_inicial)+" y "+str(anho_final))
        printPrimeros3Artistas(resultado[0], resultado[1])
        ultimos3Artistas(resultado[0], resultado[1])

    elif int(inputs[0]) == 3:
        anho_inicial = input('\nIngrese la Fecha Inicial (AAAA-MM-DD): ')
        anho_final = input('Ingrese la Fecha Final (AAAA-MM-DD): ')
        resultado = controller.rangoAcquired(catalog, anho_inicial, anho_final)
        size = lt.size(resultado[0]['artworks'])
        print('\nHay '+str(size)+' obras únicas entre ' +
              anho_inicial + ' y '+anho_final)
        print('Obras adquiridas por Purchase: ' + str(resultado[1]))
        printprimeros3artistasyobras(resultado[0]['artworks'], size)
        printUltimos3ArtistasyObras(resultado[0]['artworks'], size)

    elif int(inputs[0]) == 4:
        artista = input('Ingrese el nombre del artista: ')
        resultado = controller.req3reto(catalog, artista)
        print('\nTotal de obras: ' + str(resultado[0]))
        print('Total de tecnicas: ' + str(resultado[1]))
        print('Tecnica mas usada: ' + str(resultado[2]))
        print('\nLas primeras 3 obras son: ')
        printprimeros3(resultado[3])
        print('\nLas ultimas 3 obras son: ')
        printultimos3(resultado[3])

    elif int(inputs[0]) == 5:
        resultado = controller.obrasPorNacionalidad(catalog,i)
        printTOP10(resultado)
        printPrimeras3ObrasNacionalidad(resultado)
        printUltimas3obrasNacionalidad(resultado)
        i+=1

    elif int(inputs[0]) == 6:
        depto = input('Ingrese el departamento: ')
        resultado = controller.req5reto(catalog, depto)
        print('\nEl total de obras a transportar: '+str(resultado[0]))
        print('\nEl estimado del precio de servicio (USD) es de: ' +
              str(resultado[1]))
        print('\nEl peso estimado de las obras es: '+str(resultado[2]))
        print('\nLas 5 obras mas antiguas a transportar son: ' +
              str(resultado[3]))
        print('\nLas 5 obras mas costosas son: '+str(resultado[4]))

    else:
        sys.exit(0)
sys.exit(0)
