from gerador_senha import *

repetir = True

while repetir:
    print("[1] Gerador de senhas aleatórias")
    print("[2] Gerador de senhas condicionais")
    print("[3] Gerador de wordlist")
    print("[4] Gerador de wordlist condicional")
    print("[5] Sair")
    opcao = str(input("Escolha uma opção: "))

    if opcao == "1":
        senha_aleatoria()
    elif opcao == "2":
        senha_direcionada()
    elif opcao == "3":
        gerador_wordlist()
    elif opcao == "4":
        gerador_wordlist_direcionada()
    elif opcao == "5":
        repetir = False
    else:
        print("\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Opção inválida!")
        print("Escolha uma entre as cinco opçoes permitidas!\033[0m")

    print()  # Adiciona uma linha em branco para separar as execuções

print("Encerrando o programa.")
