import sys


ingredients = {
    'bakery': [
        'bread',
        ],

    'tins': [
        'baked beans',
        ],

    'dairy': [
        'butter',
        ],
    }


recipes = {
    'beans on toast': [
        'bread',
        'baked beans',
        'butter',
        ],
    }


def find_ingredient(ingredient):

    for place in ingredients:
        if ingredient in ingredients[place]:
            return place
    raise ValueError(f'Ingredient not found: {ingredient}')


def add_ingredient(item, groceries):

    if item in recipes:
        for ingredient in recipes[item]:
            groceries = add_ingredient(ingredient, groceries)
    else:
        place = find_ingredient(item)
        if place not in groceries:
            groceries[place] = []
        if item not in groceries[place]:
            groceries[place].append(item)
            
    return groceries


def grocery_list(*items):

    groceries = {}
    for item in items:
        if item not in sum(list(groceries.values()), []):
            groceries = add_ingredient(item, groceries)
            
    for place in groceries:
        groceries[place] = sorted(groceries[place])

    return {key: groceries[key] for key in sorted(groceries)}


def main():

    groceries = grocery_list(*sys.argv[1:])
    for place in groceries:
        print(place)
        for ingredient in groceries[place]:
            print('\t' + ingredient)
        print()


if __name__ == '__main__':

    main()

