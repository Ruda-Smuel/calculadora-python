def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    else:
        return a / b

while True:
    print("===== CALCULADORA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("=======================")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "5":
        print("¡Hasta luego!")
        break
    elif opcion in ["1", "2", "3", "4"]:
        numero1 = float(input("Primer número: "))
        numero2 = float(input("Segundo número: "))
        
        if opcion == "1":
            resultado = sumar(numero1, numero2)
        elif opcion == "2":
            resultado = restar(numero1, numero2)
        elif opcion == "3":
            resultado = multiplicar(numero1, numero2)
        elif opcion == "4":
            resultado = dividir(numero1, numero2)
        
        print("=======================")
        print("Resultado:", resultado)
        
    else:
        print("=======================")
        print("Opción inválida")
