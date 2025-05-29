import random

n = random.randint(1, 10)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe o número de 1 a 10: "))
    tentativas += 1
    if tentativa == n:
        print(f"Acertou em {tentativas} tentativas!")
        break
    elif tentativa < n:
        print("Muito baixo.")
    else:
        print("Muito alto.")
