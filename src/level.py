"""
    #level.py

    gerencia os níveis do jogo, incluindo
    layout dos níveis, a posição inicial dos inimigos, itens,
    e quaisquer variáveis específicas associadas à fase do jogo.
"""
import pygame


class Level:
    def __init__(self):
        self.level = 0


bg = pygame.image.load("./assets/images/background_x720.jpeg")
