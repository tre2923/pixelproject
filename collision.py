# collision.py

def check_collision(pixel_object, screen_width, screen_height):
    """
    Simple collision detection to keep the pixel object within screen bounds.

    :param pixel_object: The PixelObject to check for collision.
    :param screen_width: Width of the screen.
    :param screen_height: Height of the screen.
    """
    x, y = pixel_object.position
    size = pixel_object.size

    # Check if the object goes out of bounds on the left, right, top, or bottom
    if x - size < 0:  # Left bound
        pixel_object.position = (size, y)
    if x + size >= screen_width:  # Right bound
        pixel_object.position = (screen_width - size - 1, y)
    if y - size < 0:  # Top bound
        pixel_object.position = (x, size)
    if y + size >= screen_height:  # Bottom bound
        pixel_object.position = (x, screen_height - size - 1)
