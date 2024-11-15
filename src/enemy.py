"""
    #enemy.py

    Define a lógica e o comportamento dos inimigos.
"""
import pygame


class Enemy:
    sprite_idle_animation = [pygame.image.load("./assets/sprites/sprite_cowboy3_idle_1.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_2.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_3.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_4.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_5.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_6.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_7.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_8.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_9.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_10.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_11.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_12.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_13.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_14.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_15.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_16.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_17.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_18.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_19.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_20.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_21.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_22.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_23.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_24.png"),
                             pygame.image.load("./assets/sprites/sprite_cowboy3_idle_25.png")]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [x, end]  # Definirá aonde o inimigo começa e termina seu caminho.
        self.walkCount = 0
        self.speed = .5

    def move(self):
        if self.speed > 0:  # Se estiver em movimento para direita:
            if self.x < self.path[1] + self.speed:  # Se não chegou ao ultimo ponto possível à direita:
                self.x += self.speed
            else:  # Muda de direção e volta ao outro lado.
                self.speed = self.speed * -1
                self.x += self.speed
                self.walkCount = 0
        else:  # Se estiver em movimento para esquerda:
            if self.x > self.path[0] - self.speed:  # Se não chegou ao ultimo ponto possível à esquerda:
                self.x += self.speed
            else:  # Muda de direção e volta ao outro lado.
                self.speed = self.speed * -1
                self.x += self.speed
                self.walkCount = 0

    def draw(self, screen):  # Iniciar inimigo e controlar animação
        self.move()
        if self.walkCount + 1 >= 25:
            self.walkCount = 0

        if self.speed > 0:
            screen.blit(self.sprite_idle_animation[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(self.sprite_idle_animation[self.walkCount], (self.x, self.y))
            self.walkCount += 1
