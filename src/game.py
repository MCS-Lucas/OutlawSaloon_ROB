"""
    #game.py

    Módulo de gerenciamento do jogo.
    Cria e atualiza elementos principais, como jogador, inimigos, ui e inserts.
"""
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.player import Player
from src.level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Outlaw Saloon: Rails of Blood")
        self.level = Level()  # Inicializa o background
        self.player = Player()  # Inicializa o jogador
        self.clock = pygame.time.Clock()

    def update(self):
        # Atualiza o jogador com as plataformas do nível
        self.player.update(self.level.get_platforms())

    def draw(self):
        # Primeiro desenha o background
        self.level.draw(self.screen)

        # Depois desenha o jogador
        self.player.draw(self.screen)

        # Atualiza a tela
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
