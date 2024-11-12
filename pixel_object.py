import pygame

class PixelObject:
    def __init__(self, mass, position, size=1):
        """
        Initialize a PixelObject with mass, position, and size.

        :param mass: Mass of the object (in kg).
        :param position: Position of the object as a tuple (x, y).
        :param size: The size of the object (default is 1, making it a single pixel).
        """
        self.mass = mass
        self.position = pygame.Vector2(position)
        self.size = size  # Size of the object (default is 1)

    def get_pixels(self):
        """
        Get the list of positions representing the pixels that make up the PixelObject
        based on its size.

        :return: A list of (x, y) tuples representing the pixels.
        """
        pixels = []

        # Loop through the size to add pixels in all directions
        for dx in range(-self.size + 1, self.size):
            for dy in range(-self.size + 1, self.size):
                pixels.append((self.position.x + dx, self.position.y + dy))

        return pixels
