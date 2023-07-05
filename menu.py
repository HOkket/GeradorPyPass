#!/bin/python3
import importlib
import gerador_de_senhas

print("Gerador de senhas aleatorias")
print("Gerador de senhas codicionais")
opcao = int(input())

if opcao == 1:
    modulo = importlib.gera('senhas_aleatoria')
    modulo.executar()
elif opcao == 2:
    modulo = importlib.import_module('senha_direcionada')
    modulo.executar()
else:
    print("Opção invalida!")