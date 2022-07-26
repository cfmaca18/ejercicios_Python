print("===========================================================================================================================================")
print("Programa para mostrar numeros naturales en pantalla hasta 100, calcula el numero de pares que hay y cuales son, suma los impares que hayan.")
print("===========================================================================================================================================")
a=int(input("Ingrese el primer valor:"))
b=int(input("Ingrese el segundo valor:"))
print("=========================================")
if b <= 100:
    var1=([i for i in range(a, b)])
    print(var1)
    print("Hay", len(var1), "elementos, entre", a, "y", b)

    print("=========================================")

    var2=([i for i in range(a, b) if i%2==0])
    print("Numero de pares:",len(var2))
    print("=========================================")

    var3=([i for i in range(a, b) if i%2!=0])
    print("Los numeros impares entre", a, "y", b, "son:", var3)
    print("=========================================")
    sumvar3=sum(var3)
    print("El resultado de la suma de los numeros impares es:",sumvar3)
else:
    print("El valor maximo puede ser mayor a 100.")