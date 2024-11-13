# game_logic.py

import pygame
from events import handle_events
from collision import check_collision
from scene import Scene
from renderer import Renderer
from pixel_object import PixelObject
from game_state import GameState
from screen import Screen


class Game:
    def __init__(self, screen_width, screen_height):
        # Initialize the screen handler with screen dimensions and a title
        self.screen_handler = Screen(screen_width, screen_height, "Black Pixel on White Screen")

        # Initialize the game state
        self.state = GameState()

        # Create the scene and add objects
        self.scene = Scene()
        self.pixel = PixelObject(1.0, (screen_width // 2, screen_height // 2), size=3)
        self.scene.add_object(self.pixel)

        # Initialize the renderer to display the screen
        self.renderer = Renderer(self.screen_handler.screen)

        self.screen_width = screen_width
        self.screen_height = screen_height

    def run(self):
        # Main game loop
        while self.state.running:
            # Handle events like user input (movement, quitting)
            handle_events(self.state, self.pixel)

            # Check if the pixel object collides with the screen bounds
            check_collision(self.pixel, self.screen_width, self.screen_height)

            # Update the scene (this may update objects in the scene)
            self.scene.update()

            # Render the updated scene to the screen
            self.renderer.render_scene(self.scene)

        # Quit pygame when the game ends
        pygame.quit()

