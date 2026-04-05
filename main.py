# main.py
"""
Pong Workshop - Meu Primeiro Jogo com Python + Pygame
Vamos construir o clássico Pong passo a passo!
"""

import pygame
import random
from constantes import *

# ===============================================
# Inicialização do Pygame
# ===============================================
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong - Workshop Pygame")
clock = pygame.time.Clock()


# ===============================================
# Funções auxiliares
# ===============================================
def centralizar_bola():
    """Coloca a bola no centro e dá velocidade inicial aleatória."""
    bola.center = (LARGURA // 2, ALTURA // 2)
    vel_x = VELOCIDADE_BOLA_INICIAL * random.choice([-1, 1])
    vel_y = VELOCIDADE_BOLA_INICIAL * random.choice([-1, 1])
    return vel_x, vel_y


def desenhar_placar():
    """Desenha o placar na tela."""
    fonte = pygame.font.SysFont("arial", TAMANHO_FONTE_PLACAR, bold=True)
    texto_esq = fonte.render(str(pontos_esquerda), True, BRANCO)
    texto_dir = fonte.render(str(pontos_direita), True, BRANCO)
    tela.blit(texto_esq, (LARGURA // 4 - texto_esq.get_width() // 2, 20))
    tela.blit(texto_dir, (LARGURA * 3 // 4 - texto_dir.get_width() // 2, 20))


# ===============================================
# Variáveis do jogo
# ===============================================
pontos_esquerda = 0
pontos_direita = 0

# Paddles
paddle_esq = pygame.Rect(30, ALTURA // 2 - TAMANHO_PADDLE // 2, LARGURA_PADDLE, TAMANHO_PADDLE)
paddle_dir = pygame.Rect(LARGURA - 30 - LARGURA_PADDLE, ALTURA // 2 - TAMANHO_PADDLE // 2, LARGURA_PADDLE, TAMANHO_PADDLE)

# Bola
bola = pygame.Rect(LARGURA // 2 - RAIO_BOLA, ALTURA // 2 - RAIO_BOLA, RAIO_BOLA * 2, RAIO_BOLA * 2)
vel_x, vel_y = centralizar_bola()  # Velocidade inicial da bola

# ===============================================
# Game Loop Principal
# ===============================================
rodando = True
while rodando:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Entrada
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paddle_esq.top > 0:
        paddle_esq.y -= VELOCIDADE_PADDLE
    if teclas[pygame.K_s] and paddle_esq.bottom < ALTURA:
        paddle_esq.y += VELOCIDADE_PADDLE
    if teclas[pygame.K_UP] and paddle_dir.top > 0:
        paddle_dir.y -= VELOCIDADE_PADDLE
    if teclas[pygame.K_DOWN] and paddle_dir.bottom < ALTURA:
        paddle_dir.y += VELOCIDADE_PADDLE

    # Atualização do jogo
    bola.x += vel_x
    bola.y += vel_y

    # Colisão com paredes
    if bola.top <= 0 or bola.bottom >= ALTURA:
        vel_y = -vel_y

    # Colisão com paddles
    if bola.colliderect(paddle_esq) or bola.colliderect(paddle_dir):
        vel_x = -vel_x

    # Pontuação
    if bola.left <= 0:
        pontos_direita += 1
        vel_x, vel_y = centralizar_bola()
    if bola.right >= LARGURA:
        pontos_esquerda += 1
        vel_x, vel_y = centralizar_bola()

    # Desenho
    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, paddle_esq)
    pygame.draw.rect(tela, BRANCO, paddle_dir)
    pygame.draw.circle(tela, AZUL, bola.center, RAIO_BOLA)
    pygame.draw.line(tela, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA), 2)

    # Desenhar placar
    desenhar_placar()

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(FPS)

# Finalização
pygame.quit()
print("Obrigado por jogar/participar do workshop!")
