import pygame
from game_logic import Game  # Import the Game class

# Initialize Pygame
pygame.init()

# Set up the game with specified screen size
game = Game(screen_width=800, screen_height=600)

# Run the game loop
game.run()
