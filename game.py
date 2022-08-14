"""
Game activity for SDV602, playing with the functionality of pysimpleGUI 
Hamash, mort 
"""
# Add image to dictionary
#figure was to apply radio button option
import PySimpleGUI as sg

# Define game states to declare locations and track interaction
visit = 0
game_state = 'Prison'
game_places =   {'Prison':{'Description':'You are in a prison, you can escape(1)\n or stay(2), enter your decision',
                        '1':'Hallway','2':'End'},
                 'Prison2':{'Description':'Welcome back to your cell!!!, escape(1)\n or stay(2), enter your decision',
                        '1':'Hallway','2':'End'},
                'Hallway':{'Description':'You enter the hallway,\n to your left is a room with the door ajar,\n would you like to enter(1) or continue down the hallway(2)?',
                        '1':'Room', '2':'Guard'},
                'End':{'Description':'You were caught, try again(1)',
                        '1':'Prison2' },
                'Room':{'Description':'You enter the room, there is a knife on the ground,\n pick it up(1) or leave it(2)?',
                        '1':'Guard vs Knife', '2':'Guard'},
                'Guard':{'Description':'You are confronted by a guard,Attack the guard with your hands(1)\n or continue running(2)?',
                        '1':'Grab keys', '2':'End'},
                'Guard vs Knife':{'Description':'You are confronted by a guard, use the knife(1)?\n Attack the guard with your hands(2)\n or continue running(3)?',
                        '1':'Grab keys', '2':'Grab keys', '3':'End'},
                'Grab keys':{'Description':'Would you like to go through the main gate(1) or the sewer(2)?',
                        '1':'End', '2':'Landing pad'},
                'Landing pad':{'Description':'You are on the landing pad, would you like to stow away on the ship(1)\n or run into the forest(2)?',
                        '1':'Ship', '2':'Forest'},
                'Ship':{'Description':'Ship lands on new planet, would you like to stay on the ship(1)\n or live the remainder of your criminal life on this docile planet(2)?',
                        '1':'Travel', '2':'Live'},
                'Travel':{'Description':'You join a band of mercenaries(1)',
                        '1':'Prison2' },
                'Live':{'Description':'You live a happy life and raise a happy criminal family(1)',
                        '1':'Prison2'},
                'Forest':{'Description':'The guards are chasing you, run(1) or hide(2)?',
                        '1':'Cliff', '2':'End'},
                'Cliff':{'Description':'You have come to a cliff, would you like to jump(1)\n or surrender(2)?', 
                        '1':'End', '2':'End'}
}
knife = False

def dice_roll():
    """
    Rolls a die and returns the result
    """
    import random
    return random.randint(1,6)

dice = dice_roll()

# Define functions to happen during execution 
def display_current_place():
    """
    Get the current setting and return the descriptor of 
    """
    global game_state
    
    return game_places[game_state]['Description']

def game_play(option):
        """
                Runs the game_play

                Args:
                direction string: _North or South

                Returns:
        string: the sory at the current place
        """ 
        global game_state
        global dice
        global visit
        

        if 'Guard' in game_state and option == '1' and dice <= 6:
            return game_places['Prison2']['Description']
        
        if 'Prison' in game_state or 'Prison2' in game_state:
                visit = visit + 1
                pass
        
        if 'Prison' in game_state or 'Prison2' in game_state:
                sg.popup('You have visited {} times!!!', visit)
        
        if option.lower() in '123': # is this a nasty check?
                game_place = game_places[game_state]
                proposed_state = game_place[option]
        if proposed_state == '' :
            return 'You can not go that way.\n'+game_places[game_state]['Description']
        else :
            game_state = proposed_state
            return game_places[game_state]['Description']

def make_a_window():
        """
        Creates a game window
        """
        sg.theme('Dark Blue 3')  # please make your windows
        prompt_input = [sg.Text('Enter your command',font='Any 14'),sg.Input(key='-IN-',size=(20,1),font='Any 14')]
        buttons = [sg.Button('Enter',  bind_return_key=True), sg.Button('Exit')]
        #sg.Radio('Permission Granted', "Option1", default=False),sg.Radio('Permission not Granted', "Option2", default=False),sg.Radio('Permission not Granted', "Option3", default=False)
        command_col = sg.Column([prompt_input,buttons],element_justification='r')
        layout = [[sg.Text('Description:', size=(7,1), font='Any 14'), sg.Text(display_current_place(),size=(100,4), font='Any 14', key='-OUTPUT-')],
        [command_col]]
        return  sg.Window('Prison Game', layout, size=(800,500), resizable=True)


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
                if '1'.lower() in values['-IN-'].lower():
                    current_story = game_play('1')
                    window['-OUTPUT-'].update(current_story)
                elif '2'.lower() in values['-IN-'].lower():
                    current_story = game_play('2')
                    window['-OUTPUT-'].update(current_story)
                elif '3'.lower() in values['-IN-'].lower():
                    current_story = game_play('3')
                    window['-OUTPUT-'].update(current_story)
                pass

    window.close()

