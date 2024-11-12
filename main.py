import pygame
from game import Game  # Import the Game class

# Initialize Pygame
pygame.init()

# Set up the game
game = Game(screen_width=800, screen_height=600)

# Start the game loop
game.run()
