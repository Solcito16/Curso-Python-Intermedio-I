
from cb import CuentaBancaria # se puede poner un as y darle un nombre temporal
from cc import CuentaCorriente
from ca import CuentaAhorro # type: ignore

# Crear cuenta de ahorro
cuenta_ahorro = CuentaAhorro("Ana Gómez", "87654321", "1995/03/15", saldo=5000)

# Prueba de métodos
#cuenta_ahorro.depositar(1000)
#print(f"Interés generado: {cuenta_ahorro.calcular_interes()}")

cuenta_corriente = CuentaCorriente("Juan Pérez", "12345678", "1990/05/20", saldo=1000)

cuenta_corriente.extraer(300)
#cuenta_ahorro.depositar(1000)
print(f"Nombre del titular: {cuenta_ahorro.mostrar_nombre()}")
print(f"Nombre del titular: {cuenta_corriente.mostrar_nombre()}")
#print(f"Interés generado: {cuenta_ahorro.calcular_interes()}")

