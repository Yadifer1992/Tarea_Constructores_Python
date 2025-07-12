# cuenta_bancaria.py

# Clase CuentaBancaria con constructor y destructor

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        """
        Constructor: se ejecuta al crear una nueva cuenta bancaria.
        Inicializa el nombre del titular y el saldo.
        """
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"🏦 Cuenta creada para {self.titular} con saldo inicial de ${self.saldo:.2f}")

    def depositar(self, monto):
        """
        Método para depositar dinero en la cuenta.
        """
        self.saldo += monto
        print(f"💰 Depósito de ${monto:.2f} realizado. Saldo actual: ${self.saldo:.2f}")

    def retirar(self, monto):
        """
        Método para retirar dinero de la cuenta.
        Verifica si hay suficiente saldo disponible.
        """
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"💸 Retiro de ${monto:.2f} realizado. Saldo actual: ${self.saldo:.2f}")
        else:
            print("❌ Fondos insuficientes.")

    def __del__(self):
        """
        Destructor: se ejecuta cuando se elimina la cuenta.
        Puede usarse para limpiar recursos o mostrar un mensaje.
        """
        print(f"📴 La cuenta de {self.titular} ha sido cerrada.")

# Ejemplo de uso:
cuenta1 = CuentaBancaria("Ana Torres", 150.00)
cuenta1.depositar(50.00)
cuenta1.retirar(30.00)

# Eliminar manualmente para activar el destructor:
del cuenta1