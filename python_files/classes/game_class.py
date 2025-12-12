# Start date: 12, 12, 2025
# By: Lewis Burt
''' This is the Game class.
The game needs this to run. '''

import os
os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
from python_files.file_importer import PG, dev_settings, sys, Defaults, colours

class GameClass():
    """ The main class for my game. """
    def __init__(self):
        # Initialises the game:
        PG.init()
        PG.mixer.init()
        self.screen = PG.display.set_mode((Defaults.WIDTH, Defaults.HEIGHT))
        PG.display.set_caption(dev_settings.TITLE)
        # Ready for updates:
        self.clock = PG.time.Clock()
        self.running = True
        self.playing = True
        # Groups:
        self.all_sprites = None


    def new_game(self):
        """ Starts a new game. """
        self.all_sprites = PG.sprite.Group()
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


    def game_draw(self):
        """ Used for drawing the game. Executed at the end of every frame. """
        self.screen.fill(colours.BLACK)
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
