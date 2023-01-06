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

sample = random.sample(deck, 12)

print(sample)

def print_combinations(iterable, k):
    combinations = []
    def comb_generator(start, comb=list):
        if len(comb) == k:
            combinations.append(comb.copy())
            return
        for i in range(start, len(iterable)):
            comb.append(i)
            comb_generator(i + 1, comb)
            comb.pop()

    comb_generator(0, [])
    return combinations

cards_indexes = [i for i, card in enumerate(sample)]

index_combinations = print_combinations(cards_indexes, 3)

for x in index_combinations:
    card_a = sample[x[0]]
    card_b = sample[x[1]]
    card_c = sample[x[2]]

    if card_a[0] == card_b[0] and card_a[0] == card_c[0] or card_a[0] != card_b[0] and card_a[0] != card_c[0] and card_b[0] != card_c[0]:
        if card_a[1] == card_b[1] and card_a[1] == card_c[1] or card_a[1] != card_b[1] and card_a[1] != card_c[1] and card_b[1] != card_c[1]:
            if card_a[2] == card_b[2] and card_a[2] == card_c[2] or card_a[2] != card_b[2] and card_a[2] != card_c[2] and card_b[2] != card_c[2]:
                if card_a[3] == card_b[3] and card_a[3] == card_c[3] or card_a[3] != card_b[3] and card_a[3] != card_c[3] and card_b[3] != card_c[3]:
                    print(f"{sample.index(card_a)}: {card_a}\n{sample.index(card_b)}: {card_b}\n{sample.index(card_c)}: {card_c}")
                    break
    if x == len(index_combinations) - 1:
        print("no set found")