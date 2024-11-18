"""
    #enemies.py

    Define a lógica e o comportamento dos inimigos.
"""
import pygame
import os


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, patrol_range, platforms):
        super().__init__()

        # Caminho para os diretórios das animações
        self.sprites_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'sprites', 'enemies')

        # Carrega as animações
        self.walk_images = self.load_images('walk', 10)
        self.attack_images = self.load_images('punch', 4)

        # Define a imagem e posição iniciais do inimigo
        self.image = self.walk_images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Variáveis de controle de movimento
        self.patrol_range = patrol_range
        self.direction = 1  # 1 para direita, -1 para esquerda
        self.speed = 2

        # Controle de animação
        self.is_attacking = False
        self.walk_index = 0
        self.attack_index = 0
        self.frame_count = 0
        self.frame_delay = 5  # Velocidade da animação

        # Plataformas para colisão
        self.platforms = platforms
        self.on_platform = False  # Verifica se o inimigo está em uma plataforma

    def load_images(self, folder_name, frame_count):
        """Carrega uma lista de imagens de uma pasta específica."""
        folder_path = os.path.join(self.sprites_path, folder_name)
        print(f"Carregando imagens de: {folder_path}")
        return [pygame.image.load(os.path.join(folder_path, f"{folder_name.capitalize()}{i}.png")).convert_alpha()
                for i in range(1, frame_count + 1)]

    def move(self):
        """Move o inimigo horizontalmente e verifica colisões com plataformas."""
        # Move horizontalmente
        self.rect.x += self.direction * self.speed

        # Verifica os limites de patrulha
        if self.rect.left <= self.patrol_range[0] or self.rect.right >= self.patrol_range[1]:
            self.direction *= -1
        # Atualiza a animação de caminhada
        self.update_animation(self.walk_images)

    def apply_gravity(self):
        """Aplica gravidade e verifica colisões com plataformas."""
        print(f"Aplicando gravidade ao inimigo na posição {self.rect}")
        self.rect.y += 5  # Velocidade de queda

        self.on_platform = False  # Inicialmente assume que não está em uma plataforma

        # Verifica colisões com as laterais das plataformas
        for platform in self.platforms:
            if self.rect.colliderect(platform):
                if platform.top <= self.rect.bottom <= platform.top + 10:
                    self.rect.bottom = platform.top
                    self.on_platform = True
                    break
        # Se não estiver em uma plataforma, continua caindo
        if not self.on_platform:
            self.rect.y += 5
            print(f"Inimigo no ar: {self.rect}")

    def attack(self, player):
        """Inicia a animação de ataque se colidir com o jogador."""
        if self.rect.colliderect(player.rect):
            self.is_attacking = True
            return True  # Indica que o jogador foi atacado
        return False

    def update_animation(self, animation_images):
        """Atualiza o frame da animação."""
        self.frame_count += 1
        if self.frame_count >= self.frame_delay:
            self.frame_count = 0
            if self.is_attacking:
                if self.attack_index < len(self.attack_images):
                    if self.direction < 0:
                        self.image = pygame.transform.flip(self.attack_images[self.attack_index], True, False)
                    elif self.direction > 0:
                        self.image = self.attack_images[self.attack_index]
                    self.attack_index += 1
                else:
                    self.attack_index = 0  # Reinicia o ataque
                    self.is_attacking = False
            else:
                self.walk_index = (self.walk_index + 1) % len(animation_images)
                self.image = animation_images[self.walk_index]
                if self.direction < 0:
                    self.image = pygame.transform.flip(self.image, True, False)

    def update(self, player):
        """Atualiza o estado do inimigo."""
        if self.is_attacking:
            self.update_animation(self.attack_images)
        else:
            self.move()
            self.attack(player)

    def draw(self, screen):
        """Desenha o inimigo na tela."""
        screen.blit(self.image, self.rect)
