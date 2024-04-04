import time

t = input("Digite o tempo (em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida. Digite um número!")
    quit()

while t != 0:
    minutes, seconds = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutes, seconds) #O :02d formata o número de forma que exiba somente suas duas casas decimais
    print(timer, end="\r")
    time.sleep(1)
    t = t - 1

print("Tempo acabou!")
