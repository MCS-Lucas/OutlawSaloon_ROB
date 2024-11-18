"""
    #ui.py

    Define elementos da interface do usuário, como pontuação, vida e menus.
"""
import pygame
import os


class UI:
    def __init__(self, screen):
        self.screen = screen

        # Caminho para os assets de vidas
        self.heart_image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'sprites', 'life', 'hat.png')
        self.heart_image = pygame.image.load(self.heart_image_path).convert_alpha()
        self.heart_image = pygame.transform.scale(self.heart_image, (40, 40))  # Ajusta o tamanho do ícone

        self.lives = 3  # Número inicial de vidas

        # Fonte para exibição de texto
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

    def draw_lives(self):
        """Desenha as vidas no canto superior esquerdo da tela."""
        for i in range(self.lives):
            x_position = 20 + i * 50
            self.screen.blit(self.heart_image, (x_position, 20))

    def draw_game_over(self):
        """Desenha a mensagem de Game Over na tela."""
        game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(game_over_text, text_rect)

    def reduce_life(self):
        """Reduz uma vida do jogador."""
        self.lives -= 1

    def is_game_over(self):
        """Verifica se o jogo acabou."""
        return self.lives <= 0

    def update(self):
        """Atualiza a interface de usuário."""
        if self.is_game_over():
            self.draw_game_over()
        else:
            self.draw_lives()
