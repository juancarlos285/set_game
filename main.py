import random

numbers = [1, 2, 3]
shadings = ['solid', 'striped', 'open']
shapes = ['squiggle', 'diamond', 'oval']
colors = ['green', 'purple', 'red']

deck = []

for number in numbers:
    for shading in shadings:
        for shape in shapes:
            for color in colors:
                deck.append((number, shading, shape, color))
