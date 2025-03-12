class ContaBancaria:
    def __init__(self, titular, saldo, cpf, cep, chavePix):
        self.titular = titular
        self.__saldo = saldo
        self.__cpf = cpf
        self.cep = cep
        self.__chavePix = chavePix

    def exibir_saldo(self):
        print(f'Saldo atual do cpf {self.__cpf}: \n R$ {self.__saldo}')

    def receber_pix(self, valor) :
        self.__saldo += valor

    def enviar_pix(self, valor):

        self.__chavePix = int(input('Digite a chave pix: \n'))

        if valor <= self.__saldo:
            print('Pix enviado!')
            self.__saldo -= valor
        else:
            print(f'Saldo insuficiente')