"""
Descripcion: Codigo para calcular el Volumen
Enrique B.
fis.ebetancourt@gmail.com
Uso:

"""

# Librerias
import sys

# Funciones
def Volumen(l):
    '''
    Esta es una funcion que calcula el Volumen de un cubo.
    Argumentos:
        l - [Float], lado del cubo
    Regresa:
        [Float], Volumen del cubo de lado l
    '''
    volumen = l**3
    # Regresar el resultado del calculo
    return volumen

# Declarar la funcion principal
def main():
    # Tomar un input del usuario
    lado = float(sys.argv[1])

    # Aplicar la funcion Volumen
    volumen = Volumen(lado)

    # imprimir en la consola
    print(volumen)

# Para llamar main, se usa esta estructura
if __name__ == "__main__":
    main()


