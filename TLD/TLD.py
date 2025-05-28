import pygame
import random
from modulos import *

# Inicialização
pygame.init()

# Tamanho da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Ícone e título
pygame.display.set_caption("THE LAST DONETE")
foto = pygame.image.load('images/donut.png')
pygame.display.set_icon(foto)

# Fundo
background = pygame.image.load('images/mesa.jpg')

# Jogadores
player = pygame.image.load('images/donete_jogador.png')
playerx = 370
playery = 480

player2 = pygame.image.load('images/donete_jogador2.png')
player2x = 470
player2y = 480

# Tiros
bala = pygame.image.load('images/tiro.png')
balax = 0
balay = 480
bala_mudancay = 10
estado_bala = "ready"

bala2 = pygame.image.load('images/tiro.png')
balax2 = 0
balay2 = 480
estado_bala2 = "ready"

# Inimigos
inimigo_img = []
inimigox = []
inimigoy = []
inimigox_mudanca = []
inimigoy_mudanca = []
num_inimigos = 6

for _ in range(num_inimigos):
    inimigo_img.append(pygame.image.load('images/boca.png'))
    inimigox.append(random.randint(0, screen_width - 64))
    inimigoy.append(random.randint(50, 150))
    inimigox_mudanca.append(5)
    inimigoy_mudanca.append(40)

# Pontuação
valor_de_ponto = 0
textox = 10
textoy = 10
font = pygame.font.Font('freesansbold.ttf', 32)

# Fonte Game Over
game_over_fonte = pygame.font.Font('freesansbold.ttf', 64)


# Loop principal
clock = pygame.time.Clock()
run = True

while run:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and estado_bala == "ready":
                balax = playerx + 16
                balay = playery
                estado_bala = "fire"
            if event.key == pygame.K_RSHIFT and estado_bala2 == "ready":
                balax2 = player2x + 16
                balay2 = player2y
                estado_bala2 = "fire"

    # Movimento dos jogadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: playerx -= 5
    if keys[pygame.K_d]: playerx += 5
    if keys[pygame.K_w]: playery -= 5
    if keys[pygame.K_s]: playery += 5

    if keys[pygame.K_LEFT]: player2x -= 5
    if keys[pygame.K_RIGHT]: player2x += 5
    if keys[pygame.K_UP]: player2y -= 5
    if keys[pygame.K_DOWN]: player2y += 5

    # Limites dos jogadores
    playerx = max(0, min(playerx, screen_width - 64))
    playery = max(0, min(playery, screen_height - 64))
    player2x = max(0, min(player2x, screen_width - 64))
    player2y = max(0, min(player2y, screen_height - 64))

    # Inimigos
    for i in range(num_inimigos):
        if inimigoy[i] > playery or inimigoy[i] > player2y:
            for j in range(num_inimigos):
                inimigoy[j] = 2000
            game_over_texto(screen, game_over_fonte)
            break

        inimigox[i] += inimigox_mudanca[i]
        if inimigox[i] <= 0 or inimigox[i] >= screen_width - 64:
            inimigox_mudanca[i] *= -1.05
            inimigoy[i] += inimigoy_mudanca[i]

        if colisao(inimigox[i], inimigoy[i], balax, balay):
            balay = playery
            estado_bala = "ready"
            valor_de_ponto += 1
            inimigox[i] = random.randint(0, screen_width - 64)
            inimigoy[i] = random.randint(50, 150)

        if colisao(inimigox[i], inimigoy[i], balax2, balay2):
            balay2 = player2y
            estado_bala2 = "ready"
            valor_de_ponto += 1
            inimigox[i] = random.randint(0, screen_width - 64)
            inimigoy[i] = random.randint(50, 150)

        mostrar_inimigo(screen, inimigo_img[i], inimigox[i], inimigoy[i])

    # Movimento das balas
    if estado_bala == "fire":
        da_tiro(screen, bala, balax, balay)
        balay -= bala_mudancay
        if balay <= 0:
            estado_bala = "ready"

    if estado_bala2 == "fire":
        da_tiro(screen, bala2, balax2, balay2)
        balay2 -= bala_mudancay
        if balay2 <= 0:
            estado_bala2 = "ready"

    # Mostrar jogadores
    mostrar_jogador(screen, player, playerx, playery)
    mostrar_jogador(screen, player2, player2x, player2y)

    # Mostrar pontuação
    mostra_ponto(screen, font, textox, textoy, valor_de_ponto)

    # Atualiza tela
    pygame.display.update()
    clock.tick(60)

pygame.quit()

