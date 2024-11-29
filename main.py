"""
    #main.py

    Módulo de ponto de entrada para o jogo.
    Ele inicializa o Pygame, carrega os recursos, cria uma instância do jogo e executa o loop principal.
"""
import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.utils import show_menu
from src.game import Game



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Usa valores de config.py
    # Exibe o menu antes de iniciar o jogo
    show_menu(screen)
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
