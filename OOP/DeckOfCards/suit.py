from enum import Enum

class Suit(Enum):
    SPADE = 0
    CLUB = 1
    HEART = 2
    DIAMOND = 3


class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9 
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Deck:
    def __init__(self):
        self.cards = []

    def insert_card(self, card):
        for element in self.cards:
            if element.suit.name == card.suit.name and element.rank.name == card.rank.name:
                return False
        self.cards.append(card)
        return True
 

    def remove_card(self, suit, rank):
        for card in self.cards:
            if card.rank.name == rank.name and card.suit.name == suit.name:
                self.cards.remove(card)
                return True
        return False
        

    def show_cards(self):
        for card in self.cards:
            print("Suit is {} and Rank is {}".format(card.suit.name, card.rank.name))


    def sort_through_rank(self, low, high):
        if high > low:
            mid = low + int((high - low) / 2)
            self.sort_through_rank(low, mid)
            self.sort_through_rank(mid + 1, high)
            self.merge(low, mid, high)

    def merge(self, low, mid, high):
        left_array = self.cards[low: mid + 1]

        right_array = self.cards[mid + 1: high + 1]

        left_index = 0
        right_index = 0
        array_index = low
        
        while right_index < len(right_array) and left_index < len(left_array):
            if left_array[left_index].rank.value <= right_array[right_index].rank.value:
                self.cards[array_index] = left_array[left_index]
                left_index += 1
            else:
                self.cards[array_index] = right_array[right_index]
                right_index += 1
            array_index += 1

        while left_index < len(left_array):
            self.cards[array_index] = left_array[left_index]
            array_index += 1
            left_index += 1

        while right_index < len(right_array):
            self.cards[array_index] = right_array[right_index]
            array_index += 1
            right_index += 1

    
    def quick_sort(self, low, high):
        if low > high:
            return
        partition_index = self.partition(low, high)
        self.quick_sort(low, partition_index - 1)
        self.quick_sort(partition_index + 1, high)


    def partition(self, low, high):
        pivot = self.cards[high].suit.value
        p_index = low       

        for element in range(low, high):
            if self.cards[element].suit.value < pivot:
                self.cards[element], self.cards[p_index] = self.cards[p_index], self.cards[element]
                p_index += 1
        self.cards[p_index], self.cards[high] = self.cards[high], self.cards[p_index]
        return p_index

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def retrieve_suit(self):
        return self.suit.name

    def retrieve_rank(self):
        return self.rank.name

    
if __name__ == '__main__':
    deck = Deck()

    card = Card(Suit.SPADE, Rank.EIGHT)
    deck.insert_card(card)

    card = Card(Suit.CLUB, Rank.TEN)
    deck.insert_card(card)

    card = Card(Suit.CLUB, Rank.SIX)
    deck.insert_card(card)

    card = Card(Suit.HEART, Rank.EIGHT)
    deck.insert_card(card)

    card = Card(Suit.SPADE, Rank.ACE)
    deck.insert_card(card)

    deck.show_cards()

    print("----------------------------------")

    #deck.sort_through_rank(0, len(deck.cards) - 1)
    deck.quick_sort(0, len(deck.cards) - 1)
    deck.show_cards()
