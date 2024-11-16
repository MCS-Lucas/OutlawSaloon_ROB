"""
    #level.py

    gerencia os níveis do jogo, incluindo
    layout dos níveis, a posição inicial dos inimigos, itens,
    e quaisquer variáveis específicas associadas à fase do jogo.
"""
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_PATH


class Level:
    def __init__(self):
        # Carrega o background e ajusta a escala para as dimensões da tela
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Define as plataformas como retângulos
        self.platforms = [
            pygame.Rect(0, 684, 1280, 50),
            pygame.Rect(573, 650, 60, 60),
            pygame.Rect(1150, 638, 200, 70),
            # Adicione mais conforme necessário
        ]

    def draw(self, screen):
        # Desenha o background
        screen.blit(self.background, (0, 0))

        # Desenha as plataformas (exemplo: cor verde para visualizar)
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)  # Verde para destacar

    def get_platforms(self):
        return self.platforms
