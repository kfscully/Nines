import card
from card import Card
# from collections import defaultdict
from random import shuffle


class Deck:
    """
    This defines a deck
    Behaviors of a deck: shuffle, deal, flip top card,
        rank cards, collect cards from players
    deal one card should be a function
    dealing multiple cards should be a separate
        function that uses single-card deal
    shuffling should reset the trump, lead, and plain suits all to False
    you should have a shuffle cards vs
        shuffle all cards in case you want to use this code in the future
    dealing a card should move it out of the deck and into a hand
    flipping the top card should remove it from the deck.
        should it also be a property? probs not. it SHOULD also
    set the suit trump and plain properties though
    properties: trump suit, lead suit, plain suit
    lead suit will be set by player class
    """
    def __init__(self):
        cards = []
        for i in card.rank_values:
            for suit in card.suits:
                cards.append(Card(i, suit))
        self.cards = cards
        self.discarded_cards = []

    @property
    def lead_suit(self):
        return False

    @property
    def plain_suits(self):
        return False

    @property
    def trump_suit(self):
        return False

    def deal_single(self):
        # deal_single is different from flip_top_card because eventually
        # you'll need to specify a recipient of the dealt card
        try:
            dealt_card = self.cards.pop(0)
        except IndexError:
            print("Your deck doesn't have any cards left!")
        else:
            self.discarded_cards.append(dealt_card)
            return dealt_card.name

    def deal_many(self, num_players, num_cards):
        # you'll need to specify a recipient players of the dealt cards # kfs
        assert num_players * num_cards <= 52, "You don't have enough cards!"
        cards_dealt = {f"player_{i+1}": [] for i in range(num_players)}
        for nc in range(num_cards):
            for np in range(num_players):
                player_key = f"player_{np+1}"
                cards_dealt[player_key].append(Deck.deal_single(self))
        return cards_dealt

    def flip_top_card(self):
        try:
            dealt_card = self.cards.pop(0)
        except IndexError:
            print("Your deck doesn't have any cards left!")
        else:
            self.discarded_cards.append(dealt_card)
            return dealt_card

    def len(self):
        return len(self.cards)

    def shuffle_remaining(self):
        shuffle(self.cards)

    def shuffle_all(self):
        self.cards += self.discarded_cards
        shuffle(self.cards)

    def __iter__(self):
        return self

    def __repr__(self):
        return f"{self.cards}"

    def __str__(self):
        total_deck = []
        for item in self.cards:
            total_deck.append(item.name)
        return f"{total_deck}"
