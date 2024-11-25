import csv
import datetime
from typing import NamedTuple
from parsers import *

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

