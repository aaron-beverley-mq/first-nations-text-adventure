from i18n import Translator

# Words, locations and crafting ideas are sourced from The Sydney Language by Jakelin Troy (1993)
# and https://dharug.dalang.com.au/language/dictionary. Note, the story is fictitional but
# tries to respect the traditional owners of the Darug Country and created to enhance students 
# understading of the history of the First Nations people.
locations = {
    # location, directions, items, text
    1: ('Hawkesbury River', ['east', 'west', 'south'], ['river', 'perch', 'sandstone'], ['you', 'stand', 'this side of the river', 'called the', 'Hawkesbury River', 'and see no way to cross.']),
    2: ('Blue Mountains', ['east', 'south'], ['grass trees', 'kangaroo', 'wood'], ['As you climb the hills you see a vast mountain range.']),
    3: ('Manly Bay', ['west', 'south'], ['sea', 'stingray'], ['The sea crashes into the cliffs and there are quieter bays with pools of water']),
    4: ('Macquarie Park', ['north', 'east', 'west'], ['reeds', 'root vegetables'], ['Wandering along a track you come upon a lake with signs of animal tracks leading west']),
    5: ('Parramatta', ['north', 'east'], ['grass', 'yam', 'wallaby'], ['Stumbling through the trees you come across a fertile area covered in grass and yams'])
}

map = {1: [3, 2, 4], 2: [1, 5], 3: [1, 4], 4: [1, 3, 5], 5: [2, 4]}
crafting = {
    'fishhook': ['sandstone'],
    'fishing line': ['shrub bark'],
    'fish gigs': ['bone', 'spiral shoot', 'gum'],
    'boomerang': ['wood'],
}

hunting = {
    'kangaroo': ['leather', 'bone', 'meat'],
    'wallaby': ['leather', 'bone', 'meat'],
}

harvesting = {
    'shrub': ['shrub bark'],
    'grass tree': ['gum', 'spiral shoot'],
    'wood': ['wood'],
    'yam': ['food'],
    'sandstone': ['sandstone'],
    'river': ['water'],
    'sea': ['salt water']
}

fishing = {
    'perch': ['meat', 'bones']
}

def main():

    directions = ('east', 'west', 'north', 'south')
    darug_directions = ('buruwi', 'bayinmarri', 'buruwan', 'balgayalang')
    
    inventory = []

    current_location = 1

    def format(key: str) -> str:
        answer = translator.translate(key)
        return f"{answer[0]} ({answer[1]})"

    translator = Translator('data/')
    translator.set_locale('darug')
    quit = False

    print("Welcome to Darug Country. You are welcome to explore the area and try different activities. Please only use what you need and respect the land.")
    print("Your actions will include: [look, take, fish, hunt, bag]. While directions are [east, west, north, south]. 'q'uit to leave the game.")
    print("These can also be done using the language of the Darug people. \n\tActions: [ngalga, maan, maugra, wulbung, djuguma]. \n\tDirections: [buruwi, bayinmarri, buruwan, balgayalang]")
    print("\n")
    while not quit:
        print_location(current_location, translator)
        darug_dirs = []
        for item in locations[current_location][1]:
            darug_dirs.append(translator.translate(item)[0])
        print(f"Directions to can go are: {locations[current_location][1]} {darug_dirs}")

        command = input("> ")
        if (command in ['q', 'quit']):
            return
        
        commands = command.split(' ')
        # movement
        if (commands[0] in directions + darug_directions):
            loc = locations[current_location]
            darug_dirs = []
            for index, val in enumerate(loc[1]):
                if val == commands[0]:
                    current_location = (map[current_location][index])
                    continue
                darug_dirs.append(translator.translate(val)[0])
            for index, val in enumerate(darug_dirs):
                if val == commands[0]:
                    current_location = (map[current_location][index])
                    continue            
        elif commands[0] in ['look', 'ngalga']:
            loc = locations[current_location]
            darug_items = []
            for item in loc[2]:
                darug_items.append(translator.translate(item)[0])
            print(f"You see the following around you: {loc[2]} {darug_items}")
        elif commands[0] in ['take', 'maan']:
            loc = locations[current_location]
            if len(commands) == 1:
                print(f"What do you want to '{commands[0]}'")
            elif commands[1] in loc[2]:
                inventory.append(commands[1])
                loc[2].remove(commands[1])
            darug_items = []
            for item in loc[2]:
                darug_items.append(translator.translate(item)[0])
            print(f"You see the following around you: {loc[2]} {darug_items}")
        elif commands[0] in ['fish', 'maugra']:
            loc = locations[current_location]
            if len(commands) == 1:
                print(f"What do you want to '{commands[0]}'?")
            elif commands[1] not in fishing:
                print(f"You cannot fish for {commands[1]}")
            elif commands[1] in loc[2]:                
                print(f'You caught a {commands[1]}')
                for item in fishing[commands[1]]:
                    inventory.append(item)
            else:
                print(f"No '{commands[1]}' here to catch")
        elif commands[0] in ['hunt', 'wulbung']:
            loc = locations[current_location]
            if len(commands) == 1:
                print("What do you want to hunt?")
            elif commands[1] not in hunting:
                print(f"You cannot hunt {commands[1]}")
            elif commands[1] in loc[2]:                
                print(f"You hunted a {commands[1]}")
                for item in hunting[commands[1]]:
                    inventory.append(item)
            else:
                print(f"No {commands[1]} here to hunt")
        elif commands[0] in ['make', 'bangawarra']:
            if len(commands) == 1:
                print("What do you want to make?")
            elif commands[1] in crafting:
                craft_need = crafting[commands[1]]
                if all(elements in inventory for elements in craft_need):
                    print(f"You made a {commands[1]}")
                    for item in craft_need:
                        inventory.remove(item)
                    inventory.append(commands[1])
                else:
                    print(f"You are missing items to craft: {commands[1]}")
            else:
                print(f"{commands[1]} does not exist.")
        elif commands[0] in ['bag', 'djuguma']:
            print(f"Your bag contains: {inventory}")
            print(f"Crafting requirements are:")
            for key, value in crafting.items():
                print(f"\t{key} {value}")
        elif commands[0] == 'help':
            print('help')
       
    print("Thanks for play, I hope you enjoyed exploring Darug Country.")
    
def format(answer: tuple) -> str:
    return f"{answer[0]} ({answer[1]})"

def print_location(index: int, translator: Translator) -> None:
    loc = locations[index]
    sentence = "< "
    for word in loc[3]:
        translate = translator.translate(word)
        sentence += (format(translate), translate[1]) [translate[0] is None] + " "
    print(sentence)

if __name__ == '__main__':
    main()