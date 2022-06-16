from Models.banco import Banco

caixa = Banco()
retorno = 0

while retorno != True:
    print('Digite ação desejada:[1]Extrato,[2]Sacar,[3]Depositar, [4]Sair')
    entrada = int(input('Sua escolha: '))
    if entrada < 0 or entrada > 5:
        print('Opção inválida')

    if entrada == 1:
        caixa.dados

    if entrada == 2:
        valor = int(input('Digite valor: R$'))
        caixa.sacar(valor)
        caixa.horario
        caixa.dados

    if entrada == 3:
        valor = int(input('Digite valor: R$'))
        caixa.depositar(valor)
        caixa.dados
    
    if entrada == 4:
        print('Obrigado por usar nossos serviços')
        retorno = True