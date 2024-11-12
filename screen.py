# screen.py

import pygame

class Screen:
    def __init__(self, width, height, title="Game Window"):
        self.width = width
        self.height = height
        self.screen = self.initialize_screen(title)

    def initialize_screen(self, title):
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        return screen
