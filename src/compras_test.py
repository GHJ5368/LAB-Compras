from compras import *

def test_lee_compras(fichero):
    resultado = lee_compras(fichero)
    print("EJERCICIO 1")
    print(f"Número de registros leídos: {len(resultado)}")
    print(f"Tres primeros registros: {resultado[:3]}")
    print(f"Tres últimos registros: {resultado[-3:]}")


if __name__ == "__main__":
    datos = lee_compras("LAB-Compras\data\compras.csv")
    test_lee_compras("LAB-Compras\data\compras.csv")
