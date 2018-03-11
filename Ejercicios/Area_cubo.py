"""
Nombre Area_cubo.py
Descripcion: Codigo para calcular el Area
Enrique B.
fis.ebetancourt@gmail.com
Uso:

"""

# Librerias
import sys

# Funciones
def Area(l):
    '''
    Esta es una funcion que calcula el Area de un cuadrado.
    Argumentos:
        l - [Float], lado del cuadrado
    Regresa:
        [Float], Area del cuadrado de lado l
    '''
    area = l**2
    # Regresar el resultado del calculo
    return area

# Declarar la funcion principal
def main():
    # Tomar un input del usuario
    lado = float(sys.argv[1])

    # Aplicar la funcion Area
    area = Area(lado)

    # imprimir en la consola
    print(area)

# Para llamar main, se usa esta estructura
if __name__ == "__main__":
    main()


