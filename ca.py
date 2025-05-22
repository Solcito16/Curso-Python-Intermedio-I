from cb import CuentaBancaria


class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self.__tasa_interes = 0.001  # Atributo privado de tasa de interés
        

    def calcular_interes(self):
        return self.obtener_saldo() * self.__tasa_interes

    def extraer(self, monto):
        if monto <= self.obtener_saldo():
            self._saldo -= monto
            print(f"Se ha extraído {monto}. Saldo actual: {self.obtener_saldo()}")
        else:
            print("No posee saldo suficiente.")

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto}. Saldo actual: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser mayor a 0.")