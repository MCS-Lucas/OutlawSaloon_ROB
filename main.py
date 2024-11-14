"""
    #main.py

    Módulo de ponto de entrada para o jogo.
    Ele inicializa o Pygame, carrega os recursos, cria uma instância do jogo e executa o loop principal.
"""

import pygame
import sys
import config



# Inicializar o Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Outlaw Saloon: Rails of Blood")

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher a tela com uma cor de fundo
    screen.fill(WHITE)

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o Pygame
pygame.quit()
sys.exit()
