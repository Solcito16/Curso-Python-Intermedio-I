#Ejercicio 3
#Determinar si un número es par o impar


def par_o_impar():
    # Pedimos al usuario que ingrese un número
    num = int(input("Ingresa un número: "))
    
    # Verificamos si el número es par o impar
    resultado = "Par" if num % 2 == 0 else "Impar"
    
    # Mostramos el resultado en pantalla
    print(f"El número {num} es {resultado}")

par_o_impar()
