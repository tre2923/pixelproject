import pygame


def initialize_screen(width, height, title="Game Window"):
    """
    Initializes the Pygame display window with the given width, height, and title.

    :param width: Width of the screen.
    :param height: Height of the screen.
    :param title: Title of the window.
    :return: The Pygame screen object.
    """
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return screen
