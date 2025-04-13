import random


def senha_aleatoria():
    try:
        tamanho = int(input("Tamanho da senha: "))
        if tamanho < 4:
            print(
                "O tamanho da senha deve ser pelo menos 4 para incluir todos os tipos de caracteres.")
            return
        ALFA = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
        alfa = "qwertyuiopasdfghjklçzxcvbnm"
        numeros = "1234567890"
        especial = "!@#$%¨&*()?/}]{[+="
        Estrutura = ALFA + alfa + numeros + especial

        # Garantir pelo menos um caractere de cada tipo
        senha = [
            random.choice(ALFA),
            random.choice(alfa),
            random.choice(numeros),
            random.choice(especial)
        ]

        # Preencher o restante da senha
        senha += random.choices(Estrutura, k=tamanho - 4)

        # Embaralhar os caracteres para evitar padrões previsíveis
        random.shuffle(senha)

        # Converter a lista em uma string
        senha = "".join(senha)

        print("Senha gerada com sucesso!")
        print("Senha: ", senha)
    except ValueError:
        print("Por favor, insira um número válido para o tamanho da senha.")


def senha_direcionada():
    try:
        tamanho = int(input("Tamanho da senha: "))
        if tamanho < 4:
            print(
                "O tamanho da senha deve ser pelo menos 4 para incluir todos os tipos de caracteres.")
            return

        PRIMEIRA_CHAVE = input("Insira a primeira palavra chave: ").strip()
        SEGUNDA_CHAVE = input("Insira a segunda palavra chave: ").strip()
        numeros = input(
            "Insira os caracteres especiais ou números (opcional): ").strip()

        if not PRIMEIRA_CHAVE or not SEGUNDA_CHAVE:
            print("As palavras-chave não podem estar vazias.")
            return

        Estrutura = PRIMEIRA_CHAVE + SEGUNDA_CHAVE + numeros

        # Garantir que a estrutura tenha caracteres suficientes
        if len(Estrutura) < tamanho:
            print("A combinação das palavras-chave e caracteres adicionais deve ser maior ou igual ao tamanho da senha.")
            return

        # Gerar a senha embaralhando os caracteres
        senha = "".join(random.sample(Estrutura, tamanho))

        print("Senha gerada com sucesso!")
        print("Senha: ", senha)
    except ValueError:
        print("Por favor, insira um número válido para o tamanho da senha.")


def gerador_wordlist():
    try:
        tamanho = int(input("Tamanho da senha: "))
        quantidade = int(input("Quantas senhas você deseja gerar? "))
        if tamanho < 4:
            print(
                "O tamanho da senha deve ser pelo menos 4 para incluir todos os tipos de caracteres.")
            return

        ALFA = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
        alfa = "qwertyuiopasdfghjklçzxcvbnm"
        numeros = "1234567890"
        especial = "!@#$%¨&*()?/}]{[+="
        Estrutura = ALFA + alfa + numeros + especial

        # Abrir o arquivo no modo de escrita para garantir que o conteúdo seja limpo
        with open('wordlist.txt', 'w') as arquivo:
            contagem = 0
            for i in range(quantidade):
                # Garantir pelo menos um caractere de cada tipo
                senha = [
                    random.choice(ALFA),
                    random.choice(alfa),
                    random.choice(numeros),
                    random.choice(especial)
                ]

                # Preencher o restante da senha
                senha += random.choices(Estrutura, k=tamanho - 4)

                # Embaralhar os caracteres para evitar padrões previsíveis
                random.shuffle(senha)

                # Converter a lista em uma string
                senha = "".join(senha)

                # Salvar a senha no arquivo
                print(senha, file=arquivo)

                contagem += 1
                porcentagem = (contagem / quantidade) * 100
                print("({:.2f}%)".format(porcentagem))

        print("Wordlist Finalizada")
    except ValueError:
        print("Por favor, insira valores válidos para o tamanho e a quantidade de senhas.")


def gerador_wordlist_direcionada():
    try:
        tamanho = int(input("Tamanho da senha: "))
        quantidade = int(input("Quantas senhas você deseja gerar? "))
        Nome = input("Nome do alvo: ").strip()
        Sobrenome = input("Sobrenome do alvo: ").strip()
        Data = input("Data de nascimento (apenas números): ").strip()
        especial = input("Informação adicional (opcional): ").strip()

        if not Nome or not Sobrenome or not Data:
            print("Nome, Sobrenome e Data de nascimento são obrigatórios.")
            return

        if tamanho < 4:
            print(
                "O tamanho da senha deve ser pelo menos 4 para incluir todos os tipos de caracteres.")
            return

        Estrutura = Nome + Sobrenome + Data + especial

        # Garantir que a estrutura tenha caracteres suficientes
        if len(Estrutura) < tamanho:
            print(
                "A combinação das informações fornecidas deve ser maior ou igual ao tamanho da senha.")
            return

        contagem = 0
        with open('wordlist.txt', 'a') as arquivo:
            for i in range(quantidade):
                # Gerar a senha embaralhando os caracteres
                senha = "".join(random.sample(Estrutura, tamanho))

                # Salvar a senha no arquivo
                print(senha, file=arquivo)

                contagem += 1
                porcentagem = (contagem / quantidade) * 100
                print("({:.2f}%)".format(porcentagem))

        print("Wordlist Finalizada")
    except ValueError:
        print("Por favor, insira valores válidos para o tamanho, quantidade e data de nascimento.")
