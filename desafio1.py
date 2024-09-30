menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: #Primeiro estamos vendo o depósito.


    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: ")) #pergunta para o usuario qual é o valor que vai depositar

        if valor > 0: #se o valor é maior que 0
            saldo += valor  #sendo maior que 0, adiciona o valor no saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  #concatetamos a string deposito, com duas casas decimais

        else: #se caso o valor não seja maior que 0, é enviado essa mensagem para o usuario
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: ")) #Pergunta valor do saque

        excedeu_saldo = valor > saldo #para varificar se excdeu o saldo

        excedeu_limite = valor > limite #para varificar se excdeu o limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES #para varificar se o usuario ja fez os 3 saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")