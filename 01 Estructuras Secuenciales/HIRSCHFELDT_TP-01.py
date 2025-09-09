
import math
# Actividad 1. Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola mundo!")

# Actividad 2. Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre = input("Ingrese su nombre: ")
print(f"{nombre}")

# Actividad 3. Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Actividad 4. Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro
radio=float(input("Ingrese el radio de un circulo: "))
pi=math.pi
area = pi * (radio**2)
perimetro = 2 * radio * pi
print(f"El área del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

# Actividad 5. Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = float(segundos / 3600)
print(f"La cantidad de horas que equivale a {segundos} es: {horas} horas.")

# Actividad 6. Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Ingrese un número: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# Actividad 7. Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1= int(input("Ingrese el primer número distinto de 0: "))
num2= int(input("Ingrese el segundo número distinto de 0: "))
print(f"La suma de {num1} y {num2} es igual a: {num1 + num2}")
print(f"La multiplicacion de {num1} y {num2} es igual a: {num1 * num2}")
print(f"La division de {num1} y {num2} es igual a: {num1 / num2}")
print(f"La division de {num2} y {num1} es igual a: {num2 / num1}")
print(f"La resta de {num1} y {num2} es igual a: {num1 - num2}")
print(f"La resta de {num2} y {num1} es igual a: {num2 - num1}")

# Actividad 8. Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal (imc) es: {imc}")

# Actividad 9. Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit
celsius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius} grado Celsius es equivalente a {fahrenheit} grados fahrenheit")

# Actividad 10. Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
promedio = float((num1 + num2 + num3)/3) 
print(f"El promedio de los numeros {num1}, {num2} y {num3} es: {promedio}")