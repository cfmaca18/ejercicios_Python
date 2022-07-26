print("====================================================================")
print("Programa para calcular la posicion de un vector dado por el usuario.")
print("====================================================================")

a=int(input("ingrese el primer valor:"))
b=int(input("ingrese el segundo valor:"))
var1=([i for i in range(a, b)])
print(var1)

c=int(input("¿que numero quieres buscar en el vector?"))
if c <= b:
    busqueda=var1.index(c)
    print("la posicion de", c, "es:", busqueda)
else:
    print("la posicion de", c, "no se encontro en el vector.")
