#!/usr/bin/env python3
from gerador_senha import *


def exibir_menu():
    print("\n=== Menu Principal ===")
    print("[1] Gerador de senhas aleatórias")
    print("[2] Gerador de senhas condicionais")
    print("[3] Gerador de wordlist")
    print("[4] Gerador de wordlist condicional")
    print("[5] Sair")


def opcao_invalida():
    print("\033[91m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Opção inválida!")
    print("Escolha uma entre as cinco opções permitidas!\033[0m")


def main():
    repetir = True

    while repetir:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

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
            opcao_invalida()

        print()  # Adiciona uma linha em branco para separar as execuções

    print("Encerrando o programa.")


if __name__ == "__main__":
    main()
