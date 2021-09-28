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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'artworks': None,
               'Medium': None,
               'Date':None}
        
    catalog['artworks']=lt.newList('ARRAY_LIST')

    catalog['Medium'] = mp.newMap(100,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapMedium)

    return catalog

# Funciones para agregar informacion al catalogo

def addArtworks(catalog,artwork):
    lt.addLast(catalog['artworks'], artwork)
    tecnicas=catalog['Medium']
    if artwork['Medium'] != '':
        tecnica=artwork['Medium']
    else:
        tecnica='Unknown'
    existTecnica=mp.contains(tecnicas,tecnica)

    if existTecnica:
        entry= mp.get(tecnicas,tecnica)
        tecnica_final=me.getValue(entry)
        anhos=tecnica_final['Dates']
        if artwork['Date']!='':
            anho=artwork['Date']
        else:
            anho='Unknown'
        existAnho=mp.contains(anhos,anho)

        if existAnho:
            entry_2=mp.get(anhos,anho)
            anho_final=me.getValue(entry_2)
            lt.addLast(anho_final['artworks'],artwork)
        else:
            anho_final=newAnho(anho)
            lt.addLast(anho_final['artworks'],artwork)
            
    else:
        tecnica_final=newTecnica(tecnica,artwork)
        mp.put(tecnicas,tecnica,tecnica_final)
        




def newTecnica(tecnica,artwork):
    entry={'Tecnica':None,'Dates':None}
    entry['Tecnica']=tecnica
    entry['Dates'] = mp.newMap(100,maptype='PROBING',
                                    loadfactor=2.0,
                                    comparefunction=compareMapDate)
    anhos=entry['Dates']
    if artwork['Date']!='':
        anho=artwork['Date']
    else:
        anho='Unknown'
    anho_final=newAnho(anho)
    lt.addLast(anho_final['artworks'],artwork)
    mp.put(anhos,anho,anho_final)
    return entry

def newAnho(anho):
    entry={'Date':'','artworks':None}
    entry['Date']=anho
    entry['artworks']=lt.newList('ARRAY_LIST')
    return entry

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareMapMedium(keyMedium, medium):
    medentry = me.getKey(medium)
    if (keyMedium == medentry):
        return 0
    elif (keyMedium > medentry):
        return 1
    else:
        return -1


def compareMapDate(keyDate, date):
    dateEntry=me.getValue(date)
    if keyDate==dateEntry:
        return 0
    elif int(keyDate) > int(dateEntry):
        return 1
    else:
        return 0


# Funciones de ordenamiento
