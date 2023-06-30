import random

tamanho = int(input("Tamanho da senha: "))
ALFA = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
alfa = "qwertyuiopasdfghjklçzxcvbnm"
numeros = "1234567890"
especial = "!@#$%¨&*()?/}]{[+="
Estrutura = ALFA + alfa + numeros + especial
senha = "".join(random.sample(Estrutura,tamanho))
print(senha)