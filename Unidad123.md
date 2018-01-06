# Introducción a Python

## ¿Qué es Python?

Python es un lenguaje de programación con tipado dinámico, fuertemente tipado, multiplataforma y orientado a objetos. 
Su nombre está inspirado en el grupo de cómicos ingleses Monty Python de 1969. 



## Versiones de Python

Existen dos versiones principales de Python: Python 2 y Python 3. En este curso utilizaremos Python 3. 


## Instalación

Python puede ser instalado desde 

> http://www.python.org

En una terminal podemos escribir `python` para comprobar si Python se ha instalado correctamente. 

~~~py
Python 2.5.1 (r251:54863, May 2 2007, 16:56:35)
[GCC 4.1.2 (Ubuntu 4.1.2- 0ubuntu4)] on linux2
Type “help”, “copyright”, “credits” or “license” for more
information.
>>>
~~~

## Hello World! 

> Intérprete

> Código fuente y ejecutándolo

~~~py
print("Hello World")
print("Hola Mundo")
~~~
Para ejecutar el programa sólo es necesario indicar el nombre del archivo al intérprete de Python

~~~py
python hola.py
~~~

# Tipos y Colecciones

**Recordemos:** No es necesario declarar el tipo de variable. Cada variable en Python es un objeto. 

Tipos: números, cadenas de texto, booleanos

Colecciones de datos: listas, tuplas y diccionarios

~~~py
# cadena de texto
c = "hola mundo"

# entero
e = 23

# float

f = 7.3

print(type(c))
print(type(e))
print(type(f))
~~~

**Operadores**

~~~py
+ Suma
- Resta
* Multiplicación
** Exponente
/ División
// División entera
% Modulo

~~~

## Numeros, Cadenas y Booleanos

En Python podemos representar números enteros, reales y complejos: `int`, `float` y `complex`.

Las cadenas se representan entre comillas simples o dobles. Caracteres especiales: nueva línea `\n`, tabulación `\t`, etc.

Los booleanos sólo pueden tener dos valores: True y False. 

**Operadores lógicos**

~~~py
and 
or
not
== valores iguales
!= valores distintos
<
>
<=
>=
~~~

## Listas, Tuplas y Diccionarios
**Listas**
Las listas son colecciones ordenadas (arrays o vectores), que pueden contener números, cadenas, booleanos y listas. 

~~~py

l = [22, True, "hola" [3,4]]

# acceder a los elementos de una lista

uno = l[0]
ultimo = l[4][0]

# asignacion

l[0] = 33

# acceder al ultimo elemento 

u = l[-1]

# slicing

a = l[1:]
b = l[:2]
c = [:]

# Estructura de datos

# list.append(x), list.instert(i,x), list.remove(x), list,count(x)

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

# Resultado 2 1 0

a.insert(2, -1)
a.append(333)
# Resultado  a [66.25, 333, -1, 333, 1, 1234.5, 333]

a.remove(333)
# Resultado a [66.25, -1, 333, 1, 1234.5, 333]
~~~

**Tuplas**
Las tuplas se definen entre paréntesis. Las tuplas, a diferencia de las listas, son inmutables y tienen un tamaño fijo. 

~~~py 
t = (1,)
print(type(t))

# acceder a los elementos de una tupla

a = t[0]

~~~
**Diccionarios**
Los diccionarios son colecciones que relacionan una clave y un valor. Por ejemplo:

~~~py 
m = {"materia": "python",
      "profesor": "Perengano Godinez",
       "escuela": "UAM"}      

#Se accede a los elementos de un diccionario por su clave.

d["materia"] 

~~~
