import pandas as pd
import numpy as np


def output(d):
    for k, v in d:
        print(k)
        print(v)


suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10] * 3) * 4
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
cards = []
for suit in ['H', 'S', 'C', 'D']:
    cards.extend(str(num) + suit for num in base_names)
deck = pd.Series(card_val, index=cards)


def draw(deck, n=5):
    return deck.sample(n)


draw(deck)

# Series.groupby()是以Series的index值作为关键字分组
get_suit = lambda card: card[-1]
output(deck.groupby(get_suit))
output(deck.groupby())
