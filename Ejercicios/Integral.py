# intervalo de integracion
a = 0
b = 3
# Numero de rectangulos entre a y b
n = 5
# Tamano de rectangulo
d = (b-a)/ (n *1.0)
# Inicializamos la variable
I = 0

#DEFINIR UNA FUNCION
def f(x):
    return x**2 - 2*x + 4
#range (0,n) = range(n)

# Recordatorio: La funcion range
# range(3) = [0,1,2]
# range(1,6,2) = [1,3,5]

for i in range(n):
    # Punto inicial izquierdo del rectangulo
    xi = a + i*d
    # Punto final, derecha del rectangulo
    xii = a + (1+i)*d

    # La altura del rectangulo en el punto xi y xii
    fi = f(xi)
    fii = f(xii)

    # La altura promedio del rectangulo
    h = (fi + fii) / (2 * 1.0)

    # Area del rectangulo
    A = d*h

    # Se hace la suma de Riemman
    I += A
    # I = I + A

print (I)
