1. Tarea: Constructores y Destructores en Python

Este proyecto consiste en la implementación de una clase en Python que utiliza los conceptos de **programación orientada a objetos (POO)**, específicamente los **constructores** y **destructores**.

2. Objetivo:

Aplicar los fundamentos de la programación orientada a objetos mediante el uso de:

- Constructor `__init__`
- Destructor `__del__`
- Atributos de instancia
- Métodos definidos por el usuario

3. Descripción del programa:

Se desarrolló una clase llamada `CuentaBancaria` que permite simular una cuenta de banco. Al crear un objeto de esta clase, se inicializa con el nombre del titular y el saldo inicial. Además, se pueden realizar operaciones de **depósito** y **retiro**.

El destructor muestra un mensaje cuando se elimina la cuenta (simulando el cierre de una cuenta bancaria).


4. Estructura del código:

```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"Cuenta creada para {self.titular} con ${self.saldo}")

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes")

    def __del__(self):
        print(f"La cuenta de {self.titular} ha sido cerrada.")
