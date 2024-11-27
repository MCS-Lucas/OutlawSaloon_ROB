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

        # Tenta carregar o áudio e iniciar a reprodução
        try:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play(-1, 0.0)  # Toca o áudio em loop
        except pygame.error as e:
            print(f"Erro ao carregar o áudio: {e}")
            return  # Se não conseguir carregar o áudio, retorna imediatamente

        # Abre o vídeo usando OpenCV
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Erro ao abrir o vídeo: {video_path}")
            pygame.mixer.music.stop()  # Para o áudio se o vídeo não puder ser carregado
            return

        clock = pygame.time.Clock()

        # Obtém a largura e altura do vídeo original
        video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Define a escala para manter a proporção do vídeo na tela
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        # Calcula a escala para manter a proporção
        scale_factor = min(screen_width / video_width, screen_height / video_height)
        new_width = int(video_width * scale_factor)
        new_height = int(video_height * scale_factor)

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break  # Fim do vídeo

            # Converte a imagem do OpenCV (BGR) para o formato do Pygame (RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Se a rotação for necessária (caso a largura seja menor que a altura), rotaciona o frame
            if video_width < video_height:
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)  # Roda 90 graus no sentido horário

            # Verifica se o vídeo está invertido e corrige se necessário
            # (isso pode ser necessário se o vídeo tiver sido gravado de forma invertida)
            frame = cv2.rotate(frame, cv2.ROTATE_180)  # Roda o vídeo 180 graus (inverte)

            # Redimensiona o frame para manter a proporção correta
            frame = cv2.resize(frame, (new_width, new_height))

            # Converte o frame redimensionado para uma superfície Pygame
            frame_surface = pygame.surfarray.make_surface(frame)

            # Calcula a posição para centralizar o vídeo na tela
            x_position = (screen_width - new_width) // 2
            y_position = (screen_height - new_height) // 2

            # Exibe o frame centralizado na tela
            self.screen.fill((0, 0, 0))  # Limpa a tela com a cor preta
            self.screen.blit(frame_surface, (x_position, y_position))
            pygame.display.flip()

            # Controle de eventos para fechar a janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cap.release()
                    pygame.mixer.music.stop()  # Para a música
                    pygame.quit()
                    exit()

            clock.tick(30)  # Limita a taxa de quadros a 30 FPS

        cap.release()
        pygame.mixer.music.stop()  # Para a música quando o vídeo terminar

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
