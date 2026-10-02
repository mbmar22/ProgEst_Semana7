#suma de matrices cuadradas
matrizA=[]
matrizB=[]

def imprimirmatriz(matriz):
    for fila in matriz:
        print(fila)

#llenar matriz
for i in range(3):
    matrizA.append([]) #el ([]) indica un lugar vacio
    for j in range(3):
        elemento= float(input(f"Dime el valor de posicion ({i} {j}): "))
        matrizA[i].append(elemento)

print("Llenar matriz B")
for i in range(3):
    columnas=[]
    for j in range(3):
        elemento = float(input(f"Elemento ({i+1}, {j+1}): "))
        columnas.append(elemento)
    matrizB.append(columnas)


matrizC=[]
for i in range(3):
    columnas = []
    for j in range(3):
        suma= matrizA[i][j] + matrizB[i][j]
        columnas.append(suma)
    matrizC.append(columnas)


print("Mostrar amtriz A")
imprimirmatriz(matrizA)

print("Mostrar amtriz B")
imprimirmatriz(matrizB)

print("Mostrar amtriz C")
imprimirmatriz(matrizC)