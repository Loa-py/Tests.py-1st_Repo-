def tablas(numero):
    for i in range(0, 11):
        print(f"{numero} * {i} = {i * numero}")


while True:
    numero = float(input("Tablas de multiplicación (0-10) de: "))
    tablas(numero)
