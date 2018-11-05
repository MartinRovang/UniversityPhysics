import numpy as np 


# Implementation of card game with errors and left out features

class Deck:
    def __init__(self):
        cardrep = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        card_suit = ['C','D','H','S']
        #H6 osv...
        self.deck_given = [suit+str(rank) for suit  in card_suit for rank in cardrep]
        shuffle(self.deck_given)

    def hand(self,n):
        temp = self.deck_given[:n]
        del self.deck_given[:n]
        return temp
    

    def deal(self, n, p):
        temp = []
        for i in range(p):
            temp.append(self.deck_given[:n])
            del self.deck_given[:n]
        return temp


    def __str__(self):
        return '{}'.format(self.deck_given)


def begin_game(p):
    
    #Initiate players
    players = game_deck.deal(5,p)
    print(players)
    flipped_deck = str(eval(str(game_deck))[0])
    game_deck.hand(1)
    while True:
        for i in range(len(players)):
            print('Facing card: %s'%flipped_deck)
            print('--------------------')
            flipped_deck_color = flipped_deck[0]
            flipped_deck_value = flipped_deck[1]
            print('Player %s turn'%i)
            print('Cards: %s'%players[i])

            legal = False
            for z in players[i]:
                if z[0] == flipped_deck[0] or z[1] == flipped_deck[1] or z[1] == 8:
                    legal = True

            drawn = 0
            if legal == False:
                while legal == False:
                    print('--------------------')
                    draw = input('You must draw cards (max 3 each round, input = no or 1-3\n')
                    if draw != 'no':
                        if int(draw) < 4:
                            for k in range(int(draw)):
                                players[i].append(game_deck.hand(int(draw))[0])
                            print('Cards: %s'%players[i])
                            print('--------------------')
                        else:
                            print('Invalid nr')
                    legal = False
                    for z in players[i]:
                        if z[0] == flipped_deck[0] or z[1] == flipped_deck[1] or z[1] == 8:
                            legal = True
                            drawn = 1

            if drawn == 0:
                print('--------------------')
                draw = input('Want to draw a card? (max 3 each round, input = no or 1-3\n')
                if draw != 'no':
                    if int(draw) < 4:
                        for k in range(int(draw)):
                            players[i].append(game_deck.hand(int(draw))[0])
                        print('Cards: %s'%players[i])
                        print('--------------------')
                    else:
                        print('Invalid nr')
            drawn = 0
            card_chosen = int(input('Enter index from 0 to n-1 to choose card: '))
            print('--------------------')
            players_card = players[i][card_chosen]
            players_card_color = players[ii][card_chosen][0]
            players_card_value = players[i][card_chosen][1]
            if players_card_color == flipped_deck[0] or players_card_value == flipped_deck_value or players_card_value == 8:
                flipped_deck = players_card
                del players[i][card_chosen]
            else:
                print('Cant place this card')
                print('--------------------')

            if len(players[i]) == 0:
                print('PLAYER %s WON!!!'%str(i))
                break
            
            

begin_game(2)
