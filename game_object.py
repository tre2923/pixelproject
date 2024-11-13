# game_object.py

class GameObject:
    def __init__(self, mass, position, size=1, velocity=(0, 0)):
        """
        Initializes a new game object.

        :param mass: The mass of the object.
        :param position: A tuple (x, y) representing the position of the object.
        :param size: The size of the object (used for PixelObject to determine area).
        :param velocity: A tuple (vx, vy) representing the velocity of the object.
        """
        self.mass = mass
        self.position = position
        self.size = size
        self.velocity = velocity

    def update(self):
        """
        Update the state of the object. This method should be overridden by subclasses
        to implement custom behavior for each object.
        """
        pass

    def get_pixels(self):
        """
        Returns the list of pixels that make up the object (to be overridden in subclasses).

        :return: A list of tuples (x, y) representing the pixels occupied by the object.
        """
        raise NotImplementedError("get_pixels method must be implemented in the subclass.")
