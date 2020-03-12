from item import Item
from item import Food

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("You cannot move in that direction")
    def print_inventory(self):
        if len(self.items) > 0:
            print("You are holding: ")
            for item in self.items:
                print(f'{item.name}: {item.description}')
        else:
            print("You have no items.")
    def eat(self, food_item):
        if isinstance(food_item, Food):
            print(f"You have eaten {food_item.name}")
            self.items.remove(food_item)
        else:
            print("You cannot eat that item!")
        
    def look(self):
        print(f"You are in {self.current_room.name}\n")
        print(f"{self.current_room.description}\n")
        if len(self.current_room.items) > 0:
            print("You see the following items:")
            for item in self.current_room.items:
                print(item.name)
    def take_item(self, taken_item):
        self.current_room.items.remove(taken_item)
        self.items.append(taken_item)
        print(f"You took the {taken_item.name}")
    def drop_item(self, dropped_item):
        self.current_room.items.append(dropped_item)
        self.items.remove(dropped_item)
        print(f"You dropped the {dropped_item.name}")
    def unlock(self, unlocked_room):
        self.current_room = unlocked_room
        print("You have used your key to unlock the door!")
        print("You step through but the door shuts behind you!")
        print(self.current_room)