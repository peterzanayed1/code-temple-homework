import random

class solution():
    a = 11
    q=10
    k=10
    j=10
    deck = [2,3,4,5,6,7,8,9,10,j,q,k,a,2,3,4,5,6,7,8,9,10,j,q,k,a,2,3,4,5,6,7,8,9,10,j,q,k,a,2,3,4,5,6,7,8,9,10,j,q,k,a]
    player_hand = []
    dealer_hand = []

    def __innit__(self,player_hand = [], dealer_hand = []):
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand


    def deal(self):
        random.shuffle(self.deck)
        self.player_hand.append(self.deck.pop(0))
        self.dealer_hand.append(self.deck.pop(0))
        self.player_hand.append(self.deck.pop(0))
        self.dealer_hand.append(self.deck.pop(0))
        print(f"You have {self.player_hand}")
        print(f"dealer has [{self.dealer_hand[0]},X]")
        if sum(self.player_hand) == 21 and sum(self.dealer_hand) != 21:
            return 'You Have BlackJack. You Win'
        elif sum(self.player_hand) != 21 and sum(self.dealer_hand) == 21:
            return 'Dealer has 21 YOU LOSE'
        elif sum(self.player_hand) == 21 and sum(self.dealer_hand) == 21:
            return 'PUSH'
        
        while True:
            hitorstay = input('would you like to hit or stay')
            if hitorstay.lower() == 'hit':
                self.player_hand.append(self.deck.pop(0))
                if sum(self.player_hand) > 21:
                    print(f'you Busted with {self.player_hand} {sum(self.player_hand)}')
                    break
                else:
                    print(f'you have:{sum(self.player_hand)} {(self.player_hand)}')
            elif hitorstay.lower() == 'stay':
                print(sum(self.player_hand))
                break

        
        while True:
            if sum(self.dealer_hand) <= 16:
                self.dealer_hand.append(self.deck.pop(0))
            else:
                break
            print(f"{self.dealer_hand} {sum(self.dealer_hand)}")


        if sum(self.player_hand) > 21:
            print('BUST! You lose this hand')
            
        elif sum(self.dealer_hand) > 21:
            print('DEALER BUST! you win this hand')
           
        elif sum(self.player_hand) <= 21 and sum(self.player_hand) > sum(self.dealer_hand):
            print(f"you have {sum(self.player_hand)} and dealer has {sum(self.dealer_hand)} You Win!")
           
        elif sum(self.player_hand) == sum(self.dealer_hand) and sum(self.player_hand) <= 21:
            print(f"you have {sum(self.player_hand)} and dealer has {sum(self.dealer_hand)} You push!")
            
        elif sum(self.dealer_hand) <= 21 and sum(self.player_hand) < sum(self.dealer_hand):
            print(f"you have {sum(self.player_hand)} and dealer has {sum(self.dealer_hand)} You Lose!")
            



            





play = solution()

(play.deal())