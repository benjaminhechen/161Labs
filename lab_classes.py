import random

class PlayingCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def get_rank(self):
        return self.rank
    def get_suit(self):
        return self.suit
    def bj_value(self):
        if(self.rank >= 10):
            return 10
        else:
            return self.rank
    def __repr__(self):
        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
                  "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        x = ranks[self.rank-1]
        
        if self.suit == 's':
            y = "Spades"
        elif self.suit == 'h':
            y = "Hearts"
        elif self.suit == 'c':
            y = "Clubs"
        elif self.suit == 'd':
            y = "Diamonds"
        
        output = x + " of " + y  
        
        return output

def main():
#    print("Testing card class")
#    num = eval(input("How many cards would you like to see? "))
#       
    suits = ["s", "h", "c", "d"]
#    
#    for i in range(num):
#        rank = random.randint(0,12)
#        suit = random.choice(suits)
#        
#        newCard = PlayingCard(rank, suit)
#        
#        print(str(newCard) + " counts " + str(newCard.bj_value()))
        

main()
