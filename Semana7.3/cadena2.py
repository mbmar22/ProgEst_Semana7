def nombreCompleto(nombres, apellidos):
    return f"{nombres} {apellidos}"

def nombreCompletoMayuscula(nombres, apellidos):
    return f"{nombres} {apellidos}".upper()

def nombreCompletoMinuscula(nombres, apellidos):
    return f"{nombres} {apellidos}".lower()

def nombreCompletoCapitalizable(nombres, apellidos):
    return f"{nombres.capitalize()} {apellidos.capitalize()}"

def nombreCompletoTitulo(nombres, apellidos):
    return f"{nombres} {apellidos}".title()

def generarCorreo(nombres, apellidos):
    return f"{nombres[:3]}.{apellidos[:3]}@uamv.edu.ni".lower()

nombres = input("Dime tus nombres: ")
apellidos = input("Dime tus apellidos: ")

print(nombreCompleto(nombres, apellidos))
print(nombreCompletoMayuscula(nombres, apellidos))
print(nombreCompletoMinuscula(nombres, apellidos))
print(nombreCompletoCapitalizable(nombres, apellidos))
print(nombreCompletoTitulo(nombres, apellidos))
print(generarCorreo(nombres, apellidos))