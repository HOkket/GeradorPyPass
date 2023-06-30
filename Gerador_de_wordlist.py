import random

tamanho = int(input("Tamanho da senha: "))
quantidade = int(input("Quantas senhas você deseja gerar? "))

arquivo = open('wordlist.txt', 'a')  # Abrir o arquivo no modo de adição

for i in range(quantidade):
    ALFA = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
    alfa = "qwertyuiopasdfghjklçzxcvbnm"
    numeros = "1234567890"
    especial = "!@#$%¨&*()?/}]{[+="
    Estrutura = ALFA + alfa + numeros + especial
    senha = "".join(random.sample(Estrutura, tamanho))
    print(senha, file=arquivo)  # Salvar a senha no arquivo
    quantidade += 1

arquivo.close()  # Fechar o arquivo fora do loop
print("Finalizado")
