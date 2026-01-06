# Start date: 13, 12, 2025
# By: Lewis Burt
''' This is a character base class. '''

# Imports:
import os
os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
from ...file_importer import PG, dev_settings, colours



class BaseObjectClass(PG.sprite.Sprite):
    """ The basics of every object in the game. """
    def __init__(self, game_class, coordinates, img = None, dimensions = None):
        self.groups = game_class.all_sprites
        PG.sprite.Sprite.__init__(self, self.groups)
        self.game = game_class
        # For images:
        self.image = self.set_image(image=img, dimensions=dimensions)
        if img is None:
            self.image.fill(colours.BEEFBLUE)
        # For rect and location:
        self.rect = self.image.get_rect()
        self.x, self.y = coordinates[0], coordinates[1]
        self.rect.x = self.x * dev_settings.TILESIZE
        self.rect.y = self.y * dev_settings.TILESIZE


    def set_image(self, image, dimensions):
        """ Sets the image of the sprite. """
        if image is not None:
            c_image = image
        else:
            if dimensions is not None:
                c_image = PG.Surface((dimensions))
            else:
                c_image = PG.Surface((dev_settings.TILESIZE, dev_settings.TILESIZE))
        return c_image


    def update(self):
        """ Updates the sprite. """
        self.rect.x = self.x * dev_settings.TILESIZE
        self.rect.y = self.y * dev_settings.TILESIZE
