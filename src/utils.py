"""
    #utils.py

    Este módulo armazena funções utilitárias,
    como cálculos de distância, detecção de colisões, ou carregamento de imagens e sons.
"""
import pygame
import webbrowser
import os
from config import SCREEN_WIDTH, SCREEN_HEIGHT


def show_menu(screen):
    # Carrega o background do menu
    background_image = pygame.image.load(os.path.join("assets", "images", "Background-menu.png"))
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Configurações dos botões
    button_font = pygame.font.Font(None, 40)
    button_color = (125, 84, 71)
    button_hover_color = (92, 67, 68)
    button_text_color = (217, 186, 148)
    buttons = [
        {"label": "Start Game", "action": "start"},
        {"label": "Exit Game", "action": "exit"},
        {"label": "Repository", "action": "repo"},
    ]

    button_width = 300
    button_height = 50
    button_spacing = 20
    offset_y = 90  # Define o deslocamento para empurrar os botões para baixo
    button_start_y = SCREEN_HEIGHT // 2 - ((button_height + button_spacing) * len(buttons)) // 2 + offset_y

    # Música do menu
    pygame.mixer.music.load(os.path.join("assets", "music", "Americana.mp3"))
    pygame.mixer.music.play(-1)

    # Controle de clique
    click_released = True

    running = True
    while running:
        screen.blit(background_image, (0, 0))

        # Detecta eventos do mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        for i, button in enumerate(buttons):
            button_x = SCREEN_WIDTH // 2 - button_width // 2
            button_y = button_start_y + i * (button_height + button_spacing)

            if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                color = button_hover_color
                if mouse_pressed and click_released:
                    click_released = False  # Bloqueia múltiplos cliques enquanto o botão está pressionado
                    if button["action"] == "start":
                        running = False
                    elif button["action"] == "exit":
                        pygame.quit()
                        exit()
                    elif button["action"] == "repo":
                        webbrowser.open("https://github.com/MCS-Lucas/OutlawSaloon_ROB.git")
            else:
                color = button_color

            # Desenha o botão
            pygame.draw.rect(screen, color, (button_x, button_y, button_width, button_height))
            text_surface = button_font.render(button["label"], True, button_text_color)
            text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
            screen.blit(text_surface, text_rect)

        # Libera o clique quando o botão do mouse é solto
        if not mouse_pressed:
            click_released = True

        # Atualiza a tela
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    # Para a música do menu ao sair
    pygame.mixer.music.stop()
