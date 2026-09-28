matriz = []
i = 0
j = 0

def pedirTamaño(i, j):
    global filas, columnas
    filas = int(input("Tamaño de Filas:"))
    columnas = int(input("Tamaño de Columnas:"))
    
def leerValor():
    while True:
        try:
            valor = int(input("Dime un valor númerico: "))
            return valor
        except ValueError:
            print("Error. Verifique que el valor sea entero.")

def agregarElemento():
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            dato = leerValor(f"Valor [{i}, {j}]: ")
            matriz[i].append(dato)

pedirTamaño(2, 2)
print(filas, columnas)

agregarElemento()

def menu():
    print("""
          1. Asignar tamaño.
          2. Agregar elemento
          3. Salir""")
    op =  leerValor("Opción: ")
    return op

def main():
    while True:
        op = menu()
        if op == 1:
            pedirTamaño()
        elif op == 2:
            agregarElemento()
        elif op == 3:
            print("Ádios...")
            break

main()
