#!/bin/python3
import random

print("1 - Gerador aleatorio de senhas")
print("2 - Gerador de senhas direcionado")
MODO = int(input("Escolha o modo de gerarar suas senha: "))

if MODO == 1:
    tamanho = int(input("Tamanho da senha: "))
    ALFA = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
    alfa = "qwertyuiopasdfghjklçzxcvbnm"
    numeros = "1234567890"
    especial = "!@#$%¨&*()?/}]{[+="
    Estrutura = ALFA + alfa + numeros + especial
    senha = "".join(random.sample(Estrutura,tamanho))
    print(senha)
elif MODO == 2:
    tamanho = int(input("Tamanho da senha: "))
    PRIMEIRA_CHAVE = str(input("Isira a primeira palavra chave: "))
    SEGUNDA_CHAVE = str(input("Isira a segunda palavra chave: "))
    numeros = input("Insira os caracteres especiais ou numeros (opcional): ")
    Estrutura = PRIMEIRA_CHAVE + SEGUNDA_CHAVE + numeros
    senha = "".join(random.sample(Estrutura,tamanho))
    print(senha)
