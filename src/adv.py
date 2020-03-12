from room import Room
from player import Player
from item import Item
from item import Food

# list of items

rock = Item("rock", "This is a rock")
sandwich = Food("sandwich", "club sandwich", 50)
apple = Food("apple", "granny smith apple", 20)
key = Item("key", "this key looks secretive")
silver_coins = Item("silver coins", "a pile of silver coins!")
gold_coins = Item("gold coins", "a pile of gold coins!")
sword = Item("sword", "a badass sword")
painting = Item("painting", "a portrait of... you? Or is it a mirror?")
bones = Item("bones", "the skeletal remains of another adventurer")

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [rock]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [apple, sandwich]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [sword]),

    "secret_door": Room("Secret Door Room", """Before you stands an empty room with
a secret door! Perhaps it might unlock with a secret key?""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [key, gold_coins, silver_coins]),

    'enlightenment': Room("Room of enlightenment", """You have found the hidden room of enlightment!
There is no physical escape, only spiritual. Ascend or be trapped forever!""", [painting, bones])
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['secret_door']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['secret_door'].e_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Please enter your name: "), room['outside'])
print(player.current_room)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

valid_directions = ("n", "s", "e", "w")

while True:
    cmd = input("\n~~> ")
    if cmd == "q":
        print("Goodbye!")
        exit(0)
    elif cmd in valid_directions:
        player.travel(cmd)
    elif cmd == "i" or cmd == "inventory":
        player.print_inventory()
    elif cmd == "l" or cmd == "look":
        player.look()
    elif "take" in cmd or "get" in cmd:
        if len(player.current_room.items) > 0:
            for item in player.current_room.items:
                if item.name in cmd:
                    player.take_item(item)
        else:
            print("There are no items in this room to take!")
    elif "drop" in cmd or "get" in cmd:
        if len(player.items) > 0:
            for item in player.items:
                if item.name in cmd:
                    player.drop_item(item)
        else:
            print("There are no items in your inventory to drop!")
    elif "eat " in cmd:
        if len(cmd[4:]) > 0:
            if len(player.items) > 0:
                if " " in cmd[4:]:
                    print("Please specify ONE thing that you would like to eat.")
                else:
                    for item in player.items:
                        if item.name in cmd[4:]:
                            player.eat(item)
            else:
                print("You have no items in your inventory.")
        else:
            print("Please specify what you would like to eat.")
    elif "unlock" in cmd:
        if player.current_room == room["secret_door"]:
            if key in player.items:
                player.unlock(room['enlightenment'])
            else:
                print("You don't have the key for this door.")
        else:
            print("There is nothing to unlock!")
    elif "meditate" in cmd or "ascend" in cmd or "pray" in cmd:
        if player.current_room == room['enlightenment']:
            if len(player.items) == 0:
                print("You cast off all of your material possessions and attempt to focus your spirit.")
                print("The heavens open and you leave behind your physical body as you transcend into a higher plain of existence.")
                print("You feel at one with all things. You have achieved true enlightenment! Congratulations!")
                print("Then end!")
                exit(0)
            else:
                print("You try to ascend... but to no affect!")
        else:
            print("Now is not the time for that!")
    else:
        print("I did not understand that command")
