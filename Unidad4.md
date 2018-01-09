# Control de flujo

## Secuencias condicionales

Con las secuencias condicionales podemos elegir entre dos rutas diferentes basadas en un valor booleano.  

**if**

La ejecución condicional se escribe con la palabra `if [condicion]:` seguido de la condición a evaluar y en la siguiente e identado la acción a ejecutar, la acción dentro del `if` solo se ejecutará si la condición se cumple. Por ejemplo: 

~~~py
a = 5
if a > 2:
  print("tu numero es menor que 5")
  print("adios")

# atencion a la identacion

if a > 2:
  print("tu numero es menor que 5")
print("adios")

# nota importante
s= "hello"
f = 1.0
i = 40

if s == "hello":
    print("String: %s" % s)
if f == 1.0:
    print("Float: %f" % f)
if i == 40:
    print("Integer: %d" % i)
~~~

**if... else**

En caso de que se desee ejecutar una orden alternativa en caso de que la condición no se cumpla podemos usar la palabra `else:`, por ejemplo: 

~~~py
a == "hamburguesa"
if a == "hamburguesa":
  print("tu orden esta lista")
 else: 
  print("lo sentimos, nos quedamos sin hamburguesas")
~~~

**if ... elif... elif... else**

`elif` es una contracción de `else` `if`, por ejemplo: 

~~~py
a = 0
if a < 0:
  print("tu numero es negativo")
elif a > 0:
  print("tu numero es positivo")
else:
  print("tu numero es 0")
~~~

Como notarás la primera condición evaluada es `if a < 0:`, si no se cumple la confición elavula la condicion `elif a > 0:`, de nuevo, si no cumple ninguna condición sucesiva `elif` ejecuta el código `else:`.

**Operadores**
 
**Booleanos** Este tipo de operador permite usar expresiones booleanas al evaluar una condición if.

**in** Este operador permite evaluar si determinados objetos existen dentro de un objeto "contenedor", como una lista

Por ejemplo: 

~~~py
orden = "papas"
tiempo = 30

if orden == "papas" and tiempo == 30:
  print("Tu orden esta lista")
  
if orden in ["papas", "hamburguesa"]:
  print("Aun tenemos papas")
~~~

## Bucles

¿Cómo crearía un programa que escribiera los primeros 6 números pares? ¿los primeros 1000?

El control de flujo que nos permite ejecutar un mismo fragmento de código mientras se cumpla una determianda condición se llama bucle y podemos ejecutarlo con la palabra `while` y `for`, por ejemplo: 

~~~py
edad = 0 
while edad < 18:
  edad = edad + 1
  print("Tienes %d" %edad)

# o bien

edad = 0 
while edad < 18:
  edad += 1
  print("Tienes %d" %edad)
~~~

La variable comienza valiendo 0, la edad aumenta de 1 en 1 hasta que deje de cumplirse la condición `edad < 18`. 

**for**

Los bucles `for` pueden iterar sobre una secuencia de números usando un rango determinado, por ejemplo: 

~~~py
pares = [2, 4, 6, 8, 10]
for x in pares:
  print(x)

for y in range(5):
  print(y)

for z in range (3,10):
  print(z)

for x in (1,10,2):
  print(x)
~~~

**break and continue**

**break** Usamos la palabra `break` para salir de un loop (`for` o `while`)

**continue** Usamos la palabra `continue` para saltar la condición y regresar a la condición (`for` o `while`).

Por ejemplo, 

~~~py
edad = 0
while True: 
  print(edad)
  edad += 1
  if edad >= 5:
    break

for x in range(10):
  if x % 3 == 0:
    continue
  print(x)
~~~

## Ejercicios

* Imprima todos los números pares de la siguiente lista, además no imprima ningún número después del número 237

~~~py
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
~~~

* Escriba un loop que imprima lo siguiente 

~~~py
#
##
###
####
#####
######
#######
~~~

* a) Escriba todos los número del 1 al 100 excepto los divisibles entre 3, b) escriba la palabra `alpaca` en lugar de los números divisibles entre 5, c) escriba la palabra `hola alpaca` para los números que son divisibles entre 3 y 5. 

* Escriba un programa que genere un string que represente un grid de 8x8 para formar un tablero de ajedrez como se muestra 

~~~py
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # #
~~~

* a)  Escriba un código que imprima los primeros 20 números de Fibonacci en una lista b) filtre los números de Fibonacci generados a otra lista que contenga solo los numeros pares.
