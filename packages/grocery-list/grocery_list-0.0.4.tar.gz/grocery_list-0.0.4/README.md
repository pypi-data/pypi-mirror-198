# grocery-list

`pip install grocery-list`

Silly package to compile a shopping list.

The ingredients dictionary's keys are categories (e.g., fruits, vegetables, bakery, etc.) and their values are lists of shopping items (e.g., apple, potato, bread, etc.). A second dictionary contains recipes whose keys are the name of a meal and whose values are lists of ingredients, each of which can be a shopping item or another recipe.

Just fork and edit `ingredients.py` and `recipes.py` as you wish.

Example:
```
from grocery_list import *
grocery_list('beans on toast')
```

Output: `{'bakery': ['bread'], 'dairy': ['butter'], 'tins': ['baked beans']}`
