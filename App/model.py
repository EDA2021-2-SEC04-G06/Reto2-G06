"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


'''from typing_extensions import TypeVarTuple'''
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as sm
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
    catalog = {'artworks': None,
               'Medium': None,
               'Date': None}

    catalog['artworks'] = lt.newList('ARRAY_LIST')

    catalog['Medium'] = mp.newMap(200,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=compareMapMedium)

    return catalog

# Funciones para agregar informacion al catalogo


def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    tecnicas = catalog['Medium']
    if artwork['Medium'] != '':
        tecnica = artwork['Medium']
    else:
        tecnica = 'Unknown'
    existTecnica = mp.contains(tecnicas, tecnica)

    if existTecnica:
        entry = mp.get(tecnicas, tecnica)
        tecnica_final = me.getValue(entry)
        lt.addLast(tecnica_final['artworks'],artwork)

    else:
        tecnica_final = newTecnica(tecnica, artwork)
        lt.addLast(tecnica_final['artworks'],artwork)
        mp.put(tecnicas, tecnica, tecnica_final)


def newTecnica(tecnica, artwork):
    entry = {'Tecnica': None, 'artworks': None}
    entry['Tecnica'] = tecnica
    entry['artworks'] = lt.newList('ARRAY_LIST')
    return entry


# Funciones para creacion de datos

# Funciones de consulta

def reqlab(catalog,numObras,medio):
    tecnicas=catalog['Medium']
    entry = mp.get(tecnicas, medio)
    tecnica_final=me.getValue(entry)
    sublist=tecnica_final['artworks'].copy()
    sortedList=sm.sort(sublist,compareListDate)
    listaCorta=lt.subList(sortedList,1,numObras)
    return listaCorta


# Funciones utilizadas para comparar elementos dentro de una lista


def compareMapMedium(keyMedium, medium):
    medentry = me.getKey(medium)
    if (keyMedium == medentry):
        return 0
    elif (keyMedium > medentry):
        return 1
    else:
        return -1


def compareListDate(artwork1, artwork2):
    fechaObra1=artwork1['Date']
    fechaObra2=artwork2['Date']
    if fechaObra1<fechaObra2:
        return 1
    else:
        return 0


# Funciones de ordenamiento
