from datetime import datetime

class Banco:

    def __init__(self):
        self.__saldo = 0

    def horario(self):
        data = datetime.now().strftime('%H:%M dia: %d/%m/%Y')
        return data

    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return self.__saldo
        else:
            print('Saldo Insuficiente!\n')

    @property
    def dados(self):
        print(f'Seu saldo: R${self.__saldo}')
        print(f'Horário da transação {self.horario()}\n')