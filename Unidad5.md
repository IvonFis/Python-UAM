## Funciones 

Usar funciones nos permiten dividir el código en bloques que podemos reutilizar nuestro código. Las funciones se declaran como: 

~~~py
def f():
  print("Hola funcion")
  
 def suma(a,b):
  return a+b
 
 def imprimir(texto, veces):
  print(veces * texto)
 
# Calling a function

fun1 = f()
fun2 = suma(2,3)
fun3 = imprimir("hola", 4)

print(fun1)
print(fun2)
print(suma(34,234))
print(fun3)
~~~

## Ejercicios

* Analice el siguiente programa ¿identifica todos los métodos utilizados? ¿cuál es el resultado? Bajo el mismo razonamiento realice un programa que resulte en la aproximación de la integral de la función `f(x) = x**2 + 3x - 5` para `x=8`.

~~~py
a = 0
b = 3
n = 5
d = (b-a)/ (n *1.0)
I = 0
#DEFINIR UNA FUNCION

def f(x):
    return x**2 - 2*x +4
#range (0,n) = range(n)

for i in range (n):
    xi = a + i*d
    xii = a + (1+i)*d

    fi = f(xi)
    fii = f(xii)

    h = (fi + fii) / (2 * 1.0)
    A = d*h
    I += A

print (I)
~~~

* Escriba un programa que imprima una tabla con valores de distancia contra tiempo para el tiro parabólico con las condiciones inicales de `V0x = 15 [m/s]`, `V0y = 20 [m/s]`, `x0 = y0 = 0` y considere `g = 9.81 [m/s**2]`.
