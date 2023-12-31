import random


def senha_aleatoria():
    tamanho = int(input("Tamanho da senha: "))
    ALFA = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
    alfa = "qwertyuiopasdfghjklçzxcvbnm"
    numeros = "1234567890"
    especial = "!@#$%¨&*()?/}]{[+="
    Estrutura = ALFA + alfa + numeros + especial
    senha = "".join(random.sample(Estrutura, tamanho))
    print("Senha gerada com secesso!")
    print("Senha: ", senha)


def senha_direcionada():
    tamanho = int(input("Tamanho da senha: "))
    PRIMEIRA_CHAVE = input("Insira a primeira palavra chave: ")
    SEGUNDA_CHAVE = input("Insira a segunda palavra chave: ")
    numeros = input("Insira os caracteres especiais ou números (opcional): ")
    Estrutura = PRIMEIRA_CHAVE + SEGUNDA_CHAVE + numeros
    senha = "".join(random.sample(Estrutura, tamanho))
    print("Senha gerada com secesso!")
    print("Senha: ", senha)


def gerador_wordlist():
    tamanho = int(input("Tamanho da senha: "))
    quantidade = int(input("Quantas senhas você deseja gerar? "))
    # Abrir o arquivo no modo de adição
    arquivo = open('wordlist.txt', 'a')
    contagem = 0
    with open('wordlist.txt') as wdlist:
        for i in range(quantidade):
            ALFA = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
            alfa = "qwertyuiopasdfghjklçzxcvbnm"
            numeros = "1234567890"
            especial = "!@#$%¨&*()?/}]{[+="
            Estrutura = ALFA + alfa + numeros + especial
            senha = "".join(random.sample(Estrutura, tamanho))
            print(senha, file=arquivo)  # Salvar a senha no arquivo
            contagem += 1
            porcentagem = (contagem / quantidade) * 100
            print("({:.2f}%)".format(porcentagem))
    arquivo.close()  # Fechar o arquivo fora do loop
    print("Wordlist Finalizada")


def gerador_wordlist_direcionada():
    tamanho = int(input("Tamanho da senha: "))
    quantidade = int(input("Quantas senhas você deseja gerar? "))
    contagem = 0
    Nome = str(input("Nome do alvo: "))
    Sobrenome = str(input("Sobrenome do avlo: "))
    Data = int(input("Data de nascimento: "))
    especial = input("Informação adicional: ")
    # Abrir o arquivo no modo de adição
    arquivo = open('wordlist.txt', 'a')
    for i in range(quantidade):
        Estrutura = Nome + Sobrenome + Data + especial
        senha = "".join(random.sample(Estrutura, tamanho))
        print(senha, file=arquivo)  # Salvar a senha no arquivo
        contagem += 1
        porcentagem = (contagem / quantidade) * 100
        print("({:.2f}%)".format(porcentagem))
    arquivo.close()  # Fechar o arquivo fora do loop
    print("Wordlist Finalizada")
