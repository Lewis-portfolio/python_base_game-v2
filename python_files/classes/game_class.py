# Start date: 12, 12, 2025
# By: Lewis Burt
''' This is the Game class.
The game needs this to run. '''

import os
os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
from ..file_importer import PG, dev_settings, sys, Defaults, colours
from .debug_class import DebuggingClass
from .object_classes.player_class import PlayerClass
from .object_classes.base_object_class import BaseObjectClass

class GameClass():
    """ The main class for my game. """
    def __init__(self):
        # Initialises the game:
        PG.init()
        PG.mixer.init()
        self.screen = PG.display.set_mode((Defaults.WIDTH, Defaults.HEIGHT))
        PG.display.set_caption(dev_settings.TITLE)
        # Initialises the sub classes:
        self.debug_class = DebuggingClass(self)
        self.player = None
        # Ready for updates:
        self.clock = PG.time.Clock()
        self.running = True
        self.playing = True
        # Groups:
        self.all_sprites = None


    def new_game(self):
        """ Starts a new game. """
        self.all_sprites = PG.sprite.Group()
        self.player = PlayerClass(self, (2, 3))
        self.run_game()


    def run_game(self):
        """ Runs the game loop. """
        while self.playing:
            self.clock.tick(Defaults.FPS)
            self.game_events()
            self.game_updates()
            self.game_draw()


    def game_updates(self):
        """ Used when the game loops. It's for general updates. """
        self.all_sprites.update()


    def game_events(self):
        """ Used for game event updates. """
        for event in PG.event.get():
            # Checks if the window is closing:
            if event.type == PG.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == PG.KEYDOWN:
                if event.key == PG.K_ESCAPE:
                    self.quit_game()
                if event.key == PG.K_LEFT:
                    self.player.move(dx = -1)
                if event.key == PG.K_RIGHT:
                    self.player.move(dx = 1)
                elif event.key == PG.K_UP:
                    self.player.move(dy = -1)
                elif event.key == PG.K_DOWN:
                    self.player.move(dy = 1)


    def game_draw(self):
        """ Used for drawing the game. Executed at the end of every frame. """
        self.screen.fill(colours.BLACK)
        self.debug_class.draw_grid()
        self.all_sprites.draw(self.screen)

        # Right at the end:
        PG.display.flip()


    def quit_game(self):
        """ Quits the game. """
        PG.quit()
        sys.exit()


    def show_start_screen(self):
        """ Shows the start screen. """


    def show_game_paused_screen(self):
        """ Shows the paused screen. """


    def show_game_over_screen(self):
        """ Shows the game over screen. """
