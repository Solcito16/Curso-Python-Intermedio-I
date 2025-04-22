#Ejercicio 5
#Imprimir un mensaje de error si no se pasan suficientes argumentos

def verificar_argumentos():
    # Solicitamos que se ingresen los argumentos separados por espacios
    argumentos = input("Ingresa los argumentos separados por espacios: ")
    
    # Convertimos la entrada en una lista de argumentos
    lista_argumentos = argumentos.split()
    
    # Verificamos si se han ingresado argumentos
    if len(lista_argumentos) <= 3:
        print("Error: No se han ingresado suficientes argumentos.")
    else:
        print(f"Se recibieron {len(lista_argumentos)} argumentos: {lista_argumentos}")

verificar_argumentos()