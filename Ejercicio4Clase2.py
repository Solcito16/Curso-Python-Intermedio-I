#un mensaje de error al usuario.
#Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
#FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
#embargo, también intenta crear el archivo si no existe.


try:
    # Intento abrir un archivo que no existe
    archivo_sol = "archivo_inexistente.txt"
    with open(archivo_sol, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print(f"Error: El archivo '{archivo_sol}' no existe.")
    print("Creando el archivo...")
    
    # Crear el archivo
    with open(archivo_sol, "w") as archivo:
        archivo.write("Este es un archivo recién creado.\n")
    print(f"El archivo '{archivo_sol}' ha sido creado exitosamente.")