# game_state.py

class GameState:
    def __init__(self):
        """
        Initialize basic game state variables.
        """
        self.running = True  # Control the main game loop
        self.pixel_object_position = None  # Placeholder for the pixel position if needed
        # Add any other necessary attributes specific to the current game stage

    def stop(self):
        """
        Method to stop the game.
        """
        self.running = False
