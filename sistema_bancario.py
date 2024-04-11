menu = """

[d] depositar
[s] sacar
[e] extrato 
[q] sair
    
==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Qual o valor que você deseja depositar? "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R${valor:.2f}\n"
        else:
            print("O valor informado é inválido.")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do seu saque: "))
        
        if numero_saques == LIMITE_SAQUES:
            print("Numero de saques excedidos")
        elif valor > saldo:
            print("Saldo insuficiente")
        elif valor > limite:
            print("Limite excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("O valor informado é inválido.")
        
    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações")
        else:
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
        
    elif opcao == "q":
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada")