# pixel_object.py

from game_object import GameObject


class PixelObject(GameObject):
    def __init__(self, mass, position, size=1):
        """
        Initialize a PixelObject, inheriting from GameObject.

        :param mass: Mass of the object.
        :param position: Tuple for x, y coordinates.
        :param size: Size of the object, default is 1 pixel.
        """
        super().__init__(mass, position, size)

    def get_pixels(self):
        """
        Get the coordinates of the pixels that make up the object based on its size.

        :return: List of tuples with (x, y) coordinates for each pixel in the object.
        """
        x, y = self.position
        pixels = [(x, y)]

        # Add neighboring pixels to the north, south, east, and west
        for i in range(1, self.size):
            pixels.extend([
                (x + i, y), (x - i, y),  # Right and left
                (x, y + i), (x, y - i)  # Down and up
            ])

        return pixels
