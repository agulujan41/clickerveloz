"""nombre = input("Ingrese un nombre:")
apellido = input("Ingrese apellido:")
nacimiento = input("Ingrese fecha de nacimiento:")
lugar_nacimiento = input("Ingresar nacimiento:")
print(f"Sr, {nombre} {apellido} de fecha de nacimiento {nacimiento} de {lugar_nacimiento}")"""

import time
tiempo_inicio = time.time() 

parar = input("Apretar una tecla para parar: ")

tiempo_fin = time.time() 

tiempo = tiempo_fin - tiempo_inicio
print("Tiempo transcurrido:",tiempo)