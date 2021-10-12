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
                'artists':None,
               'Medium': None,
               'Nationality': None}

    catalog['artworks'] = lt.newList('ARRAY_LIST')

    catalog['artists'] =lt.newList('ARRAY_LIST',cmpfunction=cmpConstituentID)

    catalog['Medium'] = mp.newMap(200,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=compareMapMedium)

    catalog['Nationality'] = mp.newMap(200,maptype='CHAINING', 
                                  loadfactor=4.0,
                                   comparefunction=compareMapNationality)

    return catalog

# Funciones para agregar informacion al catalogo

def addArtists(catalog, artist):
    lt.addLast(catalog['artists'],artist)


def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    tecnicas = catalog['Medium']
    nacionalidades = catalog['Nationality']
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
        tecnica_final = newTecnica(tecnica)
        lt.addLast(tecnica_final['artworks'],artwork)
        mp.put(tecnicas, tecnica, tecnica_final)


    artistas = str(artwork['ConstituentID'])
    artistas = artistas[1:len(artistas)-1]
    artistas = artistas.split(',')
    for artista in artistas:
        artista=artista.strip()
        posartista = lt.isPresent(catalog['artists'], artista)
        if posartista > 0:
            artista = lt.getElement(catalog['artists'], posartista)
            nacionalidad=artista['Nationality']
            if nacionalidad == "":
                nacionalidad = 'Nationality unknown'
        else:
            nacionalidad = 'Nationality unknown'

    existNacionalidad=mp.contains(nacionalidades, nacionalidad)

    if existNacionalidad:
        entry_2=mp.get(nacionalidades, nacionalidad)
        nacionalidad_final=me.getValue(entry_2)
        lt.addLast(nacionalidad_final['artworks'],artwork)

    else:
        nacionalidad_final = newNationality(nacionalidad)
        lt.addLast(nacionalidad_final['artworks'],artwork)
        mp.put(nacionalidades, nacionalidad, nacionalidad_final)

def newTecnica(tecnica):
    entry = {'Tecnica': None, 'artworks': None}
    entry['Tecnica'] = tecnica
    entry['artworks'] = lt.newList('ARRAY_LIST')
    return entry

def newNationality(nacionalidad):
    entry={'Nationality':None, 'artworks': None}
    entry['Nationality']=nacionalidad
    entry['artworks']=lt.newList('ARRAY_LIST')
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

def reqlab2(catalog,nacionalidad):
    nacionalidades=catalog['Nationality']
    entry=mp.get(nacionalidades,nacionalidad)
    nacionalidad_final=me.getValue(entry)
    sublist=nacionalidad_final['artworks'].copy()
    tamanho=lt.size(sublist)
    return tamanho

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpConstituentID(id1, lista):
    if id1 in str(lista['ConstituentID']):
        return 0
    return -1

def compareMapNationality(keyNationality, nationality):
    natentry=me.getKey(nationality)
    if keyNationality == natentry:
        return 0
    elif keyNationality > natentry:
        return 1
    else:
        return -1

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
