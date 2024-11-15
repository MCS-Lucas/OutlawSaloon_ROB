"""
    #main.py

    Módulo de ponto de entrada para o jogo.
    Ele inicializa o Pygame, carrega os recursos, cria uma instância do jogo e executa o loop principal.
"""
import pygame
import sys
from src.game import Game


def main():
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
