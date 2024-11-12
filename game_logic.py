import pygame
from screen import Screen
from game_state import GameState
from events import handle_events
from renderer import render  # Render function for drawing objects

class Game:
    def __init__(self, screen_width, screen_height):
        """
        Initializes the game with screen, game state, and other essential components.
        """
        self.screen_handler = Screen(screen_width, screen_height, "Black Pixel on White Screen")
        self.state = GameState()  # Initialize game state

    def update(self):
        """
        Update game state and logic.
        """
        # Here you can include any game state updates outside of events
        pass

    def render(self):
        """
        Render the game objects on the screen.
        """
        self.screen_handler.clear_screen((255, 255, 255))  # Clear with white background
        render(self.screen_handler.screen, self.screen_handler.pixel)  # Render the main object
        pygame.display.flip()

    def run(self):
        """
        Main game loop.
        """
        while self.state.running:
            handle_events(self.state)  # Handle user inputs
            self.update()  # Update game state
            self.render()  # Render to the screen

        pygame.quit()
