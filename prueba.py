# pide al usuario que ingrese su nombre y edad, luego muestra un mensaje con su nombre y edad, y calcula cuántos años tendrá el próximo año.

"""Nombre = input("Ingrese su nombre: ")
Edad = int(input("Ingrese su edad: "))

edad_usuario = Edad + 1 

print("Hola " + Nombre + ", tienes " + str(Edad) + " años.")
print("El próximo año tendrás " + str(edad_usuario) + " años.")"""

#pide al usuario que ingrese la temperatura en grados Celsius y luego la convierte a Fahrenheit y Kelvin, mostrando los resultados.

'''Temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
Temperatura_Fahrenheit = (Temperatura * 9/5) + 32
temperatura_Kelvin = Temperatura + 273.15
print("La temperatura en Fahrenheit es: " + str(Temperatura_Fahrenheit) + "grados.")
print("La temperatura en Kelvin es: " + str(temperatura_Kelvin) + "grados.")'''

#pide al usuario que ingrese tres notas de diferentes materias, calcula el promedio y muestra los resultados.

'''nota_matematicas = float(input("Ingrese la primera nota: "))
nota_fisica = float(input("Ingrese la segunda nota: "))
nota_quimica = float(input("Ingrese la tercera nota: "))

promedio = (nota_matematicas + nota_fisica + nota_quimica) / 3
print(f"El promedio de las notas es {promedio}")'''

#pide al usuario que ingrese un número y luego muestra si es par o impar.














# Una persona vende un producto en línea. El programa pide el precio de venta, el costo de compra, el porcentaje de comisión de la plataforma y el costo del envío que asume el vendedor. Calcula la comisión en pesos, el costo total y la ganancia neta por unidad. Luego pide cuántas unidades vendió en el mes y muestra la ganancia mensual.


'''precio_venta = float(input("Ingrese el precio de venta del producto: "))
costo_compra = float(input("Ingrese el costo de compra del producto: "))
porcentaje_comision = float(input("Ingrese el porcentaje de comisión de la plataforma: "))
costo_envio = float(input("Ingrese el costo del envío que asume el vendedor: "))

comision_pesos = (porcentaje_comision / 100) * precio_venta
costo_total = costo_compra + comision_pesos + costo_envio

Unidades_vendidas = int(input("Ingrese la cantidad de unidades vendidas en el mes: "))

ganancia_neta_por_unidad = precio_venta - costo_total
ganancia_mensual = ganancia_neta_por_unidad * Unidades_vendidas

print(f"La comisión en pesos es: {comision_pesos}")
print(f"El costo total es: {costo_total}")
print(f"La ganancia neta por unidad es: {ganancia_neta_por_unidad}")
print(f"La ganancia mensual es: {ganancia_mensual}")

print("Gracias por usar el programa. ¡Hasta luego!")'''


# Una tienda vende tres productos. El programa pide el nombre y precio unitario de cada uno, junto
# con la cantidad comprada. Calcula el subtotal, el IVA del 19% y el total a pagar, y los muestra como
# una factura.

'''Producto1 = input("Ingrese el nombre del primer producto: ")
Precio1 = float(input("Ingrese el precio unitario del primer producto: "))
Cantidad1 = int(input("Ingrese la cantidad comprada del primer producto: "))

Producto2 = input("Ingrese el nombre del segundo producto: ")
Precio2 = float(input("Ingrese el precio unitario del segundo producto: ")) 
Cantidad2 = int(input("Ingrese la cantidad comprada del segundo producto: "))

Producto3 = input("Ingrese el nombre del tercer producto: ")
Precio3 = float(input("Ingrese el precio unitario del tercer producto: "))
Cantidad3 = int(input("Ingrese la cantidad comprada del tercer producto: "))

subtotal = (Precio1 * Cantidad1) + (Precio2 * Cantidad2) + (Precio3 * Cantidad3)
IVA = subtotal * 0.19

total = subtotal + IVA

print("_" * 30)
print("\nFactura:")
print(f"{Producto1}: {Cantidad1} x {Precio1} = {Precio1 * Cantidad1}")
print(f"{Producto2}: {Cantidad2} x {Precio2} = {Precio2 * Cantidad2}")
print(f"{Producto3}: {Cantidad3} x {Precio3} = {Precio3 * Cantidad3}")
print(f"Subtotal: {subtotal}")
print(f"IVA (19%): {IVA}")
print(f"Total: {total}")
print("_" * 30)'''

# Un grupo de amigos termina de comer. El programa pide el valor de la cuenta, el porcentaje de propina y el número de personas. Calcula la propina, el total con propina y cuánto debe pagar cada uno.

'''Valor_cuenta = float(input("Ingrese el valor de la cuenta: "))
propina = Valor_cuenta * 0.10 
personas = int(input("Ingrese el número de personas que van a pagar la cuenta: "))

total_con_propina = Valor_cuenta + propina
pago_por_persona = total_con_propina / personas

print(f"La propina es: {propina}")
print(f"El total con propina es: {total_con_propina}")
print(f"El pago por persona es: {pago_por_persona}")'''

# El programa pide al usuario que ingrese un número y luego muestra si es menor que 10, utilizando un bucle while para incrementar el número hasta que sea mayor o igual a 10.

"""Numero = int(input("Ingrese un número: "))

while Numero <10:
    print(f"El número {Numero} es menor que 10")
    Numero = Numero + 1
else:
    print(f"El número {Numero} es mayor o igual a 10 fin del programa")"""

# El programa muestra los números del 1 al 10 utilizando un bucle while.

"""numero = 1

while numero <= 10:
    print(f"el numero {numero}")
    numero = numero + 1"""

# El programa muestra los números del 10 al 1 utilizando un bucle while.

"""numero = 10 

while numero >= 1:
    print(f"el numero es {numero}")
    numero = numero - 1"""

# El programa muestra los números pares del 2 al 20 utilizando un bucle while.

"""numeros_pares = 2

while numeros_pares <= 20:
    print(f"el numero {numeros_pares} es par")
    numeros_pares = numeros_pares + 2"""

#

"""numeros_impares = 1

while numeros_impares <= 19:
    print(f"el numero {numeros_impares} es impar")
    numeros_impares = numeros_impares + 2"""

#pida al usuario que ingrese un número y luego muestre todos los números desde ese número hasta 5 utilizando un bucle while.

"""numero = int(input("Ingrese un número: "))

while numero <=5:
    print(f"El número es {numero}")
    numero = numero + 1"""

#Escriba un algoritmo que pida un número al usuario y lo muestre 5 veces en pantalla.

"""numero = int(input("Ingrese un número: "))
i = 1
while i <= 5:
    print(f"El número es {numero}")
    i = i + 1"""


#escriba un algortimo que muestre las tablas de multiplicar

"""tabla = int(input("Ingrese la tabla de multiplicar que desea ver: "))
i = 1

while i <= 10:
    resultado = tabla * i
    print(f"{tabla} x {i} = {resultado}")
    i = i + 1"""

#escriba un algoritmo que pida un número al usuario y muestre todos los números desde 1 hasta ese número.

"""numero = int(input("Ingrese un número: "))

x = 1

while x <= numero:
    print("el numero es " + str(x))
    x = x + 1"""

# pide un numero aleatorio a un usuario y que adivine cual es el numero

"""import random

numero_secreto = random.randint(1, 10)
print(f"el numero secreto es {numero_secreto}")

intentos = 3

numero_usuario = int(input("Adivina el número secreto entre 1 y 10: "))

while numero_usuario != numero_secreto:
    numero_usuario = int(input("Intenta de nuevo: "))
    intentos = intentos - 1

def print(arg1):
    ...

przint("¡Felicidades! Adivinaste el número secreto.")"""