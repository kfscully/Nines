# Rulebook

## Definitions
- **trick**
  - a sequence of play where each player contributes exactly one card
- **round**
  - a sequence of tricks where all players play all the cards in their hand
- **trick-taking**
  - the achievement of winning a trick by playing the highest ranking card relative to the cards played by your opponents
- **betting**
  - attempt to predict the number of tricks you'll win in a round (e.g. if everyone is dealt 3 cards then there are 3 tricks to be won)
- **head**
  - a title of the player who kicks off betting in a given round
  - the head changes at the beginning of each new round, rotating one player clockwise
- **tail**
  - a title of the player who makes the final bet in a given round, always one player to right of the head
- **engine**
  - a title of the player who plays the first card of a trick
  - on the first trick of any round, the head and engine titles are held by the same person
- **caboose**
  - a title of the player who plays the last card of a trick
  - the caboose is always one player to the right of the engine
  - on the first trick of any round, the tail and caboose titles are held by the same person
- **trump suit**
  - the suit of the card flipped from the deck at the beginning of the round
  - this suit outranks the other three suits
  - e.g. if spades <span style="background-color: #FFFFFF"><font color="black">♠️</font></span> is the trump suit, then the 2 of spades <span style="background-color: #FFFFFF"><font color="black">♠️</font></span> outranks all cards of the other suits (diamonds <span style="background-color: #FFFFFF"><font color="red">♦️</font></span>, hearts <span style="background-color: #FFFFFF"><font color="red">♥️</font></span>, and clubs <span style="background-color: #FFFFFF"><font color="black">♣️</font></span>) 
- **lead suit**
  - the suit of the first card played in a trick
  - if it matches the trump suit, then the trump and lead suits are the same
  - if it does NOT match the trump suit, the trump suit outranks the lead suit still but the lead suit then outranks the remaining two suits
  - e.g. if the trump suit is spades <span style="background-color: #FFFFFF"><font color="black">♠️</font></span> and the lead suit is hearts <span style="background-color: #FFFFFF"><font color="red">♥️</font></span>, then the 2 of spades <span style="background-color: #FFFFFF"><font color="black">♠️</font></span> outranks all cards of the other three other suits and the 2 of hearts <span style="background-color: #FFFFFF"><font color="red">♥️</font></span> outranks all cards of the remaining two suits, diamonds <span style="background-color: #FFFFFF"><font color="red">♦️</font></span> and clubs <span style="background-color: #FFFFFF"><font color="black">♣️</font></span>
- **plain suit**
  - any suit that is not the trump suit or the lead suit
- **card rank**
  - the first factor of ranking a set of cards is the suit, the second factor is the face value
  - any card of the trump suit beats all lead and plain suit cards
  - any lead suit card beats all plain suit cards
  - within a given suit:
    - the lowest valued card is a 2 and Aces are high
    - the order of card value is 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
- **following suit**
  - the first player to lay down a card sets the lead suit of that trick
  - all players MUST play a card of that same suit if they have one in their hand
  - if the player does not have the lead suit in their hand, they are free to play any card
  - e.g. let's say your hand looks like this (<span style="background-color: #FFFFFF"><font color="red">♦️</font></span> <span style="background-color: #FFFFFF"><font color="black">♣️</font></span></font></span> <span style="background-color: #FFFFFF"><font color="black">♣️</font></span> <span style="background-color: #FFFFFF"><font color="red">♥️</font></span> <span style="background-color: #FFFFFF"><font color="red">♥️</font></span> <span style="background-color: #FFFFFF"><font color="red">♥️</font></span>)
    - if the lead suit is a diamond <span style="background-color: #FFFFFF"><font color="red">♦️</font></span> then you must play your diamond <span style="background-color: #FFFFFF"><font color="red">♦️</font></span>
    - if the lead suit is a spade <span style="background-color: #FFFFFF"><font color="black">♠️</font></span> then you are free to play any card in your hand because you do not have any spades <span style="background-color: #FFFFFF"><font color="black">♠️</font></span>


## What You Need
- a regular 52 card deck, no jokers

## How To Win
- obtain the highest score after all rounds are played

## How A Trick Works
- the engine plays whatever card they wish from their hand, which sets the lead suit for the rest of the trick
- the next turn is taken by the player to the left of engine. they must follow suit and play a card of the lead suit, if they have one available in their hand. if not, they may play any card in their hand
- this continues in a clockwise pattern until all players have played exactly one card
- whoever played the highest ranking card wins the trick

## How A Round Works
- the deck is shuffled and the number of cards dealt is in accordance with the round details (found at the bottom of this section)
- the first card left over in the deck is flipped and the suit of that card becomes the trump suit
- the head makes the first bet on how many tricks they think they will win
- in a clockwise sequence, all other players make their bets for how many tricks they think they will win
- all players, except the tail, must make a bet between zero and the number of tricks available
- the sum total of all bets CANNOT equal the number of tricks available
  - this prevents a scenario where all players bet correctly; there must be at least one loser per round!
- the tail is limited in their bet by the existing sum of bets because the tail's bet must not bring the sum total equal to the number of tricks available
  - e.g. let's say there are three players (X, Y, Z) with a six-card hand
  - player X bets two, player Y bets three, and player Z wants to bet one.
  - however, because that would bring the sum total of bets to six, player Z (the tail) cannot bet one. they must bet either zero, two, three, four, five, or six
- if the sum total of bets exceeds the number of cards in hand before the tail bets then the tail is not limited
- now that all bets are logged, round play begins with the first trick
- the head starts off the first trick as the engine
- the winner of any given trick becomes the engine for the subsequent trick
- play continues until all cards in the hand have been played
- scores are tallied (see next section) and the titles of head/tail are shifted one player to the left
- round details of cards dealt per person are as follows:
  - Round 1 = 1 card, Round 2 = 2 cards, [...] , Round 9 = 9 cards, Round 10 = 9 cards, Round 11 = 9 cards, Round 12 = 8 cards, Round 13 = 7 cards, [...] , Round 18 = 2 cards, Round 19 = 1 card

## How Points Are Scored
- after the round is complete, a player only scores points if their bet of how many tricks they'd win during the round is correct
- if a player's bet is correct, they score the number of their bet times five and then add ten
  - e.g. if a player bets they'll win zero tricks and that bet is correct, they score zero times five (0) then add ten for a total of 10
  - e.g. if a player bets they'll win three tricks and that bet is correct, they score three times five (15) then add ten for a total of 25
