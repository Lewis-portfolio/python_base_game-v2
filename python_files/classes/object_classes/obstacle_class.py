# Start date: 20, 01, 2026
# By: Lewis Burt
''' This is the wall class. '''

# Imports:
import os
os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
from .base_object_class import BaseObjectClass
from ...file_importer import colours


class ObsticalClass(BaseObjectClass):
    """ The Obsticales for the game.
    Based on The BaseObjectClass. """
    def __init__(self, game_class, coordinates, img=None, dimensions=None):
        self.game = game_class
        self.groups = game_class.all_sprites, game_class.obsticles
        self.image = self.set_image(img, dimensions)
        super().__init__(self.game, coordinates, self.set_colour(colours.GREEN), img=self.image)
