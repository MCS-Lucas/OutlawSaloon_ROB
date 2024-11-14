import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Outlaw Saloon: Rails of Blood")

# Configurações de cores
WHITE = (255, 255, 255)

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
