# Changes on 20, 01, 2026:
### Overview:
Alot has changed in this update. So far the Obstacles have no collisions.
### Added:
- #### Classes:
  - Added a new class for Obstacles along with it's calling in the game class.
  - Game class:
    - Added a line to make sure that the player doesn't have to spam keys to move.
    - Added a couple comments in areas to help with information.
  - Base object class:
    - Added a set color function to set a color of a sprite (might have to change behaviour later)
### Changed:
- #### Classes:
  - Player class:
    - The spacing in the parameters with defaults.
  - Game class:
    - Changed how the keybinds work so that the player can use both the arrow keys and WASD keys depending on their preference.
      - This is subject to change on how a dev or player could change keybinds.
  - Base object class:
    - The following changes were required to allow for larger and diffrent shaped sprites
      - correting the set image definition to default dimensions to None
      - Checking if the image is an instance of a surface before applying a fill - Might need to edit this behaviour in the future.
- Misc:
  - Changed where the groups are located (in individual classes)

### Removed:
Removed an unnessicary call of the base object class in the game class.  
Removed an unnessicary dimensions parameter in the initialiser of the base object class and player class. 
##

# Changes on 16, 01, 2026:
### Overview:
I fixed a typo, updated the readme, and removed an old system.
### Added:
Nothing.
### Changed:
Fixed the date of the previous changelog. Correcting it to the correct year.  
Updated the read me.
### Removed:
Removed the old changelog system as it's no longer going to be used.
##
# Changes on 27, 12, 2025:
Added, changed and removed things in this update.
Also forgot to push it to github.
### Added:
- Added a new changelog system.
- Added several new classes to the file systems.
- #### Classes:
  - Player class:
    - This class is so that the player can interact with the game.
  - Debug class:
    - This class is to help with debugging of the game.
### Changed:
- Game class:
  - Changed numerous methods to allow for the game to be ran until the user exits.
- Tile sizing:
  - Changed from "*" to "/"

### Removed:
- From - main file:
  - Removed a commented out section of code.

##
# Changes on 12, 12, 2025:
I only added things in this changelog
### Added:
- Added several foldders and files for the game.
- #### Folders:
  - A Changelogs folder for changelogs.  
  - A imgs folder ready for images.  
  - A snds folder ready for sounds.  
  - A saves folder ready for saves.  
  - A python files folder to handle all python files except for the main file:  
    - This contains the subfolders for classes and misc_files.  
- #### Misc:
  - The main executable which is ran to start the game.
  - A file importer that imports the other files (Subject to change).
  - A colours file for game colours.
  - A default settings file that currently handles the settings that I will want the player to be able to change.
  - A dev settings file that will handle the settings that players shouldn't be able to change.
- #### Classes:
  - A base object class to handle the common code for every asset.

##
# The initial commit:
The creation of the initial project.
##
