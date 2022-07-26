print("===================================================================================")
print("Programa para calcular su edad actual, ingresando su fecha de nacimiento DD/MM/AAAA")
print("===================================================================================")

nombre=input("Ingresa tu nombre: ")
dia=int(input("Hola "+ nombre + " ingrese su dia de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))
año=int(input("Ingrese su año de nacimiento: "))
lista_1=[1, 3, 5, 7, 8, 10, 12]
lista_2=[4, 6, 9, 11]

if año > 2022:
    print("El año ingresado no puede ser mayor al año actual (2022)")
    exit()

for i in lista_1:
    if dia > 31 and mes == i and año <= 2022:
        print("El mes", mes, "no tiene", dia,"dias.")
        quit()
    elif dia <= 31 and mes == i and año == 2022:
        r = mes - 7
        r=abs(r)
        print(nombre, "su edad actual es", r, "meses")
        exit()
for i in lista_2:
    if dia > 30 and mes == i and año <= 2022:
        print("El mes", mes, "no tiene", dia,"dias.")
        quit()
    if dia <= 30 and mes == i and año == 2022:
        r = mes - 7
        r=abs(r)
        print(nombre, "su edad actual es", r, "meses")
        exit()
if dia > 28 and mes == 2 and año <= 2022:
    print("El mes", mes, "no tiene", dia,"dias.") 
elif dia <= 28 and mes == 2 and año == 2022:
    r = mes - 7
    r=abs(r)
    print(nombre, "su edad actual es", r, "meses")
elif mes <= 7:
    año-=2022
    resultado=abs(año)
    print(nombre,"su edad actual es", resultado,"años.")
elif mes > 7:
    año-=2022
    resultado=abs(año)
    resultado -= 1
    print(nombre,"su edad actual es", resultado,"años.")            
   
    
