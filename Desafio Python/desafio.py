import textwrap

def menu():    
    menu = """\n
    *******Barra de Navegação*******
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor: .2f}\n"
        print("\n ### Depósito realizado com sucesso! ###")
    else
        print("\n ||| Operação falhou! Tente novamente. |||")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, nrSaques, qutSaques):
    semSaldo = valor > saldo
    excedeuLimite = valor > limite
    excedeuSaques = nrSaques >= qutSaques

    if semSaldo:
        print("\n||| Operação falhou! Você não tem saldo suficiente. |||")

    elif excedeuLimite:
        print("\n||| Operação falhou! O valor do saque excede o limite. |||")

    elif excedeuSaques:
        print("\n||| Operação falhou! Número máximo de saques excedido. |||")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        nrSaques += 1
        print("\n### Saque realizado com sucesso! ###")

    else:
        print("\n||| Operação falhou! O valor informado é inválido. |||")

    return saldo, extrato

def mostrarExtrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def principal():
    saldo = 0
    limite = 500
    extrato = ""
    nrSaques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                nrSaques=nrSaques,
                qutSaques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
