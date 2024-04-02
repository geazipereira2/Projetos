import random

print(f"\nBem vindo ao jogo de pedra, papel e tesoura. Siga as instruções abaixo para jogar:\n")

user_points = 0
computer_points = 0

options = ["r", "t", "p"]

while True:
    user_choice = input(f"\nR para Pedra\nT para Tesoura\nP para Papel\nou Q para Sair:\n\nSua escolha: ").lower() #Esse lower transforma MAIUSCULAS em minusculas.

    if user_choice == 'q':
        break

    if user_choice not in options:
        continue

    computer_choice = random.randint(0, 2)
    # 0 para R (Pedra);
    # 1 para T (Tesoura);
    # 2 para Q (Papel).
    computer_option = options[computer_choice]

    print("Escolha do Computador: " + computer_option)

    if user_choice == computer_option:
        print(f"\nEmpate!")
    elif user_choice == "r" and computer_option == "t":
        print(f"\nVocê ganhou!")
        user_points = user_points + 1
    elif user_choice == "t" and computer_option == "p":
        print(f"\nVocê ganhou!")
        user_points = user_points + 1
    elif user_choice == "p" and computer_option == "r":
        print(f"\nVocê ganhou!")
        user_points = user_points + 1
    else:
        print(f"\nVocê perdeu essa...")
        computer_points = computer_points + 1

print(f"\nSua pontuação:", user_points)
print("Pontuação do Computador:", computer_points)

if computer_points < user_points:
    print(f"\nVocê ganhou do Computador. Parabéns!!\n")
elif computer_points == user_points:
    print(f"\nVocê empatou com o Computador.\n")
else:
    print(f"\nVocê perdeu para o Computador. Boa sorte na próxima!\n")
