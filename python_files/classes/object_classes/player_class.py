# Start date: 13, 12, 2025
# By: Lewis Burt
''' This is the player class. '''

# Imports:
import os
os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
from .base_object_class import BaseObjectClass
from ...file_importer import colours


class PlayerClass(BaseObjectClass):
    """ The player class for the game.
    Based on The BaseObjectClass. """
    def __init__(self, game_class, coordinates, stats=None, img=None):
        self.stats = stats
        self.game = game_class
        self.groups = game_class.all_sprites
        self.image = self.set_image(img)
        super().__init__(self.game, coordinates, self.set_colour(colours.BEEFBLUE), img=self.image)


    def move(self, dx=0, dy=0):
        """ Moves the player in the x and y coordinates. """
        self.x += dx
        self.y += dy


    def update(self):
        """ Get's the parent update. """
        return super().update()
