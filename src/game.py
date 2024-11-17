"""
    #game.py

    Módulo de gerenciamento do jogo.
    Cria e atualiza elementos principais, como jogador, inimigos, ui e inserts.
"""
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.level import Level
from src.player import Player
from src.enemies import Enemy


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Outlaw Saloon: Rails of Blood")
        self.level = Level()  # Inicializa o background e plataformas
        self.player = Player()  # Inicializa o jogador
        self.enemies = [  # Lista de inimigos
            Enemy(x=680, y=600, patrol_range=(680, 1100), platforms=self.level.get_platforms())
        ]
        self.clock = pygame.time.Clock()
        self.running = True
        print(f"Inimigos carregados: {len(self.enemies)}")

    def get_player(self):
        """Retorna o jogador para interações externas."""
        return self.player

    def update(self):
        """Atualiza os elementos do jogo."""
        # Atualiza o jogador com colisões de plataformas
        self.player.update(self.level.get_platforms())

        # Atualiza todos os inimigos
        for enemy in self.enemies:
            enemy.update(self.player)

    def draw(self):
        """Desenha os elementos do jogo."""
        # Primeiro desenha o nível (background e plataformas)
        self.level.draw(self.screen)

        # Depois desenha o jogador
        self.player.draw(self.screen)

        # Desenha os inimigos
        for enemy in self.enemies:
            enemy.draw(self.screen)

        # Atualiza a tela
        pygame.display.flip()

    def run(self):
        """Inicia o loop principal do jogo."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.draw()
            self.clock.tick(60)  # Limita o jogo a 60 FPS

        pygame.quit()
