import pygame
import math

def mostrar_jogador(screen, player, x, y):
    """Desenha o jogador na tela."""
    screen.blit(player, (x, y))

def mostrar_inimigo(screen, inimigo, x, y):
    """Desenha o inimigo na tela."""
    screen.blit(inimigo, (x, y))

def da_tiro(screen, bala, x, y):
    """Desenha o tiro na tela."""
    screen.blit(bala, (x + 16, y))

def colisao(inimigox, inimigoy, balax, balay):
    """Detecta colisão entre dois pontos (por distância)."""
    distancia = math.sqrt((inimigox - balax)**2 + (inimigoy - balay)**2)
    return distancia < 67

def game_over_texto(screen, fonte):
    """Mostra o Texto "GAME OVER". """
    fim = fonte.render("GAME OVER", True, (255, 0, 0))
    screen.blit(fim, (250, 250))

def mostra_ponto(screen, fonte, x, y, pontos):
    """Mostra os pontos na tela."""
    pontoo = fonte.render("Ponto: " + str(pontos), True, (255, 255, 255))
    screen.blit(pontoo, (x, y))
