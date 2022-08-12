"""
Game activity for SDV602, playing with the functionality of pysimpleGUI 
Hamash, mort 
"""
import PySimpleGUI as sg

# Define game states to declare locations and track interaction 
game_state = 'Prison'
game_places =   {'Prison':{'Description':'You are in a prison, you can escape or stay, enter your decision',
                        'Escape':'Hallway','Stay':'End'},
                'Hallway':{'Description':'You enter the hallway, to your left is a room with the door ajar, would you like to enter or continue down the hallway?',
                        'Enter':'Room', 'Continue':'Guard'},
                'End':{'Description':'You were caught',
                        '':'Prison' },
                'Room':{'Description':'You enter the room, there is a knife, pick it up?',
                        'Yes':'Guard', 'No':'Guard'},
                'Guard':{'Description':'You are confronted by a guard, use the knife? Attack the guard or continue running?',
                        'Knife':'Grab keys', 'Attack':'Grab keys', 'Continue':'End'},
                'Grab keys':{'Description':'Would you like to go through the main gate or the sewer?',
                        'Main gate':'End', 'Sewer':'Landing pad'},
                'Landing pad':{'Description':'You are on the landing pad, would you like to stow away on the ship or run into the forest?',
                        'Stow away':'Ship', 'Forest':'Forest'},
                'Ship':{'Description':'Ship lands on new planet, would you like to stay on the ship or live the remainder of your criminal life on this docile planet?',
                        'Stay':'Travel', 'Planet':'Live'},
                'Travel':{'Description':'You join a band of mercenaries',
                        '':'Prison' },
                'Live':{'Description':'You live a happy life and raise a happy criminal family',
                        '':'Prison'},
                'Forest':{'Description':'The guards are chasing you, run or hide?',
                        'Run':'Cliff', 'Hide':'End'},
                'Cliff':{'Description':'You have come to a cliff, would you like to jump or surrender?', 
                        'Surrender':'End', 'Jump':'End'}
# Define functions to happen during execution 

# Define main function with while loop that continually revolves around the case of a button
# being pressed and the value of radio buttons being selected 