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
from os import times
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
import time
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as sm
from datetime import datetime
from collections import Counter as count
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
    catalog = {'artworks': None,
               'artists': None,
               'Nacimientos': None,
               'FechaAdquirida': None,
               'Medium': None,
               'Nationality': None}

    catalog['artworks'] = lt.newList('ARRAY_LIST')

    catalog['artists'] = lt.newList('ARRAY_LIST', cmpfunction=cmpConstituentID)

    catalog['Nacimientos'] = mp.newMap(maptype='CHAINING',
                                       loadfactor=4.0,
                                       comparefunction=compareMapBeginDate)

    catalog['FechaAdquirida'] = mp.newMap(maptype='CHAINING',
                                          loadfactor=4.0,
                                          comparefunction=compareMapDateAcquired)

    catalog['Medium'] = mp.newMap(200,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=compareMapMedium)

    catalog['Nationality'] = mp.newMap(200, maptype='CHAINING',
                                       loadfactor=4.0,
                                       comparefunction=compareMapNationality)

    return catalog

# Funciones para agregar informacion al catalogo


def addArtists(catalog, artist):
    lt.addLast(catalog['artists'], artist)
    nacimientos = catalog['Nacimientos']
    nacimiento = artist['BeginDate']
    if nacimiento == '':
        nacimiento = 0

    existNacimiento = mp.contains(nacimientos, nacimiento)

    if existNacimiento:
        entry = mp.get(nacimientos, nacimiento)
        nacimiento_final = me.getValue(entry)
        lt.addLast(nacimiento_final['artists'], artist)

    else:
        nacimiento_final = newNacimiento(nacimiento)
        lt.addLast(nacimiento_final['artists'], artist)
        mp.put(nacimientos, nacimiento, nacimiento_final)


def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    tecnicas = catalog['Medium']
    nacionalidades = catalog['Nationality']
    fechas_adquiridas = catalog['FechaAdquirida']

    if artwork['Medium'] != '':
        tecnica = artwork['Medium']
    else:
        tecnica = 'Unknown'
    existTecnica = mp.contains(tecnicas, tecnica)

    if existTecnica:
        entry = mp.get(tecnicas, tecnica)
        tecnica_final = me.getValue(entry)
        lt.addLast(tecnica_final['artworks'], artwork)

    else:
        tecnica_final = newTecnica(tecnica)
        lt.addLast(tecnica_final['artworks'], artwork)
        mp.put(tecnicas, tecnica, tecnica_final)

    artistas = str(artwork['ConstituentID'])
    artistas = artistas[1:len(artistas)-1]
    artistas = artistas.split(',')
    for artista in artistas:
        artista = artista.strip()
        posartista = lt.isPresent(catalog['artists'], artista)
        if posartista > 0:
            artista = lt.getElement(catalog['artists'], posartista)
            nacionalidad = artista['Nationality']
            if nacionalidad == "" or nacionalidad == "unknown" or nacionalidad == 'Unknown':
                nacionalidad = 'Nationality unknown'
        else:
            nacionalidad = 'Nationality unknown'

    existNacionalidad = mp.contains(nacionalidades, nacionalidad)

    if existNacionalidad:
        entry_2 = mp.get(nacionalidades, nacionalidad)
        nacionalidad_final = me.getValue(entry_2)
        anhadir = newFecha2(catalog, artwork)
        lt.addLast(nacionalidad_final['artworks'], anhadir)

    else:
        nacionalidad_final = newNationality(catalog, artwork)
        lt.addLast(nacionalidad_final['artworks'], artwork)
        mp.put(nacionalidades, nacionalidad, nacionalidad_final)

    fechaAdquirida = artwork['DateAcquired']
    if len(fechaAdquirida) != 10:
        fechaAdquirida = str(datetime.today())

    existFecha = mp.contains(fechas_adquiridas, fechaAdquirida)

    if existFecha:
        entry_3 = mp.get(fechas_adquiridas, fechaAdquirida)
        fecha_final = me.getValue(entry_3)
        anhadir = newFecha2(catalog, artwork)
        lt.addLast(fecha_final['artworks'], anhadir)

    else:
        fecha_final = newFecha(catalog, artwork)
        mp.put(fechas_adquiridas, fechaAdquirida, fecha_final)


def newNacimiento(nacimiento):
    entry = {'artists': None}
    entry['artists'] = lt.newList('ARRAY_LIST')
    return entry


def newFecha(catalog, artwork):
    entry = {'artworks': None}
    entry['artworks'] = lt.newList('ARRAY_LIST')
    artworkList = {'Title': artwork['Title'], 'artists': None, 'DateAcquired': artwork['DateAcquired'],
                   'Medium': artwork['Medium'], 'Dimensions': artwork['Dimensions'], 'CreditLine': artwork['CreditLine'],
                   'Date': artwork['Date']}
    artworkList['artists'] = lt.newList('ARRAY_LIST')
    artistas = str(artwork['ConstituentID'])
    artistas = artistas[1:len(artistas)-1]
    artistas = artistas.split(',')
    for artista in artistas:
        artista = artista.strip()
        posartista = lt.isPresent(catalog['artists'], artista)
        if posartista > 0:
            artista = lt.getElement(catalog['artists'], posartista)
        else:
            artista = {'ConsitutentID': artista, 'DisplayName': 'Unknown'}
        lt.addLast(artworkList['artists'], artista)
    lt.addLast(entry['artworks'], artworkList)
    return entry


def newFecha2(catalog, artwork):
    artworkList = {'Title': artwork['Title'], 'artists': None, 'DateAcquired': artwork['DateAcquired'],
                   'Medium': artwork['Medium'], 'Dimensions': artwork['Dimensions'], 'CreditLine': artwork['CreditLine'],
                   'Date': artwork['Date']}
    artworkList['artists'] = lt.newList('ARRAY_LIST')
    artistas = str(artwork['ConstituentID'])
    artistas = artistas[1:len(artistas)-1]
    artistas = artistas.split(',')
    for artista in artistas:
        artista = artista.strip()
        posartista = lt.isPresent(catalog['artists'], artista)
        if posartista > 0:
            artista = lt.getElement(catalog['artists'], posartista)
        else:
            artista = {'ConsitutentID': artista, 'DisplayName': 'Unknown'}
        lt.addLast(artworkList['artists'], artista)
    return artworkList


def newTecnica(tecnica):
    entry = {'Tecnica': None, 'artworks': None}
    entry['Tecnica'] = tecnica
    entry['artworks'] = lt.newList('ARRAY_LIST')
    return entry


def newNationality(catalog, artwork):
    entry = {'artworks': None}
    entry['artworks'] = lt.newList('ARRAY_LIST')
    artworkList = {'Title': artwork['Title'], 'artists': None,
                   'Medium': artwork['Medium'], 'Dimensions': artwork['Dimensions'],
                   'Date': artwork['Date']}
    artworkList['artists'] = lt.newList('ARRAY_LIST')
    artistas = str(artwork['ConstituentID'])
    artistas = artistas[1:len(artistas)-1]
    artistas = artistas.split(',')
    for artista in artistas:
        artista = artista.strip()
        posartista = lt.isPresent(catalog['artists'], artista)
        if posartista > 0:
            artista = lt.getElement(catalog['artists'], posartista)
        else:
            artista = {'ConsitutentID': artista, 'DisplayName': 'Unknown'}
        lt.addLast(artworkList['artists'], artista)
    lt.addLast(entry['artworks'], artworkList)
    return entry


def newnationality2(catalog, artwork):
    artworkList = {'Title': artwork['Title'], 'artists': None,
                   'Medium': artwork['Medium'], 'Dimensions': artwork['Dimensions'],
                   'Date': artwork['Date']}
    artworkList['artists'] = lt.newList('ARRAY_LIST')
    artistas = str(artwork['ConstituentID'])
    artistas = artistas[1:len(artistas)-1]
    artistas = artistas.split(',')
    for artista in artistas:
        artista = artista.strip()
        posartista = lt.isPresent(catalog['artists'], artista)
        if posartista > 0:
            artista = lt.getElement(catalog['artists'], posartista)
        else:
            artista = {'ConsitutentID': artista, 'DisplayName': 'Unknown'}
        lt.addLast(artworkList['artists'], artista)
    return artworkList


# Funciones para creacion de datos

# Funciones de consulta

def rangoArtistas(catalog, anho_inicio, anho_final):
    nacimientos = catalog['Nacimientos']
    lista_anhos = mp.keySet(nacimientos)
    sorted_list = sm.sort(lista_anhos, cmpBeginDate)
    final_lista = int(lt.size(sorted_list))
    i = 1
    while i <= final_lista:
        fecha = lt.getElement(sorted_list, i)
        if int(fecha) >= int(anho_inicio):
            pos_inicial = i
            i += final_lista
        i += 1

    j = 1
    while j <= final_lista:
        fecha = lt.getElement(sorted_list, j)
        if int(fecha) <= int(anho_final):
            pos_final = j
        j += 1

    sorted_list_2 = lt.subList(
        sorted_list, pos_inicial, pos_final-pos_inicial+1)

    cantidad = 0

    lista_final = {'artistas': None}
    lista_final['artistas'] = lt.newList('ARRAY_LIST')

    for fecha in lt.iterator(sorted_list_2):
        artistas = mp.get(nacimientos, fecha)
        lista = artistas['value']
        artista = lista['artists']
        size = lt.size(lista['artists'])
        for artista_1 in lt.iterator(artista):
            lt.addLast(lista_final['artistas'], artista_1)

        cantidad += size

    return lista_final['artistas'], cantidad


def rangoAcquired(catalog, fecha_inicial, fecha_final):
    FechasAdquiridas = catalog['FechaAdquirida']
    lista = mp.keySet(FechasAdquiridas)
    sortedList = sm.sort(lista, cmpArtworkByDateAcquired)
    final_lista = int(lt.size(sortedList))

    i = 1
    while i <= final_lista:
        fecha_adquirda = lt.getElement(sortedList, i)
        anho_adquirido = float(fecha_adquirda[0:4])
        mes_adquirido = float(fecha_adquirda[5:7])
        dia_adquirido = float(fecha_adquirda[8:10])
        anho_inicial = float(fecha_inicial[0:4])
        mes_inicial = float(fecha_inicial[5:7])
        dia_inicial = float(fecha_inicial[8:10])
        if anho_adquirido > anho_inicial:
            pos_inicial = i
            i += final_lista
        elif anho_adquirido == anho_inicial:
            if mes_adquirido > mes_inicial:
                pos_inicial = i
                i += final_lista
            elif mes_adquirido == mes_inicial:
                if dia_adquirido >= dia_inicial:
                    pos_inicial = i
                    i += final_lista
        i += 1

    j = 1
    while j <= final_lista:
        fecha_adquirda = lt.getElement(sortedList, j)
        anho_adquirido = float(fecha_adquirda[0:4])
        mes_adquirido = float(fecha_adquirda[5:7])
        dia_adquirido = float(fecha_adquirda[8:10])
        anho_final = float(fecha_final[0:4])
        mes_final = float(fecha_final[5:7])
        dia_final = float(fecha_final[8:10])
        if anho_adquirido < anho_final:
            pos_final = j
        elif anho_adquirido == anho_final:
            if mes_adquirido < mes_final:
                pos_final = j
            elif mes_adquirido == mes_final:
                if dia_adquirido <= dia_final:
                    pos_final = j
        j += 1

    sorted_list2 = lt.subList(sortedList, pos_inicial, pos_final-pos_inicial+1)

    lista_final = {'artworks': None}
    lista_final['artworks'] = lt.newList('ARRAY_LIST')

    contadorPruchase = 0

    for fecha in lt.iterator(sorted_list2):
        obras = mp.get(FechasAdquiridas, fecha)
        lista = obras['value']
        obra = lista['artworks']
        for obra_1 in lt.iterator(obra):
            lt.addLast(lista_final['artworks'], obra_1)
            tipoCompra = obra_1['CreditLine']
            if "Purchase" in tipoCompra:
                contadorPruchase += 1
            elif 'purchase' in tipoCompra:
                contadorPruchase += 1

    return lista_final, contadorPruchase


def obrasPorNacionalidad(catalog):
    nacionalidades = catalog['Nationality']
    lista = mp.keySet(nacionalidades)
    orden = {'Nacionalidades': None}
    orden['Nacionalidades'] = lt.newList('ARRAY_LIST')

    for nacionalidad in lt.iterator(lista):
        size = lt.size(
            ((mp.get(nacionalidades, nacionalidad))['value'])['artworks'])
        lista = mp.get(nacionalidades, nacionalidad)['value']['artworks']
        lt.deleteElement(lista, 2)
        nacionalidadAdd = {'Nacionalidad': nacionalidad,
                           'contador': size-1, 'artworks': lista}

        lt.addLast(orden['Nacionalidades'], nacionalidadAdd)

    sortedList = sm.sort(orden['Nacionalidades'], cmpObrasNacionalidad)

    return sortedList


def reqlab(catalog, numObras, medio):
    tecnicas = catalog['Medium']
    entry = mp.get(tecnicas, medio)
    tecnica_final = me.getValue(entry)
    sublist = tecnica_final['artworks'].copy()
    sortedList = sm.sort(sublist, compareListDate)
    listaCorta = lt.subList(sortedList, 1, numObras)
    return listaCorta


def reqlab2(catalog, nacionalidad):
    nacionalidades = catalog['Nationality']
    entry = mp.get(nacionalidades, nacionalidad)
    nacionalidad_final = me.getValue(entry)
    sublist = nacionalidad_final['artworks'].copy()
    tamanho = lt.size(sublist)
    return tamanho


def req3reto(catalog, artista):
    mediosMap = catalog['Medium']
    tecnicas = {'tecnicas': None, 'lista': None}
    tecnicas['tecnicas'] = lt.newList('ARRAY_LIST')
    tecnicas['lista'] = lt.newList('ARRAY_LIST')
    mapTecnicas = mp.newMap()
    numObras = 0

    for each in catalog['artists']['elements']:
        name = each['DisplayName']
        if name == artista:
            artistID = '['+each['ConstituentID']+']'

    for each in catalog['artworks']['elements']:
        if artistID == each['ConstituentID']:
            numObras += 1
            lt.addLast(tecnicas['tecnicas'], each['Medium'])
            mp.put(mapTecnicas, each['Medium'], [
                   each['Title'], each['Date'], each['Dimensions']])
            keys = list(tecnicas.values())
            c = count(keys[0]['elements'])
            tecMasUsada = c.most_common(1)

    entry = mp.get(mediosMap, tecMasUsada[0][0])
    tecnica_final = me.getValue(entry)
    sublist = tecnica_final['artworks'].copy()
    sortedList = sm.sort(sublist, compareListDate)

    for each in sortedList['elements']:
        if each['ConstituentID'] == artistID:
            lt.addLast(tecnicas['lista'], [
                       each['Title'], each['Date'], each['Medium'], each['Dimensions']])
    numTecnicas = mp.size(mapTecnicas)

    return numObras, numTecnicas, tecMasUsada, tecnicas['lista']['elements']

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpConstituentID(id1, lista):
    if id1 in str(lista['ConstituentID']):
        return 0
    return -1


def cmpBeginDate(beginDate1, begindate2):
    if beginDate1 < begindate2:
        return 1
    else:
        return 0


def compareMapBeginDate(keyNacimiento, nacimiento):
    nacentry = me.getKey(nacimiento)
    if keyNacimiento == nacentry:
        return 0
    else:
        return -1


def compareMapDateAcquired(keyDateAcquired, dateAcquired):
    datentry = me.getKey(dateAcquired)
    if datentry == keyDateAcquired:
        return 0
    else:
        return -1


def compareMapNationality(keyNationality, nationality):
    natentry = me.getKey(nationality)
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


def cmpArtworkByDateAcquired(fecha_artwork1, fecha_artwork2):
    anho_artwork1 = float(fecha_artwork1[:4])
    mes_artwork1 = float(fecha_artwork1[5:7])
    dia_artwork1 = float(fecha_artwork1[8:10])
    anho_artwork2 = float(fecha_artwork2[:4])
    mes_artwork2 = float(fecha_artwork2[5:7])
    dia_artwork2 = float(fecha_artwork2[8:10])
    if fecha_artwork1 == fecha_artwork2:
        return 0
    elif anho_artwork1 < anho_artwork2:
        return 1
    elif anho_artwork1 > anho_artwork2:
        return 0
    elif anho_artwork1 == anho_artwork2:
        if mes_artwork1 < mes_artwork2:
            return 1
        elif mes_artwork1 > mes_artwork2:
            return 0
        elif dia_artwork1 == mes_artwork2:
            if dia_artwork1 < dia_artwork2:
                return 1
            elif dia_artwork1 > dia_artwork2:
                return 0


def compareListDate(artwork1, artwork2):
    fechaObra1 = artwork1['Date']
    fechaObra2 = artwork2['Date']
    if fechaObra1 < fechaObra2:
        return 1
    else:
        return 0


def cmpObrasNacionalidad(nacionalidad1, nacionalidad2):
    conteo1 = nacionalidad1['contador']
    conteo2 = nacionalidad2['contador']
    if conteo1 > conteo2:
        return 1
    else:
        return 0


# Funciones de ordenamiento
