# Start date: 13, 12, 2025
# By: Lewis Burt
''' This is the debug class. '''

# Imports:
import os
os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
from ..file_importer import Defaults, dev_settings, PG, colours

class DebuggingClass():
    """ Used for all things debugging related. """
    def __init__(self, game_class):
        self.game_class = game_class


    def draw_grid(self):
        """ Draws a grid across the screen. """
        for x in range(0, Defaults.WIDTH, dev_settings.TILESIZE):
            PG.draw.line(self.game_class.screen, colours.LIGHTGREY, (x, 0), (x, Defaults.HEIGHT))
        for y in range(0, Defaults.HEIGHT, dev_settings.TILESIZE):
            PG.draw.line(self.game_class.screen, colours.LIGHTGREY, (0, y), (Defaults.WIDTH, y))
