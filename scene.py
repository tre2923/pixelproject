# scene.py

class Scene:
    def __init__(self, game_objects=None):
        """
        Initializes a scene with a list of game objects.

        :param game_objects: Optional list of game objects in the scene.
        """
        self.game_objects = game_objects if game_objects is not None else []

    def add_object(self, obj):
        """
        Adds a game object to the scene.

        :param obj: A game object to add to the scene.
        """
        self.game_objects.append(obj)

    def update(self):
        """
        Updates each game object in the scene.
        """
        for obj in self.game_objects:
            obj.update()
