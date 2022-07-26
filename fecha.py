print("========================================================================")
print("Programa para calcular el dia siguiente de una fecha dada por el usuario")
print("========================================================================\n")

dia = int(input("Ingrese el DIA: "))
mes = int(input("Ingrese el MES: "))
año = int(input("Ingrese el AÑO: "))

lista_uno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
lista_dos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
for i in lista_uno:
    if dia == i:
        dia += 1
        print(dia, mes, año)
        break
    elif mes == 12 and dia == 31:
        dia -= 30
        mes -= 11
        año += 1
        print(dia, mes, año)
    elif dia == 31:
        dia -= 30
        mes += 1
        print(dia, mes, año)
    
        
    #, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
