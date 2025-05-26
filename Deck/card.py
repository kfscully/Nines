suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
rank_values = list(range(2,15))
value_names = {2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
face_values = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

class Card:
    """
    This defines a card
    """
    def __init__(self, value, suit, name):
        self.value = value
        self.suit = suit
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value in value_names:
            name = f"{value_names[self.value]} of {suits[self.suit]}"
        if value in face_values:
            name = f"{face_values[self.value]} of {suits[self.suit]}"

    def __repr__(self):
        return(f"Card({self.suit}, {self.value})")

    def __str__(self):
        return(f"This card is the {self._name}")
