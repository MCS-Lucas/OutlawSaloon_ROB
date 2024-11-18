"""
    #player.py

    Define a lógica e o comportamento do jogador.
"""
import os

import pygame

from config import SCREEN_HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Caminho para os diretórios das animações
        self.sprites_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'sprites')

        # Carrega as animações
        self.move_images = self.load_images('walk')
        self.jump_images = self.load_images('jump')
        self.shoot_images = self.load_images('shot')

        # Define a imagem e posição iniciais do jogador
        self.image = self.move_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT - 100)

        # Variáveis de controle de estado e animação
        self.is_jumping = False
        self.is_shooting = False
        self.move_index = 0
        self.jump_index = 0
        self.shoot_index = 0
        self.velocity_y = 0

        # Controle de velocidade da animação
        self.frame_count = 0
        self.frame_delay = 5  # Número de frames entre cada atualização de animação

    def load_images(self, folder_name):
        """Carrega uma lista de imagens de uma pasta específica."""
        folder_path = os.path.join(self.sprites_path, folder_name)
        return [pygame.image.load(os.path.join(folder_path, f"{folder_name.capitalize()}{i}.png")).convert_alpha()
                for i in range(1, 10)]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Movendo para a esquerda com a tecla 'A'
            self.rect.x -= 5
            self.update_animation(self.move_images)
        elif keys[pygame.K_d]:  # Movendo para a direita com a tecla 'D'
            self.rect.x += 5
            self.update_animation(self.move_images)

        if keys[pygame.K_SPACE]:
            self.jump()

    def jump(self):
        """Inicia o pulo se não estiver pulando."""
        if not self.is_jumping:
            self.velocity_y = -15
            self.is_jumping = True
            self.jump_index = 0  # Reinicia a animação de pulo

    def apply_gravity(self, platforms):
        """Aplica a gravidade e impede que o jogador atravesse as plataformas."""
        self.rect.y += self.velocity_y
        self.velocity_y += 1  # Gravidade constante

        for platform in platforms:
            if self.rect.colliderect(platform):
                # O jogador está caindo e colidiu com o topo da plataforma
                if self.velocity_y > 0 and self.rect.bottom - self.velocity_y <= platform.top:
                    self.rect.bottom = platform.top  # Coloca o jogador no topo da plataforma
                    self.is_jumping = False  # Termina o pulo
                    self.velocity_y = 0  # Cancela a velocidade vertical
                # O jogador está subindo e colidiu com a parte inferior da plataforma
                elif self.velocity_y < 0 and self.rect.top >= platform.bottom - self.velocity_y:
                    self.rect.top = platform.bottom  # Impede atravessar a plataforma
                    self.velocity_y = 0  # Para o movimento vertical

            # Colisão com as laterais da plataforma
            if self.rect.colliderect(platform):
                if self.rect.right > platform.left > self.rect.left:
                    self.rect.right = platform.left  # Colisão no lado esquerdo do jogador
                elif self.rect.left < platform.right < self.rect.right:
                    self.rect.left = platform.right  # Colisão no lado direito do jogador

        # Impede que o jogador atravesse o chão
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.is_jumping = False
            self.velocity_y = 0

    def shoot(self):
        """Inicia a sequência de tiro."""
        self.is_shooting = True
        self.shoot_index = 0

    def update_animation(self, animation_images):
        """Atualiza o frame da animação do jogador."""
        # Incrementa o contador de frames
        self.frame_count += 1
        if self.frame_count >= self.frame_delay:
            self.frame_count = 0  # Reinicia o contador
            self.move_index = (self.move_index + 1) % len(animation_images)
            self.image = animation_images[self.move_index]

    def check_enemy_collision(self, enemies, ui):
        """Verifica colisão com inimigos e reduz vida."""
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                ui.reduce_life()
                # Opcional: reposicione o jogador após colisão
                self.rect.center = (100, SCREEN_HEIGHT - 100)

    def update(self, platforms, enemies, ui):
        """Atualiza o estado e a animação do jogador com a física de colisão."""
        self.move()
        self.apply_gravity(platforms)
        self.check_enemy_collision(enemies, ui)

        # Atualiza animação de pulo enquanto estiver no ar
        if self.is_jumping:
            self.frame_count += 1
            if self.frame_count >= self.frame_delay:
                self.frame_count = 0
                if self.jump_index < len(self.jump_images):
                    self.image = self.jump_images[self.jump_index]
                    self.jump_index += 1

        # Verifica e atualiza a animação de tiro
        if self.is_shooting:
            self.frame_count += 1
            if self.frame_count >= self.frame_delay:
                self.frame_count = 0
                self.image = self.shoot_images[self.shoot_index]
                self.shoot_index += 1
                if self.shoot_index >= len(self.shoot_images):
                    self.is_shooting = False

    def draw(self, screen):
        """Desenha o jogador na tela."""
        screen.blit(self.image, self.rect)
