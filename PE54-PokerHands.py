"""
PROJECT EULER PROBLEM 54 - Poker Hands
In the card game poker, a hand consists of five cards and are ranked, 
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up
of the highest value wins; for example, a pair of eights beats a
pair of fives (see example 1 below). But if two ranks tie, for example,
both players have a pair of queens, then highest cards in each hand
are compared (see example 4 below); if the highest cards tie then the
next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt
to two players. Each line of the file contains ten cards (separated
by a single space): the first five are Player 1's cards and the last
five are Player 2's cards. You can assume that all hands are valid
(no invalid characters or repeated cards), each player's hand is in no
specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

def readHands():
    hand_list = []
    with open("p054_poker.txt") as file:
        for line in file:
            cards = line.rstrip("\n")
            cards = cards.split(" ")
            hands = [[cards[c] for c in range(0,5)],[cards[c] for c in range(5,10)]]
            hand_list.append(hands)
    return(hand_list)


VALUE = 0
SUIT = 1
hand_rank = ("high card","pair","two pair","trips","straight","flush","full house","quads","straight flush")

hand_list = readHands()
hand_size = 5

p1wins = 0
for aHands in hand_list:
    hands = []

    # ANALYSE HANDS
    for aHand in aHands:
        hand = []
        # Convert hand to a list of cards, with a card = [VALUE,SUIT]
        for aCard in aHand:
            card = []
            card.append("23456789TJQKA".find(aCard[VALUE])+2)
            card.append(aCard[SUIT])
            hand.append(card)
            hand.sort()
        hand_type = {"hand":hand, "high card":False, "junk":[], "pair":False, "two pair":[], "trips":False, "full house":[], "quads":False}
        straight = True
        flush = True
        for iCard in range(hand_size):
            # Take care of straights
            last_card = (iCard == hand_size-1)
            if straight and not last_card:
                straight = (hand[iCard+1][VALUE] == hand[iCard][VALUE] + 1) and straight
            else:
                pass

            # Take care of flushes
            if flush and not last_card:
                flush = (hand[iCard+1][SUIT] == hand[iCard][SUIT]) and flush
            else:
                pass
                
            # Take care of pairs/trips/quads/full house (skips if straight or flush check has passed)
            # If the two adjacent cards are not a form of pair, put the card in the junk pile,
            # even if the card is part of a straight or a flush
            if not last_card:
                if not straight and not flush and (hand[iCard][VALUE] == hand[iCard+1][VALUE]):
                    if hand_type["pair"] == hand[iCard][VALUE]:
                        hand_type["trips"] = hand_type["pair"]
                        hand_type["pair"] = False
                    elif hand_type["pair"] != hand[iCard][VALUE] and hand_type["pair"] != False:
                        hand_type["two pair"] = sorted([hand[iCard][VALUE],hand_type["pair"]])
                        hand_type["pair"] = False
                    elif hand_type["trips"] == hand[iCard][VALUE]:
                        hand_type["quads"] = hand_type["trips"]
                        hand_type["trips"] = False
                    elif hand_type["trips"] != hand[iCard][VALUE] and hand_type["trips"] != False:
                        hand_type["full house"] = [hand[iCard][VALUE],hand_type["trips"]]
                        hand_type["trips"] = False
                    else:
                        hand_type["pair"] = hand[iCard][VALUE]
            if hand[iCard][VALUE] != hand_type["pair"] and hand[iCard][VALUE] != hand_type["trips"] and hand[iCard][VALUE] != hand_type["quads"] and hand[iCard][VALUE] not in hand_type["two pair"] and hand[iCard][VALUE] not in hand_type["full house"]:
                hand_type["junk"].append(hand[iCard])
        hand_type["junk"].sort()
        hand_type["junk"].reverse()

        hand_type["straight flush"] = (straight and flush)
        hand_type["straight"] = straight
        hand_type["flush"] = flush
        hands.append(hand_type)

    # RANK HANDS
    player_hand_rank = [0,0]
    winner = 0
    for player in range(2):
        for i,rank in enumerate(hand_rank):
            if rank == "high card":
                continue
            if hands[player][rank]:
                player_hand_rank[player] = i

    # COMPARE HANDS
    if player_hand_rank[0] > player_hand_rank[1]:
        winner = 1
    elif player_hand_rank[0] < player_hand_rank[1]:
        winner = 2
    else:
        if (hands[0][hand_rank[player_hand_rank[0]]] is list) and (player_hand_rank[0] > 0):
            for v in range(1,-1,-1):
                if hands[0][hand_rank[player_hand_rank[0]]][v] > hands[1][hand_rank[player_hand_rank[1]]][v]:
                    winner = 1
                    break
                elif hands[0][hand_rank[player_hand_rank[0]]][v] < hands[1][hand_rank[player_hand_rank[1]]][v]:
                    winner = 2
                    break
                else: #hands[0][hand_rank[player_hand_rank[0]]][v] == hands[1][hand_rank[player_hand_rank[1]]][v]
                    pass
        elif hands[0][hand_rank[player_hand_rank[0]]] is int:
            if hands[0][hand_rank[player_hand_rank[0]]] > hands[1][hand_rank[player_hand_rank[1]]]:
                winner = 1
            elif hands[0][hand_rank[player_hand_rank[0]]] < hands[1][hand_rank[player_hand_rank[1]]]:
                winner = 2
            else:
                pass
    if winner == 0:
        # Compare junk
        for c in range(len(hands[0]["junk"])-1):
            if hands[0]["junk"][c][VALUE] > hands[1]["junk"][c][VALUE]:
                winner = 1
                break
            elif hands[0]["junk"][c][VALUE] < hands[1]["junk"][c][VALUE]:
                winner = 2
                break
            else: #hands[0]["junk"][c][VALUE] == hands[1]["junk"][c][VALUE]
                pass
        
    # DECLARE WINNER
    if winner == 1:
        print(f"Player1's {hand_rank[player_hand_rank[0]]} beats Player2's {hand_rank[player_hand_rank[1]]}!")
        p1wins += 1
    elif winner == 2:
        print(f"Player2's {hand_rank[player_hand_rank[1]]} beats Player1's {hand_rank[player_hand_rank[0]]}!")
    else:
        print("I was told this wouldn't happen.")
print(f"Player1 wins {p1wins} times out of 1000.")
