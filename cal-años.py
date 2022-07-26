print("===================================================================================")
print("Programa para calcular su edad actual, ingresando su fecha de nacimiento(DD/MM/AAAA")
print("===================================================================================")

nombre=input("Ingresa tu nombre: ")
dia=int(input("Hola "+ nombre + " ingrese su dia de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))
año=int(input("Ingrese su año de nacimiento: "))
lista_1=[1, 3, 5, 7, 8, 10, 12]
lista_2=[4, 6, 9, 11]

año_actual=2022

año-=año_actual

resultado=abs(año)

for i in lista_1:
    if dia > 31 and mes == i:
        print("El mes", mes, "no tiene", dia,"dias.")
        quit() 
for i in lista_2:
    if dia > 30 and mes == i:
        print("El mes", mes, "no tiene", dia,"dias.")
        quit()
if dia > 28 and mes == 2:
    print("El mes", mes, "no tiene", dia,"dias.")    
elif mes <= 7:
    print(nombre,"su edad actual es", resultado,"años.")
elif mes > 7:
    resultado -= 1
    print(nombre,"su edad actual es", resultado,"años.")            
   
    
