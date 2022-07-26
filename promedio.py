print("================================================")
print ("Sistema para calcular el promedio de un alumno.")
print("================================================")
nombre = input("Para comenzar, ¿cual es tu nombre? ")

matematicas = int(input(nombre + " ¿cual es tu calificacion en matematicas? "))
quimica = int(input(nombre + " ¿cual es tu calificacion en quimica? "))
sociales = int(input(nombre + " ¿cual es tu calificacion en sociales? "))

promedio = (matematicas + quimica + sociales) / 3

if promedio >= 6:
    print ('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
    print ('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio,2))
else:
    print ('Lo sentimos ' + nombre + ' " has reprobado con un promedio de : ', promedio)
    print ('Lo sentimos ' + nombre + ' " has reprobado con un promedio de : ', round(promedio,2))

print("fin.")





 
