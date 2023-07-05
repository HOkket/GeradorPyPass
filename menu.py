#!/bin/python3
import importlib
import Gerador_de_senha


print("[1] Gerador de senhas aleatorias")
print("[2] Gerador de senhas codicionais")
print("[3] Gerador de wordlist")
opcao = int(input())

if opcao == 1:
    modulo = importlib.import_module('senhas_aleatoria')
    modulo.executar()
elif opcao == 2:
    modulo = importlib.import_module('senha_direcionada')
    modulo.executar()
else:
    print("Opção invalida!")