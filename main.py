from i18n import Translator

def main():

    directions = ('east', 'west', 'north', 'south')
    darug_directions = ('buruwi', 'bayinmarri', 'buruwan', 'balgayalang')
    
    locations = ('sea', '', '', '')
    darug_locations = ('garrigarrang', '', '', '')

    motion = ('pick up', 'play', 'look')
    darug_motion = ('manyu', 'dyanmila', 'ngalga') 

    places = ()
    darug_places = ()

    items = ()
    darug_items = ()

    crafting = ()
    darug_crafting = ()

    current_location = 1
    locations = {
        1: (),
        2: (),
        3: (),
        4: ()
    }
    map = [1, [2, 3, 4], 2, [1, 4], 3, [1, 4], 4, [1, 2, 3]]

    def format(key: str) -> str:
        answer = translator.translate(key)
        return f"{answer[0]} ({answer[1]})"

    translator = Translator('data/')
    translator.set_locale('darug')
    quit = False
    while not quit:
        print(f"{format('you')} {format('stand')} {format('this side of the river')} called the {format('Hawkesbury River')} and see no way to cross.")

        return

if __name__ == '__main__':
    main()