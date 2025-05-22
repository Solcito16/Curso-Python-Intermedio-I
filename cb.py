#Se debe modificar la clase CuentaBancaria para que sea abstracta, además los métodos extraer y 
#depositar deben volverse abstractos, también se debe crear una clase CuentaAhorro
#que herede de CuentaBancaria y se le agregue un atributo privado de tasa de interes,
#el cual tendra un valor establecido de 0.001 y un método que nos calcule el interes


from abc import ABC , abstractmethod
from datetime import date, datetime


class CuentaBancaria(ABC):  
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular
        self._dni_titular = dni_titular
        self._fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y/%m/%d').date()
        self._saldo = saldo  

    @abstractmethod
    def extraer(self, monto):
        pass

    @abstractmethod
    def depositar(self, monto):
        pass

    def obtener_saldo(self):
        return self._saldo

    def _calcular_edad(self):  # Corrección de nombre
        return (date.today() - self._fecha_nacimiento).days // 365

    def obtener_edad(self):
        return self._calcular_edad()
    
    def mostrar_nombre(self):
        return self._nombre_titular

    def cambiar_nombre(self, n):
        self._nombre_titular = n
