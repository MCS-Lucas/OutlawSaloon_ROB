"""
    #enemy.py

    Define a lógica e o comportamento dos inimigos.
"""


class Enemy:
    def __init__(self, game, x, y):

        self.game = game
        self.x = x
        self.y = y
