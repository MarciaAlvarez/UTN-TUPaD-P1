#Práctico 11: Aplicación de la Recursividad 

#Ejercicios  
#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario


def factorial_recursivo(n):
    if n == 0:
        return 1  # Caso base: factorial de 0 es 1
    else:
        return n * factorial_recursivo(n - 1)  # Llamada recursiva

# Obtener el número límite del usuario
numero_limite = int(input("Introduce un número entero: "))

# Calcular y mostrar el factorial de todos los números entre 1 y el límite
print("Factorial de los números del 1 al", numero_limite, ":")
for i in range(1, numero_limite + 1):
    factorial = factorial_recursivo(i)
    print(f"El factorial de {i} es {factorial}")



#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 


    def fibonacci_recursivo(n):
        if n <= 1:
            return n
        else:
            return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def mostrar_serie_fibonacci(n):
    print("Serie de Fibonacci hasta la posición", n, ":")
    for i in range(n + 1):
        print(fibonacci_recursivo(i), end=" ")
    print()

# Ejemplo
n = int(input("Ingrese la posición de la serie de Fibonacci: "))
valor_fibonacci = fibonacci_recursivo(n)
print("El valor de Fibonacci en la posición", n, "es:", valor_fibonacci)
mostrar_serie_fibonacci(n)



#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#algoritmo general. 


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Ejemplo
base = 2
exponente = 3
resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es igual a {resultado}")



#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. 
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
#unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este 


def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

#ejemplo 
decimal_numero = 10
binario_numero = decimal_a_binario(decimal_numero)
print(f"El número decimal {decimal_numero} en binario es: {binario_numero}")



#procedimiento: 
#1. Dividir el número por 2. 
#2. Guardar el resto (0 o 1). 
#3. Repetir el proceso con el cociente hasta que llegue a 0. 
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario. 


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
# Requisitos: 
#La solución debe ser recursiva. 
#No se debe usar [::-1] ni la función reversed().


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]


#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 
#     Restricciones: 
#No se puede convertir el número a string. 
#Usá operaciones matemáticas (%, //) y recursión. 
#Ejemplos: 
#suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
#suma_digitos(9)      → 9 
#suma_digitos(305)    → 8   (3 + 0 + 5) 



def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

print(suma_digitos(1234))  # Output: 10



#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque. 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide. 
#      Ejemplos: 
#contar_bloques(1)   → 1         (1) 
#contar_bloques(2)   → 3         (2 + 1) 
#contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 



#Contar bloques en una pirámide 
def contar_bloques(n): 
    if n == 1: 
        return 1 
    else: 
        return n + contar_bloques(n - 1)
contar_bloques(4)



#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número. 
#      Ejemplos: 
#contar_digito(12233421, 2)   → 3   
#contar_digito(5555, 5)       → 4   
#contar_digito(123456, 7)     → 0  

def contar_digito(numero, digito): 
    if numero == 0: 
        return 0 
    else:
        ultimo = numero % 10 
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)


