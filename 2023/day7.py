import math
from enum import Enum


class ordering(Enum):
    normal = "AKQJT98765432"
    jokers = "AKQT98765432J"


def entropy(hcards):
    """
    The method entropy takes a list of cards (hcards) as an input and returns the entropy of the cards as a float.
    The entropy is a measure of the uncertainty or randomness of the cards. The higher the entropy, the more diverse
    the cards are. The lower the entropy, the more similar the cards are.

    Precondition: hcards is a non-empty list of hashable values

    Postcondition: returns a float that is the entropy of hcards

    :param hcards a non-empty list of hashable values:

    :return: a float that is the entropy of hcards
    """
    return -sum(map(
        lambda p: p * math.log(p),
        [
            hcards.count(c) / len(hcards)
            for c in set(hcards)
        ],
    ))


def entropy_with_jokers(hcards):
    """
    :param hcards: a non-empty list of hashable values, possibly containing "J" as jokers
    :return: a float that is the entropy of hcards, treating jokers as the most frequent card
    """
    # Requires: hcards is a non-empty list of hashable values, possibly containing "J" as jokers
    # Ensures: returns a float that is the entropy of hcards, treating jokers as the most frequent card
    try:
        top = sorted(
            hcards.replace("J", ""),
            key=lambda c: hcards.count(c),
        )[-1]
        return entropy(hcards.replace("J", top))
    except IndexError:
        return entropy(hcards)


with open("day7.txt") as src:
    hands = [
        (h, int(b))
        for h, b in map(str.split, src)
    ]

print("Part one answer:", sum([
    (len(hands) - i) * bid
    for i, (__, bid) in enumerate(sorted(
        hands,
        key=lambda h: (
            entropy(h[0]),
            *map(ordering.normal.value.index, h[0])),
    ))
]))

print("Part two answer:", sum([
    (len(hands) - i) * bid
    for i, (__, bid) in enumerate(sorted(
        hands,
        key=lambda h: (
            entropy_with_jokers(h[0]),
            *map(ordering.jokers.value.index, h[0]),
        )
    ))
]))
