
print("===========")
print("Calculadora")
print("===========")

print("Menu de opciones")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Salir")

a=int(input("Elija una opcion: "))

if a == 1:
    def suma():
        a=int(input("Ingrese el primer valor: "))
        b=int(input("Ingrese el segundo valor: "))
        return a + b
    result = suma()
    print("El resutado es:", result)
elif a == 2:
    def resta():
        a=int(input("Ingrese el primer valor: "))
        b=int(input("Ingrese el segundo valor: "))
        return a - b
    result = resta()
    print("El resutado es:", result)

elif a == 3:
    def multiplicacion():
        a=int(input("Ingrese el primer valor: "))
        b=int(input("Ingrese el segundo valor: "))
        return a * b
    result = multiplicacion()
    print("El resutado es:", result)

elif a == 4:
    def division():
        a=int(input("Ingrese el primer valor: "))
        b=int(input("Ingrese el segundo valor: "))
        return a / b
    result = division()
    print("El resutado es:", result)

elif a == 5:
    print("Vuelve pronto:)")
    exit()




