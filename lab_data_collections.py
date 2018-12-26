from random import randrange
from lab_classes import PlayingCard
from math import sqrt

suit_size = 13  # Number of cards in a suit.
deck_size = 52  # Number of cards in a deck.
num_cards = 260  # Number of cards to create with random rank & suit values

from lab_classes import PlayingCard

def make_random_cards():
    """Generate num_cards number of random PlayingCard objects.

    This function will generate num_cards RANDOM playing cards
    using your PlayingCard class. That means you will have to choose a random
    suit and rank for a card num_cards times.

    Printing:
        Nothing

    Positional arguments:
        None

    Returns:
        cards_list -- a list of PlayingCard objects.
    """

    cards_list = []
    suits = ["s", "h", "c", "d"]
    
    for i in range(num_cards):
        rank = randrange(0,12)
        suit = suits[randrange(0,4)]
        
        newCard = PlayingCard(rank, suit)
        cards_list.append(newCard)
        
    return cards_list


def freq_count(cards_list):
    """Count every suit-rank combination.

    Returns a dictionary whose keys are the card suit-rank and value is the
    count.

    Printing:
        Nothing

    Positional arguments:
        cards_list -- A list of PlayingCard objects.

    Returns:
        card_freqs -- A dictionary whose keys are the single letter in the set
        'd', 'c', 'h', 's' representing each card suit.  The value for each key
        is a list containing the number of cards at each rank, using the index
        position to represent the rank. For example, {'s': [0, 3, 4, 2, 5]}
        says that the key 's', for 'spades' has three rank 1's (aces), four
        rank 2's (twos), two rank 3's (threes) and 5 rank 4's (fours).  Index
        position 0 is 0 since no cards have a rank 0, so make note.
    """
    # DO NOT REMOVE BELOW
    if type(cards_list) != list or \
            list(filter(lambda x: type(x) != PlayingCard, cards_list)):
        raise TypeError("cards_list is required to be a list of PlayingCard \
                        objects.")
    # DO NOT REMOVE ABOVE

    sArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    dArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in cards_list:
        if i.get_suit() == 's':
            sArray[i.get_rank()]+=1
        elif i.get_suit() == 'h':
            hArray[i.get_rank()]+=1
        elif i.get_suit() == 'c':
            cArray[i.get_rank()]+=1
        elif i.get_suit() == 'd':
            dArray[i.get_rank()]+=1    
            
    card_freqs = {'s': sArray, 'h': hArray, 'c': cArray, 'd': dArray}
    
    return card_freqs


def std_dev(counts):
    """Calculate the standard deviation of a list of numbers.

    Positional arguments:
        counts -- A list of ints representing frequency counts.

    Printing:
        Nothing

    Returns:
        _stdev -- The standard deviation as a single float value.
    """
    # DO NOT REMOVE BELOW
    if type(counts) != list or \
            list(filter(lambda x: type(x) != int, counts)):
        raise TypeError("counts is required to be a list of int values.")
    # DO NOT REMOVE ABOVE

    sigma = 0
    n = len(counts)
    mean = sum(counts)/n
    
    for i in counts:
        sigma += (i-mean)**2

    _stdev = sqrt(sigma/(n-1))
    
    return _stdev


def print_stats(card_freqs):
    """Print the final stats of the PlayingCard objects.

    Positional arguments:
        card_freqs -- A dictionary whose keys are the single letter in the set
        'dchs' representing each card suit. The value for each key is a list of
        numbers where each index position is a card rank, and its value is its
        card frequency.

        You will probably want to call th std_dev function in somewhere in
        here.

    Printing:
        Prints the statistic for each suit to the screen, see assignment page
        for an example output.

    Returns:
        None
    """
    # DO NOT REMOVE BELOW
    if type(card_freqs) != dict or \
            list(filter(lambda x: type(card_freqs[x]) != list, card_freqs)):
        raise TypeError("card_freqs is required to be a list of int values.")
    # DO NOT REMOVE ABOVE

    print('Standard deviation for the frequency counts of each rank in suit: ')
    print('Hearts: ', std_dev(card_freqs['h']), 'cards')
    print('Spades: ', std_dev(card_freqs['s']), 'cards')
    print('Clubs: ', std_dev(card_freqs['c']), 'cards')
    print('Diamonds: ', std_dev(card_freqs['d']), 'cards')

def main():
    cards = make_random_cards()
    suit_counts = freq_count(cards)
    print_stats(suit_counts)


if __name__ == "__main__":
    main()
