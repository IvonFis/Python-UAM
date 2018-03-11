# Codigos importados
# Forma 1 de importar codigos
import Area_cubo

# Forma 2
# from [Nombre del programa] import [Nombre de funcion]
from Volumen_cubo import Volumen

# ------------------------
# Librerias de este codigo
import sys

def main():
    l = float(sys.argv[1])
    # Calculo de la cara de un cubo
    area = Area_cubo.Area(l)
    print("El area de una cara de este cubo es: %s"%area)

    # Calculo del volumen de un cubo
    volumen = Volumen(l)
    print("El Volumen del cubo es: %s"%volumen)

if __name__ == "__main__":
    main()



