#Ejercicio 4
#Calcular el promedio de una lista de números usando args y un operador ternario

def calcular_promedio():
    # Solicitamos que se ingresen números separados por espacios
    numeros = input("Ingresa una serie de números separados por espacios: ")
    
    # Convertimos los números ingresados en una lista de enteros
    lista_numeros = [int(numero) for numero in numeros.split()]
    
    # Calculamos el promedio
    promedio = sum(lista_numeros) / len(lista_numeros) if len(lista_numeros) > 0 else 0
    
    # Mostramos el promedio
    print(f"El promedio es: {promedio}")

calcular_promedio()