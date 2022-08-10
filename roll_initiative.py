#!/usr/bin/env python3

import sys

player_dict = {}

# creates the menu
def menu():

    option = input('Choose an option: 1 - Add a player/roll, 2 - Print Order, Q - Quit: ')
    return option

# gets a player/NPC name 
def get_player():
    
    player = input('Enter player/NPC name (Q to quit): ')
    return player

# gets a player/NPC initiative roll
def get_roll():
    
    roll = input('Enter initiative rolled (numbers only): ')
    
    while roll.isdigit() == False:
            roll = input('Please enter numbers only: ')
    
    # convert roll to integer for sorting later on
    roll = int(roll)
    return roll

# adds the player name and their roll to the player_dict dictionary
def update_dict(player, roll):

    player_dict.update({player: roll})

# have the menu running as the default behaviour

menu_running = True
print('==================================')
print('ROLL INITIATIVE')
print('==================================\n\n')
# display menu and pass input to option variable
while menu_running:
    option = menu()

    # user has chosen to add a player
    while option == '1':
        
        # if player wants to quit from add player loop
        player = get_player()
        if player == 'Q' or player == 'q':
            break

            
        roll = get_roll()
        update_dict(player, roll)
        
    # user wants to print sorted results 
    while option == '2':

        # make a list out of the dictionary to pass into sort, by the second index i.e. roll
        player_list = list(player_dict.items())
        player_list.sort(key=lambda lst: lst[1], reverse=True)
        
        print('==================================')
        for player, roll in player_list:
            print(f'\n - {player} (rolled {roll})\n')
            print('==================================')
        break 

    # Close app
    while option =='Q' or option == 'q':
       menu_running = False  
       sys.exit()
