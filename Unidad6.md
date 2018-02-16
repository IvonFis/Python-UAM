# Entrada y salida de archivos

En Python podemos importar o exportar bases de datos, hojas de cálculo o cualquier tipo de información almacenada como un archivo de texto (caracter por caracter) tipo **.csv** (comma separated values)  o **.txt.**.

## Lectura y escritura de archivos .csv y .txt

Analice el siguiente ejemplo: 

~~~py
lita = [1, 1, 2, 3, 5, 8, 13, 21, 25]
f = open("primer.txt", "w")
for x in lista: 
  f.write("{}, ".format(x))
f.close()
~~~

Analice el siguiente ejemplo: 

~~~py
f = open("primer.txt", "r")
for linea in f: 
  print("Contenido: {}".format(linea))
f.close()
~~~

## Ejercicios
