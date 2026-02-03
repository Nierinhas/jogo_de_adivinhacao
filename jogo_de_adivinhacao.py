import random

while True:

    print("\nBem vindo ao jogo de adivinhação!")
    print("1 - Fácil - Números de 1 a 10, 3 tentativas.")
    print("2 - Médio - Números de 1 a 20, 5 tentativas.")
    print("3 - Difícil - Números de 1 a 50, 5 tentativas.")
    dificuldade = input("Escolha uma dificuldade: ")

    if dificuldade == "1":
        max_numero = 10
        max_tentativas = 3
    elif dificuldade == "2":
        max_numero = 20
        max_tentativas = 5
    elif dificuldade == "3":
        max_numero = 50
        max_tentativas = 5
    else:
        print("Comando inválido.")
        continue  # volta pro menu inicial

    numero_secreto = random.randint(1, max_numero)

    tentativas = []
    acertou = False

    while len(tentativas) < max_tentativas:
        tentativa_atual = len(tentativas) + 1

        try:
            chute = int(input(
                f"Tentativa {tentativa_atual} de {max_tentativas} - digite um número de 1 a {max_numero}: "
            ))
        except:
            print("Digite apenas números.")
            continue

        if chute < 1 or chute > max_numero:
            print(f"Apenas números de 1 a {max_numero}!")
            continue

        tentativas.append(chute)

        if chute > numero_secreto:
            print("Muito alto!")
        elif chute < numero_secreto:
            print("Muito baixo")
        else:
            print("Acertou!")
            acertou = True
            break

        print("-----------")

    if acertou:
        print("Parabéns!")
    else:
        print(f"Você perdeu! O número era {numero_secreto}.")

    print(f"Tentativas: {tentativas}")
    print(f"Quantidade de tentativas: {len(tentativas)}")

    novamente = input("Jogar novamente? (s/n): ").lower().strip()

    if novamente == "s":
        continue
    elif novamente == "n":
        print("Encerrando.")
        break
    else:
        print("Comando inválido.")
        break
