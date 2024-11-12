import pygame

def render(screen, pixel_object):
    """
    Render the PixelObject to the screen, ensuring pixel positions are within bounds.

    :param screen: The pygame screen object where pixels will be drawn.
    :param pixel_object: The PixelObject instance to be rendered.
    """
    # Get the list of pixels that make up the PixelObject
    for px, py in pixel_object.get_pixels():
        # Ensure the pixel coordinates are within bounds of the screen
        if 0 <= px < screen.get_width() and 0 <= py < screen.get_height():
            # Cast to int before setting the pixel
            screen.set_at((int(px), int(py)), (0, 0, 0))  # Set pixel to black
