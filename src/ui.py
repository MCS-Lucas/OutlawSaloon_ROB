"""
    #ui.py

    Define elementos da interface do usuário, como pontuação, vida e menus.
"""
import pygame
import os
import cv2


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

    def play_cutscene(self, video_path, audio_path):
        """Reproduz uma cutscene utilizando OpenCV e toca o áudio no fundo."""

        # Verificar se os arquivos existem
        if not os.path.exists(video_path):
            print(f"Erro: O caminho do vídeo '{video_path}' não existe!")
            return
        if not os.path.exists(audio_path):
            print(f"Erro: O caminho do áudio '{audio_path}' não existe!")
            return

        # Carrega e inicia o áudio
        try:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play(-1, 0.0)
        except pygame.error as e:
            print(f"Erro ao carregar o áudio: {e}")
            return

        # Carrega o vídeo usando OpenCV
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Erro: Não foi possível abrir o arquivo de vídeo: {video_path}")
            pygame.mixer.music.stop()
            return

        # Dimensões da tela
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        clock = pygame.time.Clock()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break  # Fim do vídeo

            # Converte de BGR (OpenCV) para RGB (Pygame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            frame = cv2.flip(frame, 1)

            # Redimensionar para caber na tela mantendo a proporção
            video_width = frame.shape[0]
            video_height = frame.shape[0]

            scale_factor = min(screen_width / video_width, screen_height / video_height)

            new_width = int(video_width * scale_factor)
            new_height = int(video_height * scale_factor)

            frame = cv2.resize(frame, (new_width, new_height))

            # Centralizar o vídeo
            x_position = (screen_width - new_width) // 2
            y_position = (screen_height - new_height) // 2

            # Criar uma superfície Pygame
            frame_surface = pygame.surfarray.make_surface(frame)

            # Desenhar o vídeo na tela
            self.screen.fill((0, 0, 0))  # Preencher com preto
            self.screen.blit(frame_surface, (x_position, y_position))
            pygame.display.flip()

            # Trata eventos (permitir sair da cutscene)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cap.release()
                    pygame.mixer.music.stop()
                    pygame.quit()
                    exit()

            clock.tick(30)  # Limita a 30 FPS

        cap.release()
        pygame.mixer.music.stop()

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
