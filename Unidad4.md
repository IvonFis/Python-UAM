# Control de flujo

## Secuencuas condicionales

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




## Ejercicios

