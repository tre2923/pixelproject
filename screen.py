import pygame
from pixel_object import PixelObject  # Assuming this is where the PixelObject is defined


class Screen:
    def __init__(self, width, height, title="Game Window"):
        """
        Initializes the screen and primary game objects, like PixelObject.

        :param width: Width of the screen.
        :param height: Height of the screen.
        :param title: Title of the screen window.
        """
        self.width = width
        self.height = height
        self.screen = self.initialize_screen(title)

        # Initialize main game object(s)
        self.pixel = PixelObject(1.0, (self.width // 2, self.height // 2), size=3)

    def initialize_screen(self, title):
        """
        Set up the Pygame display window with the given title.

        :param title: Title of the screen window.
        :return: The Pygame screen object.
        """
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        return screen

    def clear_screen(self, color=(255, 255, 255)):
        """
        Clears the screen with the given background color.

        :param color: RGB color tuple for the background.
        """
        self.screen.fill(color)
