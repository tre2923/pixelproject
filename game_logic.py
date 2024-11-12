# game_logic.py

import pygame
from screen import Screen
from game_state import GameState
from events import handle_events
from scene import Scene
from renderer import Renderer
from pixel_object import PixelObject

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_handler = Screen(screen_width, screen_height, "Black Pixel on White Screen")
        self.state = GameState()

        # Initialize the main scene and add objects
        self.scene = Scene()
        self.pixel = PixelObject(1.0, (screen_width // 2, screen_height // 2), size=3)
        self.scene.add_object(self.pixel)

        # Initialize the renderer
        self.renderer = Renderer(self.screen_handler.screen)

    def run(self):
        while self.state.running:
            handle_events(self.state)
            self.scene.update()
            self.renderer.render_scene(self.scene)  # Delegate rendering to the Renderer
        pygame.quit()
