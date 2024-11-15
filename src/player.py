"""
    #player.py

    Define a lógica e o comportamento do jogador.
"""
import pygame
import os
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
        self.shoot_index = 0
        self.velocity_y = 0

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
        elif keys[pygame.K_SPACE]:
            self.jump()

    def jump(self):
        """Inicia o pulo se não estiver pulando."""
        if not self.is_jumping:
            self.rect.y += 15
            self.is_jumping = True
            self.velocity_y = -15
            self.update_animation(self.jump_images)

    def apply_gravity(self, platforms):
        """Aplica a gravidade ao jogador."""
        # Verifica a colisão com cada plataforma
        for platform in platforms:
            if self.rect.colliderect(platform) and self.velocity_y > 0:  # Só verifica se caindo
                self.rect.bottom = platform.top  # Coloca o jogador em cima da plataforma
                self.is_jumping = False
                self.velocity_y = 0  # Para a velocidade ao colidir

        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height:
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.is_jumping = False

    def shoot(self):
        """Inicia a sequência de tiro."""
        self.is_shooting = True
        self.shoot_index = 0

    def update_animation(self, animation_images):
        """Atualiza o frame da animação do jogador."""
        self.move_index = (self.move_index + 1) % len(animation_images)
        self.image = animation_images[self.move_index]

    def update(self, platforms):
        """Atualiza o estado e a animação do jogador com a física de colisão."""
        self.move()
        self.apply_gravity(platforms)  # Passa as plataformas para a função

        # Verifica e atualiza a animação de tiro
        if self.is_shooting:
            self.image = self.shoot_images[self.shoot_index]
            self.shoot_index += 1
            if self.shoot_index >= len(self.shoot_images):
                self.is_shooting = False

    def draw(self, screen):
        """Desenha o jogador na tela."""
        screen.blit(self.image, self.rect)
