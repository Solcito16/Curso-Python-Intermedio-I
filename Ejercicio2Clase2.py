#Escribe un programa que intente sumar un número y una cadena. Si se produce un error
#de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.


try:
    numero1 = float(input("Ingrese un número: "))
    cadena1 = (input("Ingrese una cadena: "))
    
    resultado = numero1 + cadena1

    print(f"El resultado de sumar {numero1} entre {cadena1} es: {resultado}")
except TypeError:
    print("Error: No se puede sumar variables de distinto tipo.")