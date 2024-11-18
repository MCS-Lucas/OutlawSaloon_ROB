"""
    #level.py

    gerencia os níveis do jogo, incluindo
    layout dos níveis, a posição inicial dos inimigos, itens,
    e quaisquer variáveis específicas associadas à fase do jogo.
"""
import pygame
from .enemy import Enemy

bg = pygame.image.load("./assets/images/background_x720.jpeg")


class Level:
    def __init__(self):
        self.level = 0

    @staticmethod
    def level_load_1(screen):
        # Instâncias
        cowboy3 = Enemy(100, 410, 60, 60, 600)

        # Spawn
        cowboy3.draw(screen)
