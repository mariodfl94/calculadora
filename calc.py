def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

while True:
    opcion = input("Introduce tu elección (1/2/3/4): ")

    if opcion in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Entrada inválida. Introduce números válidos.")
            continue

        if opcion == '1':
            print(num1, "+", num2, "=", suma(num1, num2))
        elif opcion == '2':
            print(num1, "-", num2, "=", resta(num1, num2))
        elif opcion == '3':
            print(num1, "*", num2, "=", multiplicacion(num1, num2))
        elif opcion == '4':
            resultado = division(num1, num2)
            print(num1, "/", num2, "=", resultado)
        
        next_calculation = input("¿Quieres hacer otro cálculo? (sí/no): ")
        if next_calculation == "no":
            break
    else:
        print("Opción inválida")