# events.py

import pygame


def handle_events(game_state):
    """
    Process basic game events, such as quitting the game.

    :param game_state: Instance of GameState to modify based on events.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.stop()  # Stop the game when the quit event is triggered
