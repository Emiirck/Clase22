


suma = 0

N = int(input("Ingrese el número de notas: "))

notas = []

for i in range(1, N + 1):
    temp = float(input("Ingrese las notas: "))
    notas.append(temp)
    suma += temp

media = suma / N

if 90 <= media <= 100:
    print("A")
elif 80 <= media <= 90:
    print("B")
elif 70 <= media <= 80:
    print("C")
elif 60 <= media < 70:
    print("D")
else:
    print("E")