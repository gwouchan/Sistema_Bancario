def menu():
    text_menu = '''\n
    1 - Depositar
    2 - Sacar
    3 - Extrato
    4 - Nova Conta
    5 - Listar contas
    6 - Novo usuário
    0 - Sair
    → '''

    try:
        option = int(input(text_menu))
        if 0 <= option <= 6:
            return option
        else:
            print(f'\nDigite um número entre 0 e 6.')
            return menu()
    except ValueError:
        print(f'\nValor inválido. Tente digitar somente os números entre 0 e 6.')
        return menu()


def deposit(balance, amount, extract, /):
    if amount > 0:
        balance += amount
        extract += f'Depósito: R$ {amount:.2f}\n'
        print(f'\n»»» Depósito realizado com sucesso! «««')
    else: 
        print(f'\n✕✕✕ Operação falhou! O valor informado é inválido. ✕✕✕')
    
    return balance, extract

def withdraw(*, balance, amount, extract, limit, number_withdraw, limit_withdraw):
    balance_exceeded = amount > balance
    limit_exceeded = amount > limit
    withdraw_exceeded = number_withdraw >= limit_withdraw

    if balance_exceeded:
        print(f'\n✕✕✕ Operação falhou! Você não possui saldo suficiente. ✕✕✕')
    elif limit_exceeded:
        print(f'\n✕✕✕ Operação falhou! O valor do saque excede o limite. ✕✕✕')
    elif withdraw_exceeded:
        print(f'\n✕✕✕ Operação falhou! Número máximo de saques excedido. ✕✕✕')

    elif amount > 0:
        balance -= amount
        extract += f'Saque: R$ {amount:.2f}\n'
        number_withdraw += 1
        print(f'\n»»» Saque realizado com sucesso! «««')
    else:
        print(f'\n✕✕✕ Operação falhou! O valor informado é inválido. ✕✕✕')
    
    return balance, extract

def display_extract(balance,/,*,extract):
    print(f'\n▪▪▪▪▪▪▪▪▪▪ EXTRATO ▪▪▪▪▪▪▪▪▪▪')
    print(f'Não foram encontradas movimentações' if not extract else extract)
    print(f'\nSaldo: R$ {balance:.2f}')
    print('▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪')

def register_user(users):
    cpf = input('Informe o CPF (somente números): ')
    user = filter_user(cpf,users)

    if user:
        print(f'\n✕✕✕ Já existe um usuário com este CPF! ✕✕✕')
        return
    
    name = input('Informe o nome: ')
    date_bird = input('Informe sua data de nascimento (dd-mm-aaaa): ')
    address = input('Informe o endereço (logradouro, nº - bairro - município/UF): ')

    users.append({'name': name, 'date_bird': date_bird,'cpf': cpf, 'address': address})

    print(f'\n»»» Usuário criado com sucesso! «««')

def filter_user(cpf, users):
    filters_users = [user for user in users if user['cpf'] == cpf]
    return filters_users[0] if filters_users else None

  
def main():
    LIMIT_WITHDRAW = 3
    AGENCY = "0001"

    balance = 0
    limit = 500
    extract = ""
    number_withdraw = 0
    users = []
    accounts = []

    while True:
        option = menu()

        match option:
            case 1: #deposito
                amount = float(input(f'\nDigite o valor do depósito: R$ '))

                balance, extract = deposit(balance, amount, extract)
                ...
            case 2: #saque
                amount = float(input(f'\nDigite o valor do saque: R$ '))

                balance, extract = withdraw(
                    balance = balance,
                    amount = amount,
                    extract = extract,
                    limit = limit,
                    number_withdraw = number_withdraw,
                    limit_withdraw = LIMIT_WITHDRAW
                    )

            case 3: #extrato
                display_extract(balance, extract=extract)
            case 4:
                ...
            case 5:
                ...
            case 6:
                ...
            case 0:
                ...
            case _:
                ...

main()