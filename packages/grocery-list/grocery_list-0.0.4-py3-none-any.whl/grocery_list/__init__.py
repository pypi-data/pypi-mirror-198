import sys

from .ingredients import ingredients
from .recipes import recipes
from .grocery_list import grocery_list


def main():

    groceries = grocery_list(*sys.argv[1:])
    for place in groceries:
        print(place)
        for ingredient in groceries[place]:
            print('\t' + ingredient)
        print()


if __name__ == '__main__':

    main()

