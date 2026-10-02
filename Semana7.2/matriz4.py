#suma de matrices cuadradas

matrizA=[]
matrizB=[]

def imprimirmatriz(matriz):
    for fila in matriz:
        print(fila)

#llenar matriz
for i in range(2):
    matrizA.append([]) #el ([]) indica un lugar vacio
    for j in range(2):
        elemento= float(input(f"Dime el valor de posicion ({i}, {j}): "))
        matrizA[i].append(elemento)

print("Llenar matriz B")
for i in range(2):
    columnas=[]
    for j in range(2):
        elemento = float(input(f"Elemento ({i+1}, {j+1}): "))
        columnas.append(elemento)
    matrizB.append(columnas)


matrizC = []
for i in range(2):
    fila = []
    for j in range(2):
        suma = 0
        for k in range(2):
            suma += matrizA[i][k] * matrizB[k][j]
        fila.append(suma)
    matrizC.append(fila)


print("Mostrar matriz A")
imprimirmatriz(matrizA)

print("Mostrar matriz B")
imprimirmatriz(matrizB)

print("Mostrar matriz C")
imprimirmatriz(matrizC)


#suma de matrices cuadradas
matrizA=[]

def imprimirmatriz(matriz):
    for fila in matriz:
        print(fila)

#llenar matriz
for i in range(2):
    matrizA.append([]) #el ([]) indica un lugar vacio
    for j in range(2):
        elemento= float(input(f"Dime el valor de posicion ({i} {j}): "))
        matrizA[i].append(elemento)

escalar=int(input("Ingrese el escalar: "))


matrizC=[]
for i in range(2):
    columnas = []
    for j in range(2):
        valor= matrizA[i][j]*escalar
        columnas.append(valor)
    matrizC.append(columnas)


print("Mostrar amtriz A")
imprimirmatriz(matrizA)

print("Mostrar amtriz C")
imprimirmatriz(matrizC)