#Escribe un programa que intente acceder a una clave que no existe en un
#diccionario. Si se produce una excepción KeyError, captura la excepción y muestra


try:
    # Creo un diccionario
    mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
    
    # Solicito al usuario que ingrese la clave para ingresar
    clave = input("Ingrese la clave que desea buscar: ")
    
    valor = mi_diccionario[clave]
    
    # Muestro el valor obtenido
    print(f"El valor de la clave '{clave}' es: {valor}")
except KeyError:
    print(f"Error: La clave '{clave}' no existe en el diccionario.")