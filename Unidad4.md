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
~~~

**if... else**

En caso de que se desee ejecutar una orden alternativa en caso de que la condición no se cumpla podemos usar la palabra `else:`, por ejemplo: 

~~~py
a == "hamburguesa"
if a == "hamburguesa":
  print("tu orden esta lista")
 else: 
  print("lo sentimos, nos quedamos sin hambueguesas")
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

Como notarás la primera condición evaluada es `a < 0`, al no cumplir la condición 


## Bucles

## Ejercicios

