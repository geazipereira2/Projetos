import pygame
import sys
import random

pygame.init()
mainClock=pygame.time.Clock()

# Define as dimensões da tela
largura = 400
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake')

# Define a posição inicial da cobra
x_cobra = largura/2
y_cobra = altura/2
direcao = "" # Essa parte indica a direção que a cobra vai ou não+ 
# +estar se movendo quando o jogo abrir (nesse caso ela vai estar parada.)
cobra_cor = (0, 255, 0) # Verde
cobra_tamanho = 10

# Gera a posição aleatória para o ponto vermelho
x_ponto = 200
y_ponto = 300
ponto_tamanho = 5
ponto_cor = (255, 0, 0) # Vermelho
ponto_visivel = True

# A cauda da cobra
cauda = []

# Loop principal
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    distancia = ((x_cobra - x_ponto) ** 2 + (y_cobra - y_ponto) ** 2) ** 0.5
    if distancia < cobra_tamanho + ponto_tamanho:
        ponto_visivel = False
        # Nova posição aleatória do ponto
        x_ponto = random.randint(0, largura)
        y_ponto = random.randint(0, altura)
        # Faz a cobra crescer
        cauda.append((x_cobra, y_cobra))
    else:
        ponto_visivel = True

    tela.fill((0, 0, 0))  # preenche a tela com a cor preta
    if ponto_visivel:
        pygame.draw.circle(tela, (255,0,0), (x_ponto, y_ponto), ponto_tamanho) # desenha o ponto vermelho na tela
    pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 10, 10), cobra_tamanho)  # desenha a cobra na tela
    for segmento in cauda:
        pygame.draw.rect(tela, cobra_cor, (x_cobra, y_cobra, cobra_tamanho, cobra_tamanho))

    keys = pygame.key.get_pressed()
    # Define a velocidade da cobra:
    velocidade = 10

    if keys[pygame.K_LEFT]:
        direcao = "esquerda"
    if keys[pygame.K_RIGHT]:
        direcao = "direita"
    if keys[pygame.K_UP]:
        direcao = "cima"
    if keys[pygame.K_DOWN]:
        direcao = "baixo"

    if direcao == "direita":
        x_cobra += velocidade
    if direcao == "esquerda":
        x_cobra -= velocidade
    if direcao == "cima":
        y_cobra -= velocidade
    if direcao == "baixo":
        y_cobra += velocidade

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura
        
    pygame.display.update()  # Atualiza a tela
    mainClock.tick(20)

pygame.quit()
sys.exit()
