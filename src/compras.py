import csv
import datetime
from typing import NamedTuple
from parsers import *
from collections import defaultdict

Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)]
                    )

def lee_compras(fichero):
    res = []

    with open(fichero, "r", encoding="utf-8") as f:
        lector= csv.reader(f)
        next(lector)
        
        for dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra in lector:
            fecha_llegada = parsea_fecha(fecha_llegada)
            fecha_salida = parsea_fecha(fecha_salida)
            res.append( Compra(dni, supermercado, provincia, fecha_llegada, fecha_salida, float(total_compra)) )
    
    return res


def compra_maxima_minima_provincia(compras, provincia):
    '''
    res = []
    for c in compras:
        if provincia is None or:
            res.append(c)
    '''
    res = filter(lambda c: provincia is None or c.provincia == provincia, compras)

    maximo = max(res, key= lambda c:c.total_compra)
    minimo = min(res, key= lambda c:c.total_compra)

    return (maximo, minimo)


def numero_compras_por_hora(compras):
    res = dict()
    for c in compras:
        if c.fecha_llegada.date() in res:
            res[c.fecha_llegada.date()] += 1
        
        else:
            res[c.fecha_llegada.date()] = 1

def hora_menos_afluencia(compras):
    res = numero_compras_por_hora(compras)
    
    return min(res, key= lambda hora: hora.get())


def total_compras_por_supermercado(compras):
    res = defaultdict(float)
    for c in compras:
        res[c.supermercado] += c.total_compra
    return res

def supermercados_mas_facturacion(compras, n=3): 
    res = total_compras_por_supermercado(compras)
    
    ordenado = sorted(res.items(), key= lambda tupla: tupla[1], reverse= True)[n]
    
    return list(enumerate(ordenado, 1))

def provincias_por_clientes(compras):
    res = defaultdict(set)
    for c in compras:
        res[c.dni].add(c.supermercado)
    
    return res
def clientes_itinerantes(compras, n):
    
    provincias_clientes = provincias_por_clientes(compras)

    filtrado = filter(lambda tupla: len(tupla[1]) > n , provincias_clientes)

    res = map(lambda tupla: tupla[0], sorted(filtrado[1]), filtrado)

    return res


def compras_por_fecha(compras):
    res = defaultdict(float)

    for c in compras:
        res[c.fecha_salida.date()] += c.total_compra

    return res

def dias_estrella(facturacion_por_dias):
    compras_por_dias_ordenado = sorted(facturacion_por_dias.items())
    dia_antes_ahora_despues = zip(compras_por_dias_ordenado,compras_por_dias_ordenado[1:],compras_por_dias_ordenado[2:])

    dias_estrella = filter(lambda trio: trio[2][1] < trio[1][1] > trio[0][1], dia_antes_ahora_despues)

    return dias_estrella

def calcula_dias_estrella(compras, supermercado, provincia):

    compras_por_sitio = filter(lambda c: c.supermercado == supermercado and c.provincia == provincia, compras)

    compras_por_fecha = compras_por_fecha(compras_por_sitio)

    res = dias_estrella(compras_por_fecha)
    
    return sorted(res)


