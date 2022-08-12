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
}

# Define functions to happen during execution 
def display_current_place():
    """
    Get the current setting and return the descriptor of 
    """
    global game_state
    
    return game_places[game_state]['Description']

def make_a_window():
    """
    Creates a game window
    """
    sg.theme('Dark Blue 3')  # please make your windows 
    prompt_input = [sg.Text('Enter your command',font='Any 14'),sg.Input(key='-IN-',size=(20,1),font='Any 14')]
    buttons = [sg.Button('Enter',  bind_return_key=True), sg.Button('Exit'), sg.Radio('Permission Granted', "Option1", default=False),sg.Radio('Permission not Granted', "Option2", default=False),sg.Radio('Permission not Granted', "Option3", default=False)]
    command_col = sg.Column([prompt_input,buttons],element_justification='r')
    layout = [[sg.Text('Description:', size=(7,1), font='Any 14'), sg.Text(display_current_place(),size=(100,4), font='Any 14', key='-OUTPUT-')],
             [command_col]]

    return  sg.Window('Prison Game', layout, size=(800,500), resizable=True)
def game_play(option):
    """
    Runs the game_play
    """
    global game_state
    

    game_place = game_places[game_state]
    proposed_state = game_place[option]
    if option == 1:
        game_places[game_state]['Description']
        return game_places[game_state]['Description']
    elif option == 2:
        game_state = proposed_state
        return game_places[game_state]['Description']
    elif option == 3:
        return game_places[game_state]['Description']
    else:
        return 'Please select a single option'+game_places[game_state]['Description']
    
        
# Define main function with while loop that continually revolves around the case of a button
# being pressed and the value of radio buttons being selected 
if __name__ == "__main__":
    #testing for now
    # print(show_current_place())
    # current_story = game_play('North')
    # print(show_current_place())
    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()
    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        if event ==  'Enter': 
                if 'Option1'.lower() in values['-IN-'].lower():
                    current_story = game_play('Option1')
                    window['-OUTPUT-'].update(current_story)
                elif 'Option2'.lower() in values['-IN-'].lower():
                    current_story = game_play('Option2')
                    window['-OUTPUT-'].update(current_story)
                elif 'Option3'.lower() in values['-IN-'].lower():
                    current_story = game_play('Option3')
                    window['-OUTPUT-'].update(current_story)
                pass

    window.close()

