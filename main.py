"""
    #main.py

    Módulo de ponto de entrada para o jogo.
    Ele inicializa o Pygame, carrega os recursos, cria uma instância do jogo e executa o loop principal.
"""
import os

import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.utils import show_menu
from src.game import Game
from src.ui import UI


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Exibe o menu
    show_menu(screen)

    # Caminhos dos arquivos de vídeo e áudio
    video_path = os.path.join('assets', 'animatic', 'teste de audio akyno.mp4')
    audio_path = os.path.join('assets', 'animatic', 'teste de audio akyno-C-77bpm-441hz.mp3')

    # Reproduz a cutscene
    ui = UI(screen)
    ui.play_cutscene(video_path, audio_path)

    # Inicia o jogo
    game = Game()
    game.run()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
