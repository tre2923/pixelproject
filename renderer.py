# renderer.py

import pygame


class Renderer:
    def __init__(self, screen):
        """
        Initializes the Renderer with the screen to draw on.

        :param screen: The Pygame screen to render to.
        """
        self.screen = screen

    def render_scene(self, scene):
        """
        Clears the screen and renders all objects in the given scene.

        :param scene: The scene to render, containing game objects.
        """
        self.screen.fill((255, 255, 255))  # Clear the screen with a white background
        for obj in scene.game_objects:
            for px, py in obj.get_pixels():
                if 0 <= px < self.screen.get_width() and 0 <= py < self.screen.get_height():
                    self.screen.set_at((int(px), int(py)), (0, 0, 0))  # Set pixel to black
        pygame.display.flip()
