# Start date: 12, 12, 2025
# By: Lewis Burt
''' This is the executable file. '''

# Imports:
from python_files.file_importer import GameClass

# Main lines:
game_class = GameClass()

game_class.show_start_screen()

while game_class.running:
    game_class.new_game()
    game_class.show_game_over_screen()
