#Ejercicio 2
#Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario

def buscar_palabra(palabra, *args):
    # Utilizamos el operador ternario para verificar si la palabra está en la lista
    resultado = "Encontrada" if palabra in args else "No encontrada"
    return resultado

# Solicitamos una lista y la palabra a buscar en ella al usuario
lista = input("Ingrese palabras separadas por espacios: ").split()
palabra_a_buscar = input("Ingrese la palabra a buscar: ")

# Mostramos el resultado en pantalla
print(buscar_palabra(palabra_a_buscar, *lista))