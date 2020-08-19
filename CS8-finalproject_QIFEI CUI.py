# I understand the instructions and academic honesty policy for this project:
# Qifei
# Define all your functions here
class Card :
    '''Define card with 3 element: rank suit order'''
    RANKS = [str(n) for n in range(1, 13)]
    SUITS = 'Clubs Golds Cups Swords '.split()

    def __init__(self, rank, suit, order) :
        self.rank = rank  # rank 1~13
        self.suit = suit  # suits
        self.order = order  # give each card an index

    def __str__(self) :  # override print() to print content on cards
        cardFace = self.suit + ' ' + self.rank
        return cardFace

    def __lt__(self, other) :  # override < for ranking since object cannot be directly compared
        su1 = 0
        su2 = 0
        if self.suit == 'Clubs' :  # define weight of each rank from 1 to 4 Clubs is the smallest
            su1 = 1
        elif self.suit == 'Golds' :
            su1 = 2
        elif self.suit == 'Cups' :
            su1 = 3
        elif self.suit == 'Swords' :  # Swords is the largest
            su1 = 4

        if other.suit == 'Clubs' :  # same for the compared card
            su2 = 1
        elif other.suit == 'Golds' :
            su2 = 2
        elif other.suit == 'Cups' :
            su2 = 3
        elif other.suit == 'Swords' :
            su2 = 4

        # if su1 * int(self.rank) < su2 * int(other.rank):
        # this line used for sort by rank on card.
        if (su1 * 12 + int(self.rank)) < (su2 * 12 + int(other.rank)) :
            return True
        return False

    def cardSort(self) :  # define sorted() to sort card from different suits and ranks
        return sorted(self.cards)


class Hand() :
    # this class is defined for save cards in players' hands.

    def __init__(self) :
        self.cards = []  # initiating cards[]

    def __str__(self) :  # override print() function to print a hand of cards
        sortCard = sorted(self.cards)
        if sortCard :
            rep = ''
            for card in sortCard :
                rep += str(card) + '\n'
        else :
            rep = 'player has no card in hand.'
        return rep

    def clear(self) :  # clear players hands
        self.cards = []

    def add(self, card) :  # add card() to player
        self.cards.append(card)

    def give(self, card, other_hand) :  # give a card to another player
        self.cards.remove(card)
        other_hand.add(card)
        # other_hand.append(card)
        # using function in python lib


class Poke(Hand) :
    def populate(self) :  # create deck
        for suit in Card.SUITS :
            for rank in Card.RANKS :
                self.add(Card(rank, suit, order=0))

    def shuffle(self) :  # shuffle cards
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand) :  # pull cards after shuffle the order of cards in deck
        if len(self.cards) >= 9 :  # check if there have enough cards for dealing
            for rounds in range(per_hand) :
                for hand in hands :
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                    # self.give(top_card,hand)
                    # Poke as a subclass of Hand() can use function in class Hand()
        else :
            print('No card left!')

    def show_deck(self) :  # use sorted() function to print card in order without changing its original order
        for i in sorted(self.cards) :
            print(i)


class player() :
    def __init__(self, username, userHand=[]) :  # player has username and userHand to save names and hand()
        self.name = username
        self.Hand = userHand

    def show_hand(self) :
        print(self.name)
        print(self.Hand)


def show_Menu() :  # display menu
    print('''
s: start new game
p: Pull cards for all players
o: output deck
h: output players' hand
e: exchange one card
d: declare winner
q: quit
''')


# Write the program that uses those functions here
if __name__ == "__main__" :
    start_game = False # variable for checking if player has pressed 's' to start game.
    while True :  # start looping
        show_Menu()  # show Menu
        user_choice = input('Select an option: ')  # waiting for input

        if user_choice == 's' :
            player1 = player(username=input('Please input player 1\'s name:\n'))
            player2 = player(username=input('Please input player 2\'s name:\n'))
            player3 = player(username=input('Please input player 3\'s name:\n'))
            start_game = True # indicating that user has started the game
            poke1 = Poke()
            poke1.populate()  # create a deck named poke1
            poke1.shuffle()  # disturbing the order of cards in poke1
            players = [Hand(), Hand(), Hand()] #create three empty Hand object to receive cards

        elif user_choice == 'p' :
            if start_game == False : #check if player has started the game.
                print('Please start the game first!')
            else :
                poke1.shuffle() # disturbing the order of cards for random selecting
                poke1.deal(players, 3)  # give each player 3 cards
                player1.Hand = players[0]
                player2.Hand = players[1]
                player3.Hand = players[2]

        elif user_choice == 'o' :
            if start_game == False :
                print('Please start the game first!')
            else :
                poke1.show_deck() # display remain cards in deck

        elif user_choice == 'h' :
            if start_game == False :
                print('Please start the game first!')
            else :
                player1.show_hand() # display cards in players' hand
                player2.show_hand()
                player3.show_hand()

        elif user_choice == 'd' :
            if start_game == False :
                print('Please start the game first!')
            else :
                sum1 = 0 # scores of player 1,2,3
                sum2 = 0
                sum3 = 0
                for card in player1.Hand.cards :
                    sum1 += int(card.rank) # adding rank of all cards in player's hand
                for card in player2.Hand.cards :
                    sum2 += int(card.rank)
                for card in player3.Hand.cards :
                    sum3 += int(card.rank)
                print("%s has %d points." %(player1.name, sum1))
                print("%s has %d points." %(player2.name, sum2))
                print("%s has %d points." %(player3.name, sum3))
                if sum1 > sum2 and sum1 > sum3 : # determine the winner
                    print("The winner is \"%s\" with %d points!" %(player1.name, sum1))
                elif sum2 > sum1 and sum2 > sum3 :
                    print("The winner is \"%s\" with %d points!" % (player2.name, sum2))
                else :
                    print("The winner is \"%s\" with %d points!" % (player3.name, sum3))

        elif user_choice == 'e' :
            if start_game == False :
                print('Please start the game first!')
            else :
                card1 = ((min(player1.Hand.cards, key=lambda card : int(card.rank)))) # find the minimun card in players' hand and save the data in a new card object
                card2 = ((min(player2.Hand.cards, key=lambda card : int(card.rank))))
                card3 = ((min(player3.Hand.cards, key=lambda card : int(card.rank))))
                player1.Hand.cards.remove((min(player1.Hand.cards, key=lambda card : int(card.rank)))) # delete the origin minimun card
                player2.Hand.cards.remove((min(player2.Hand.cards, key=lambda card : int(card.rank))))
                player3.Hand.cards.remove((min(player3.Hand.cards, key=lambda card : int(card.rank))))
                player1.Hand.cards.append(card3) # add the card players' draw to the following players' hand
                player2.Hand.cards.append(card1)
                player3.Hand.cards.append(card2)

        elif user_choice == 'q' :
            break # break the loop

        else :
            print('This is not a valid input') #for other undefined input

# this part use as test program to check whether there's syntax error in program or there's output mistake while adding new function.
'''     elif user_choice == 't' :
            i = player1.Hand.cards.index(min(player1.Hand.cards))
            print(min(player1.Hand.cards))
            # player1.Hand.give(player1.Hand.cards[i],player2.Hand)
            min_value = None
            for card in player1.Hand.cards :
                if min_value == None or min_value > int(card.rank) :
                    min_value = int(card.rank)
            print(min_value)
            print(card1)
'''
