'''
Graficar salida de tiro parabolico
'''

import matplotlib.pyplot as plt
import sys
# from subprocess import call,Popen

# Leer las lineas de mi codigo
def LeerLineas(name):
    '''
    Lee las lineas de un archivo
    Argumentos:
        name - [String] nombre del archivo
    '''
    # Abrir el archivo
    data = open(name,"r")

    # Leer las lineas del archivo
    lines = data.readlines()
    # print(lines)

    # Cerrar el archivo
    data.close()

    return lines


def main():
    name = sys.argv[1]
    lineas = LeerLineas(name)

    # Separar el archivo en 3 columnas
    t = []
    x = []
    y = []

    for linea in lineas:
        # strip() remueve el caracter \n, "enter"
        # split() convierte un string en una lista, siguiendo una regla
        # por default la regla es que la lista esta separada por espacios
        ti = float(linea.strip().split(" ")[0])
        xi = float(linea.strip().split(" ")[1])
        yi = float(linea.strip().split(" ")[2])
        
        # Guardarlo en su lista respectiva
        t.append(ti)
        x.append(xi)
        y.append(yi)

    # Graficar T,Y
    plt.plot(t,y)
    plt.show()


if __name__ == "__main__":
    main()



