# Calculadora básica en Python con comentarios detallados en español
import os

# Función para sumar dos números
def suma(a, b):
    return a + b  # Retorna la suma de a y b

# Función para restar dos números
def resta(a, b):
    return a - b  # Retorna la resta de a menos b

# Función para multiplicar dos números
def multiplicacion(a, b):
    return a * b  # Retorna la multiplicación de a y b

# Función para dividir dos números
def division(a, b):
    if b == 0:
        print("Error: División por cero")  # Error si el denominador es cero
        return None
    else:
        return a / b  # Retorna la división de a por b

# Función para comparar dos números
def comparar(a, b):
    print (a is b)

# Función principal para interactuar con el usuario
def calculadora():
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    # Leer la elección del usuario
    eleccion = input("Ingrese su elección (1/2/3/4): ")
    
    # Leer los dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Ejecutar la operación seleccionada
    if eleccion == '1':
        print(f"La suma de {num1} y {num2} es {suma(num1, num2)}")
    elif eleccion == '2':
        print(f"La resta de {num1} y {num2} es {resta(num1, num2)}")
    elif eleccion == '3':
        print(f"La multiplicación de {num1} y {num2} es {multiplicacion(num1, num2)}")
    elif eleccion == '4':
        if num2 != 0:
            print(f"La división de {num1} y {num2} es {division(num1, num2)}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Elección inválida")  # Error si la elección no es válida

# Variable global innecesaria
resultado = 0

# Función innecesariamente complicada
def operacion_compleja(a, b):
    for i in range(5):
        for j in range(3):
            if i == 3 and j == 2:
                resultado = a * b * 12345
            else:
                resultado = a + b * 67890
    return True
    return resultado

# Llamar a la función principal
if __name__ == "__main__":
    calculadora()
