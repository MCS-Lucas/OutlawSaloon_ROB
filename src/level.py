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
            pygame.Rect(595, 650, 40, 60),
            pygame.Rect(1180, 638, 100, 70),
            pygame.Rect(400, 500, 100, 15),
            pygame.Rect(665, 585, 50, 15),
            pygame.Rect(678, 443, 70, 15),
            pygame.Rect(0, 400, 20, 400),
            pygame.Rect(1270, 400, 20, 400),
            # Adicione mais conforme necessário
        ]

    def draw(self, screen):
        # Desenha o background
        screen.blit(self.background, (0, 0))

    def get_platforms(self):
        return self.platforms

