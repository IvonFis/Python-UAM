# PROBLEMA 1

numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
par = []

for x in numbers:
    if x % 2 == 0:
        par.append(x)
    if  x == 237:
        break
print(par)

# PROBLEMA 2

a = 1
b = 1
O = " "
X = "#"
c = ""
d = ""

for i in range(7):
    d += X
    print(d)

# PROBLEMA 4

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            c += O
        else:
            c += X
    print(c)
    c = ""

# PROBLEMA 3

for x in range(1, 100):
    if x % 5 == 0 and x % 3 == 0:
        print("hola alpaca")
    elif x % 5 == 0:
        print("alpaca")
    elif x % 3 == 0:
        continue
    else:
        print(x)

# PROBLEMA 5
#TAREA











