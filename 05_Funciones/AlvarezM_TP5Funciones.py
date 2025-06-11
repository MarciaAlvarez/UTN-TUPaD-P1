#Actividades:
#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde elprograma principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que recibacomo parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return "Hola" "," + "Marcos" + "!"

nombre_usuario= "Marcos"
saludo=saludar_usuario(nombre_usuario)
print(saludo)

#3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

informacion_personal("marcia", "alvarez", "30", "mataderos")

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math
def calcular_area_circulo(radio):
    return math.pi * radio**2
# Calcula el perímetro de un círculo dado su radio.
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Solicitar el radio al usuario
try:
    radio = float(input("Ingresa el radio del círculo: "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número.")
    exit()  # Salir del programa si la entrada no es válida

# Calcular el área y el perímetro
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# imprimir resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba 
# una cantidad de segundos como parámetro y devuelva la cantidad de horas 
# correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600
# Solicitar al usuario la cantidad de segundos
try:
    segundos = float(input("Introduce el número de segundos: "))
except ValueError:
    print("Entrada inválida. Por favor, introduce un número.")
    exit()
# Calcular las horas
horas = segundos_a_horas(segundos)
# Mostrar el resultado
print(f"{segundos} segundos son {horas} horas")



#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# solicitar al usuario el número
try:
    numero = int(input("Ingrese un número: "))
    tabla_multiplicar(numero)
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número.")


#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero" 
    return (suma, resta, multiplicacion, division)

# Ejemplo 
numero1 = 10
numero2 = 5
resultados = operaciones_basicas(numero1, numero2)

#imprimir
print(f"Para los números {numero1} y {numero2}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#división por cero
resultados2 = operaciones_basicas(5, 0)
print(f"\nPara 5 y 0:")
print(f"División: {resultados2[3]}")


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
#para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  return round(imc, 2)

# Solicitar al usuario los datos
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Llamar a la función y mostrar el resultado
imc = calcular_imc(peso, altura)
print(f"Su Índice de Masa Corporal (IMC) es: {imc}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.


def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# solicitar la temperatura en Celsius al usuario
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))

# Convertir a Fahrenheit usando la función
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)

# Mostrar el resultado
print(f"{temperatura_celsius}°C es equivalente a {temperatura_fahrenheit}°F")


#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.


def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Solicitar los números al usuario
print("Por favor, ingrese tres números:")
a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))

# Calcular el promedio
promedio = calcular_promedio(a, b, c)

# Mostrar el resultado
print(f"El promedio de {a}, {b} y {c} es: {promedio}")

###FIN####