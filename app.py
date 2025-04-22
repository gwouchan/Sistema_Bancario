menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
mensagem_erro = 'Valor inválido. Tente novamente.'

while True:
    opcao = input(menu).lower()

    if opcao == 'd':
        while True:
            try:
                valor_deposito = float(input('Digite o valor do depósito: R$ '))
            except ValueError:
                print(mensagem_erro)
                continue

            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f'Depósito: R$ {valor_deposito:.2f}\n'

                print(f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso!')
                break

            else:
                print(mensagem_erro)
                continue
                 

    elif opcao == 's':
        while True:
            try:
                valor_saque = float(input('Digite o valor para saque (limite R$500,00 por saque): R$ '))
            except ValueError:
                print(mensagem_erro)
                continue

            if valor_saque <= 0:
                print(mensagem_erro)
                continue

            elif numero_saques == LIMITE_SAQUES:
                print('Limite diário de saque atingido. Você pode sacar até três vezes.')
                break

            elif valor_saque > saldo:
                print('Você não possui saldo eficiente para realizar o saque')
                print(f'Saldo atual: R$ {saldo:.2f}')
                continue

            elif valor_saque > limite:
                print('Limite R$500,00 por saque, tente um valor menor.')
                continue
            
            saldo -= valor_saque
            extrato += f'Saque: -R$ {valor_saque:.2f}\n'
            numero_saques += 1
            break
    
    elif opcao == 'e':
        print(' EXTRATO '.center(40,'='))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=".center(40,'='))
    
    elif opcao == 'q':
        print('Sistema finalizado.')
        break

    else:
        print('Opção inválda. Tente novamente.')