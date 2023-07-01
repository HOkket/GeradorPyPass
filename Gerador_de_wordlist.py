#!/bin/python3S
import random

tamanho = int(input("Tamanho da senha: "))
quantidade = int(input("Quantas senhas você deseja gerar? "))
arquivo = open('wordlist.txt', 'a')  # Abrir o arquivo no modo de adição
contagem = 0

for i in range(quantidade):
    ALFA = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
    alfa = "qwertyuiopasdfghjklçzxcvbnm"
    numeros = "1234567890"
    especial = "!@#$%¨&*()?/}]{[+="
    Estrutura = ALFA + alfa + numeros + especial
    senha = "".join(random.sample(Estrutura, tamanho))
    print(senha, file=arquivo)  # Salvar a senha no arquivo
    i += 1
    contagem += 1
    porcentagem = (contagem / quantidade) * 100
    print("(", porcentagem, "%", ")")

arquivo.close()  # Fechar o arquivo fora do loop
print("Finalizado")
