#Ejercicio1
#Calcular el mayor de dos números ingresados por teclado usando un operador ternario

#Pedimos que se ingresen dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calculamos el mayor
mayor = num1 if num1 > num2 else num2

# Mostramos el resultado
print(f"El mayor de los dos números es: {mayor}")