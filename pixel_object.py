# pixel_object.py

from game_object import GameObject


class PixelObject(GameObject):
    def __init__(self, mass, position, size=1):
        super().__init__(mass, position, size)

    def update(self):
        """
        Placeholder for update logic specific to PixelObject, if needed.
        """
        pass

    def get_pixels(self):
        x, y = self.position
        pixels = [(x, y)]

        for i in range(1, self.size):
            pixels.extend([
                (x + i, y), (x - i, y),
                (x, y + i), (x, y - i)
            ])

        return pixels
