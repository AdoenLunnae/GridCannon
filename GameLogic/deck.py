# !/usr/bin/python
# -*- encoding:utf-8 -*-

from typing import List


class Suit:
    name: str
    color: int

    def __init__(self, name: str, color: int):
        self.name = name
        self.color = color


class Card:
    _value: int
    _suit: Suit
    def __init__(self, value: int, suit: Suit):
        self._value = value
        self._suit = suit
    
    def __repr__(self) -> str:
        result: str = ""
        if(self._value in range(2,11)):
            result += str(self._value)
        elif self._value != 1:
            result += "JQK"[self._value-11]
        else:
            result += "A"
        result += self._suit.name
        return result


class Deck:
    _suits: List[Suit] = []
    _cards: List[Card]
    def __init__(self):
        self._cards = []
        self._suits.extend([Suit("♤", 0), 
                            Suit("♥", 1), 
                            Suit("♧", 0), 
                            Suit("♦", 1)])
        for suit in self._suits:
            for i in range(1, 14):
                self._cards.append(Card(i, suit))


deck = Deck()
