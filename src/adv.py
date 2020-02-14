from room import Room
from player import Player
from item import Item
# Declare all the rooms

# items = {
#     'potion': Item("a potion", """Heals your wounds"""),
#     'sword': Item("a sword", """To fight the bad guys"""),
#     'shoe': Item("an old shoe", """Looks like someone left this here"""),
#     'reward': Item("gold", """Congratulations!"""),
# }

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons.""",Item("No items", """---""")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("a potion", """Heals your wounds""")), 

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("a sword", """To fight the bad guys""")), 

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("an old shoe", """Looks like someone left this here""")), 

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item("gold", """Congratulations!""")), 
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#
print("\nWelcome to adventure time!\n")
# Make a new player object that is currently in the 'outside' room.
player = Player(input("\nName: "), room['outside'], '')

# Write a loop that:

player.items = []   
print("\n\nWelcome", player.name)

# def on_take(item):
#     if 
while True: 

    print("\nYour position is currently: ", player.current_room.name)
    print("\nThe description of your surroundings is: ", player.current_room.description)
   
    choice = input("\n\nPlease enter [n] North   [s] South  [e] East  [w] West to move or  [q] Quit \n")


    
    if choice == 'n':
        if player.current_room.n_to is not None:
            print("\nYou moved north!\n")
            
            player.current_room = player.current_room.n_to
            print("This room has a: ", player.current_room.item)
        
        else: 
            print("You're going the wrong way! Try again.")
    elif choice == 's':
        if player.current_room.s_to is not None:
            print("\nYou moved south!\n")
            
            player.current_room = player.current_room.s_to
            print("Item: ", player.current_room.item)
        else: 
            print("\nYou're going the wrong way! Try again.")
    elif choice == 'e':
        if player.current_room.e_to is not None:
            print("\nYou moved east!\n")
            
            player.current_room = player.current_room.e_to
            print("Item: ", player.current_room.item)
        else: 
            print("\nYou're going the wrong way! Try again.")
    elif choice == 'w':
        if player.current_room.w_to is not None:
            print("\nYou moved west!\n")
           
            player.current_room = player.current_room.w_to
            print("Item: ", player.current_room.item)
        else: 
            print("\nYou're going the wrong way! Try again.")
    elif choice == 'take':
        player.items.append(player.current_room.item.name)
        del player.current_room.item
        print("You took an item!")

    elif choice == 'my items' or choice == 'i':
        stuff = ""+", ".join(player.items)
        print(f"\nYour items: {stuff}")
    elif choice == 'q':
        print("\nThanks for playing!\n")
        break
    else: 
        print("\nInvalid input, please use 'n', 's', 'e', 'w")


