# game_object.py

class GameObject:
    def __init__(self, mass, position, size=1):
        """
        Base class for all game objects, including common attributes such as mass, position, and size.

        :param mass: Mass of the object.
        :param position: Tuple for the object's x, y coordinates.
        :param size: Size of the object, default is 1.
        """
        self.mass = mass
        self.position = position
        self.size = size

    def get_position(self):
        """
        Returns the current position of the object.

        :return: Tuple of (x, y) coordinates.
        """
        return self.position

    def set_position(self, new_position):
        """
        Sets a new position for the object.

        :param new_position: Tuple with new (x, y) coordinates.
        """
        self.position = new_position

    def get_mass(self):
        """
        Returns the mass of the object.

        :return: Mass of the object.
        """
        return self.mass
