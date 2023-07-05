from gerador_senha import *


print("[1] Gerador de senhas aleatorias")
print("[2] Gerador de senhas codicionais")
print("[3] Gerador de wordlist")
print("[4] Gerador de wordlist condicional")
opcao = int(input())

if opcao == 1:
    senha_aleatoria()
elif opcao == 2:
    senha_direcionada()
elif opcao == 3:
    gerador_wordlist()
elif opcao == 4:
    gerador_wordlist_direcionada()
else:
    print("Opção invalida!")
