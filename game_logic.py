import pygame
from pixel_object import PixelObject
from renderer import render  # Import render function to handle object drawing
from screen import initialize_screen  # Import the screen setup function


class Game:
    def __init__(self, screen_width, screen_height):
        """
        Initialize the Game with display parameters and the game objects.

        :param screen_width: Width of the screen.
        :param screen_height: Height of the screen.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = initialize_screen(self.screen_width, self.screen_height, "Black Pixel on White Screen")

        # Initialize game objects (like PixelObject)
        self.pixel = PixelObject(1.0, (self.screen_width // 2, self.screen_height // 2), size=3)

    def handle_events(self):
        """
        Processes user events (like quitting the game).
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Return False to indicate the game should end
        return True

    def update(self):
        """
        Update the game state (e.g., positions, interactions).
        Currently no updates, but this is where you’d add game logic.
        """
        pass

    def render(self):
        """
        Clears the screen, then draws objects.
        """
        # Clear the screen with a white background
        self.screen.fill((255, 255, 255))

        # Render PixelObject
        render(self.screen, self.pixel)

    def run(self):
        """
        Main game loop.
        """
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            pygame.display.flip()

        pygame.quit()
