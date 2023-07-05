import random


def senha_aleatoria():
    if __name__ == "__main__":
        tamanho = int(input("Tamanho da senha: "))
        ALFA = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
        alfa = "qwertyuiopasdfghjklçzxcvbnm"
        numeros = "1234567890"
        especial = "!@#$%¨&*()?/}]{[+="
        Estrutura = ALFA + alfa + numeros + especial
        senha = "".join(random.sample(Estrutura, tamanho))
        return senha


def senha_direcionada():
    if __name__ == "__main__":
        tamanho = int(input("Tamanho da senha: "))
        PRIMEIRA_CHAVE = input("Insira a primeira palavra chave: ")
        SEGUNDA_CHAVE = input("Insira a segunda palavra chave: ")
        numeros = input(
            "Insira os caracteres especiais ou números (opcional): ")
        Estrutura = PRIMEIRA_CHAVE + SEGUNDA_CHAVE + numeros
        senha = "".join(random.sample(Estrutura, tamanho))
        return senha


def gerador_wordlist():
    if __name__ == "__main__":
        tamanho = int(input("Tamanho da senha: "))
        quantidade = int(input("Quantas senhas você deseja gerar? "))
        # Abrir o arquivo no modo de adição
        arquivo = open('wordlist.txt', 'a')
        contagem = 0
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
        print("Finalizado")
