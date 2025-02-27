menu = """
Escolha uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0;
limite = 500;
extrato = ""
numero_saques = 0;
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor;
            extrato += f"Depósito: R${valor: .2f}\n"
        else:
            print("O valor informado é inválido. Tente novamente.")


    elif opcao == "2":
        valor = float(input("Informe o valor de saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente.")

        elif excedeu_limite:
            print(f'O valor excede o limite de {limite}. Tente outro valor.')
        
        elif excedeu_saques:
            print("Você já fez os 3 saques diários, tente novamente amanhã.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor: .2f}\n"
            numero_saques += 1
        
        else:
            print("O valor informado é invalido. Tente novamente.")
    

    elif opcao == "3":

        print("\n=================== EXTRATO ===================")
        print("Não foram realizadas transações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo: .2f}\n")
        print(f'Restam {LIMITE_SAQUES - numero_saques} saques diários.')
    
    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços.")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação.")