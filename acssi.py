print("=================================================================")
print("Programa que imprime la tabla ASCII a partir del 64 hasta el 256.")
print("=================================================================")

var2=([i for i in range(64, 257)])
numeros = var2
for numero in numeros:
    print("El carácter que representa a {} es {}".format(numero, chr(numero)))