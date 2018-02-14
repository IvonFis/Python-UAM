# Ejercicios clase 2
# Ejercicio no. 1 

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]

#Solucion propuesta por alumno for i in alumnos_que_pasaron_al_pizarron
gato = 2
a = []
j = 0

while j < gato:
    j = j+1
    if j > -1:
        a.append(j*"#")

for i in a:
    print(i)

#Solucion clase
G = "#"
d = ""
for i in range(20):
    d += G
    print(d)

for y in range(1,101):
    if y%3==0 and y%5==0:
        print("hola alpaca")
    elif y%3==0:
        continue
    elif y%5 ==0:
        print("alpaca")
    else:
         print(y)

N = "#"
B = " "
tablero = ""

for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            tablero += B
        else: 
            tablero += N
    print(tablero)
    tablero=""

print("otra solucion")
#Solucion propuesta por alumno for i in alumnos_que_pasaron_al_pizarron
#Como le harian para un m impar?
s3 = "#"
s4 = " "
h = []
n=4
m=8
for x in range(m):
    if x%2==0:
        h.append(n*(s4+s3))
    else:
        h.append(n*(s3+s4))
    print(h[x])


