print("===========================================================")
print("Programa para converir numeros romanos a numeros naturales.")
print("===========================================================")
a=input("Ingrese el numero en MAYUSCULAS que quiera convertir a entereo: ")

def convertir(romano):
    romanos={"I":1, "V":5, "X":10, "L":50, "C":100}
    entero=0
    for i in range(len(romano)):
        if i > 0 and romanos[romano[i]] > romanos[romano[i-1]]:
            entero += romanos[romano[i]] - 2 * romanos[romano[i-1]]
        else:
            entero += romanos[romano[i]]
    return entero
print(convertir(a))