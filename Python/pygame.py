import sys

# Define the rooms and their connections
rooms = {
    'Entrance': {'north': 'Living Room', 'east': 'Kitchen'},
    'Living Room': {'south': 'Entrance', 'west': 'Bedroom'},
    'Kitchen': {'west': 'Entrance'},
    'Bedroom': {'east': 'Living Room'}
}

# Current room
current_room = 'Entrance'

while True:
    print(f'You are in the {current_room}')

    # Get user input
    action = input('What do you want to do? (Enter a direction or "quit"): ').lower()

    if action == 'quit':
        print('Goodbye!')
        sys.exit(0)
    elif action in rooms[current_room]:
        current_room = rooms[current_room][action]
    else:
        print('You can\'t go that way!')