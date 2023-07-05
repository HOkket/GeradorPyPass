#!/bin/python3
from typing import Match
from gerador_senha import senha_aleatoria, senha_direcionada, gerador_wordlist


print("[1] Gerador de senhas aleatorias")
print("[2] Gerador de senhas codicionais")
print("[3] Gerador de wordlist")
opcao = int(input())

if opcao == 1:
    senha_aleatoria()
elif opcao == 2:
    senha_direcionada()
elif opcao == 3:
    gerador_wordlist()
else:
    print("Opção invalida!")