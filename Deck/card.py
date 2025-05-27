suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
rank_values = list(range(2, 15))
value_names = {2: "Two", 3: "Three", 4: "Four", 5: "Five",
               6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
face_values = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}


class Card:
    """
    This defines a card
    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit.capitalize()

    @property
    def name(self):
        if self.value in value_names:
            str_name = value_names[self.value]
        if self.value in face_values:
            str_name = face_values[self.value]
        return f"{str_name} of {self.suit}"

    def __repr__(self):
        return f"Card({self.value}, {self.suit})"

    def __str__(self):
        return f"This card is the {self.name}"
