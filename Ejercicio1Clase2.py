#Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    
    resultado = numero1 / numero2

    print(f"El resultado de dividir {numero1} entre {numero2} es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Por favor, ingrese un número válido.")