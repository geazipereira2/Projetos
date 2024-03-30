print("Seja bem-vindo ao quiz!")
start_userAnswer = input("Quer começar? (S/N) ")

if start_userAnswer != "S":
    print("\nObrigado pelo interesse!")
    quit()

score = 0

print("\n(Questão 1) Quem é considerado o pai da computação? \n(A) Linus Torvalds \n(B) Alan Turing \n(C) Steve Wozniak \n(D) Steve Jobs \n")
answerQuestion_1 = input("Sua resposta: ")

if answerQuestion_1 == "B":
    print("Parabéns, você acertou!")
    score = score + 1
else:
    print("Você errou...")

print("\n(Questão 2) Qual o nome da máquina criada por Alan Turing? \n(A) IBM PC \n(B) ENIAC \n(C) Atari 2600 \n(D) Enigma \n")
answerQuestion_2 = input("Sua resposta: ")

if answerQuestion_2 == "D":
    print("Parabéns, você acertou!")
    score = score + 1
else:
    print("Você errou...")

print("\n(Questão 3) Qual era a função da máquina Enigma? \n(A) Processamento de dados em larga escala \n(B) Decodificação de mensagens criptografadas \n(C) Calculos balísticos \n(D) Gerenciamento de processos de fabricação \n")
answerQuestion_3 = input("Sua resposta: ")

if answerQuestion_3 == "B":
    print("Parabéns, você acertou!")
    score = score + 1
else:
    print("Você errou...")

print("\n(Questão 4) Depois da máquina Enigma, o computador ENIAC foi criado. Qual era sua função? \n(A) Armazenar grande volume de informações \n(B) Gerenciar processos de fabricação \n(C) Fazer cálculos balísticos precisos \n(D) Decodificar mensagens criptografadas \n")
answerQuestion_4 = input("Sua resposta: ")

if answerQuestion_4 == "C":
    print("Parabéns, você acertou!")
    score = score + 1
else:
    print("Você errou...")

print("\n(Questão 5) Qual a categoria a que o ENIAC pertence? \n(A) Computadores pessoais \n(B) Mainframes \n(C) Microcomputadores \n(D) Mobile \n")
answerQuestion_5 = input("Sua resposta: ")

if answerQuestion_5 == "B":
    print("Parabéns, você acertou!")
    score = score + 1
else:
    print("Você errou...")

if score >= 5:
    print("\nParabéns! Você acertou todas as questões!")
else:
    print(f"\nVocê acertou {score} questões.")

print("\nFim do quiz.")
