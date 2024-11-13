# events.py

import pygame


def handle_events(game_state, pixel_object):
    """
    Process basic game events, such as quitting the game and moving the object.

    :param game_state: Instance of GameState to modify based on events.
    :param pixel_object: Instance of PixelObject to update its position.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.stop()  # Stop the game when the quit event is triggered
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pixel_object.position = (pixel_object.position[0] - 1, pixel_object.position[1])
            elif event.key == pygame.K_RIGHT:
                pixel_object.position = (pixel_object.position[0] + 1, pixel_object.position[1])
            elif event.key == pygame.K_UP:
                pixel_object.position = (pixel_object.position[0], pixel_object.position[1] - 1)
            elif event.key == pygame.K_DOWN:
                pixel_object.position = (pixel_object.position[0], pixel_object.position[1] + 1)
