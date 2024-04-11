menu = """

[d] depositar
[s] sacar
[e] extrato 
[nu] novo usuario
[nc] nova conta
[ec] exibir contas
[q] sair
    
==> """

LIMITE_SAQUES = 3
NUMERO_AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
clientes = []
contas = []

def criar_usuario(clientes):
    cpf = input("Informe seu cpf (somente numeros): ")
    
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("CPF já cadastrado")
            return

    else:
        nome = input("Informe seu nome: ")
        data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
        endereco = input("Informe seu endereço: ")
            
        clientes.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        return clientes

def criar_conta(numero_conta, clientes):
    cpf = input("Informe seu cpf (somente numeros): ")
    
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            contas.append({"numero_conta": numero_conta,"numero_agencia": NUMERO_AGENCIA, "usuario":cliente })
            return contas
    else: 
        print("CPF não cadastrado")
        return
    
def depositar(saldo,valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Deposito de R${valor:.2f}\n"
    else:
        print("O valor informado é inválido.")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    if numero_saques == limite_saques:
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
        
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    if extrato == "":
        print("Não foram realizadas movimentações")
    else:
        print(f"\n=========== EXTRATO ===========\n\n{extrato}")
        print(f"Saldo: R$ {saldo:.2f}")
        print("\n======================")
        
def exibir_contas(contas):
    if contas == []:
        print("Não há contas cadastradas")
        
    else:
        for conta in contas:
            print("\n=========== CONTAS =============")
            print(f"\nAgência: {conta["numero_agencia"]}\nConta corrente: {conta["numero_conta"]}\nTitular: {conta["usuario"]["nome"]}")
        
while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Qual o valor que você deseja depositar? "))
          
        saldo, extrato = depositar(saldo, valor, extrato)
        
    elif opcao == "s":
        valor = float(input("Informe o valor do seu saque: "))
        
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    
    elif opcao == "nu":
        criar_usuario(clientes)
        
    elif opcao == "nc":
        numero_conta = len(contas) + 1
        criar_conta(numero_conta, clientes)
        
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
        
    elif opcao == "ec":
        exibir_contas(contas)
        
    elif opcao == "q":
        break
     
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada")