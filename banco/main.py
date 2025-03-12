from conta_bancaria import ContaBancaria

cc1 = ContaBancaria(titular='Francisco', saldo=400, cpf='473.847.458-88', cep='13.426-269', chavePix=0)



print(f'A conta do cliente {cc1.titular},cep: {cc1.cep} está aberta')

cc1.exibir_saldo()

cc1.receber_pix(valor=100)
cc1.exibir_saldo()

cc1.enviar_pix(valor=int(input('Digite qual o valor que deseja enviar:\n')))

cc1.exibir_saldo()