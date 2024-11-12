import pygame
from pixel_object import PixelObject  # Import the PixelObject class
from renderer import render  # Import the render function from the renderer module

class Game:
    def __init__(self, screen_width, screen_height):
        """
        Initialize the game.

        :param screen_width: Width of the screen.
        :param screen_height: Height of the screen.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Black Pixel on White Screen")

        # Create the PixelObject instance
        self.pixel = PixelObject(1.0, (self.screen_width // 2, self.screen_height // 2), size=3)

    def handle_events(self):
        """
        Handle user events like quitting the game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Return False to indicate the game should end
        return True

    def update(self):
        """
        Update the game state.
        This could include updating positions, checking collisions, etc.
        """
        pass  # Currently no update logic; could be expanded later.

    def render(self):
        """
        Render the game objects to the screen.
        """
        # Fill the screen with white background
        self.screen.fill((255, 255, 255))

        # Render the PixelObject on the screen
        render(self.screen, self.pixel)

    def run(self):
        """
        The main game loop.
        """
        running = True
        while running:
            running = self.handle_events()  # Process user input events
            self.update()  # Update game state
            self.render()  # Render the game objects
            pygame.display.flip()  # Update the screen display

        pygame.quit()  # Quit Pygame when the game loop ends
