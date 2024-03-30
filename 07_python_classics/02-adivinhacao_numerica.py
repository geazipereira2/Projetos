import random

print("Bem vindo ao Guess Number, ou o jogo de adivinhação numérica!")
choice_number = input("Digite o número teto do desafio: ")

'''Verifica se o que foi digitado é um número, se sim: armazena ele na variável do início como um valor inteiro, 
se não: printa um mensagem na tela e encerra o programa.'''
if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("O valor digitado não é um número. Execute novamente e digite um número!")
    quit()

#Gera um número aleatório entre 0 e o número digitado pelo usuário:
random_number = random.randint(0, choice_number) 

n_choices = 0 #Essa variável é um contador (vai contar quantas vezes o usuário tentou antes de acertar o número)

#Loop para executar o algoritmo enquanto o usuário não acertar o número:
while True:
    answer_user = input("Adivinhe o número: ")
    
    #Verifica o que foi digitado (se é, ou não é um número).
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("O valor digitado não é um número. Favor digitar um número!")
        continue #Ignora tudo abaixo e volta para o início do loop.
    
    n_choices = n_choices + 1 #A variável contador ganha +1 a cada tentativa mal-sucedida do usuário!

    #Se o número do usuário for igual ao número gerado aleatoriamente:
    if answer_user == random_number: 
        print(f"\nAcertô mizeravi!\n")
        break #Quebra o loop e para a execução do programa.
    elif answer_user > random_number: 
        print("Chutou alto, o número é MENOR que isso...")
    else: 
        print("Chutou baixo, o número é MAIOR que isso...")

print("N de tentativas: " + str(n_choices))
