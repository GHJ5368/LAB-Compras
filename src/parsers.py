from datetime import datetime

def parsea_fecha(fecha):
    return datetime.strptime(fecha, "%d/%m/%Y %H:%M")