# BlackJack game
import random
import time

# card class
class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = rank['value']

  def __str__(self):
    return f"{self.rank['rank']} of {self.suit}"

# deck class
class Deck:
  def __init__(self):
    self.cards = []
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    ranks = [
      {'rank': 'A', 'value': 11},
      {'rank': '2', 'value': 2},
      {'rank': '3', 'value': 3},
      {'rank': '4', 'value': 4},
      {'rank': '5', 'value': 5},
      {'rank': '6', 'value': 6},
      {'rank': '7', 'value': 7},
      {'rank': '8', 'value': 8},
      {'rank': '9', 'value': 9},
      {'rank': '10', 'value': 10},
      {'rank': 'J', 'value': 10},
      {'rank': 'Q', 'value': 10},
      {'rank': 'K', 'value': 10},
    ]
    for suit in suits:
      for rank in ranks:
        self.cards.append(Card(suit, rank))

  def shuffle(self):
    if len(self.cards) > 1:
      random.shuffle(self.cards)

  def deal(self, number):
    dealt_cards = []
    for x in range(number):
      dealt_cards.append(self.cards.pop(0))
    return dealt_cards

# player class
class Player:
  def __init__(self, name, cash):
    self.name = name
    self.cash = cash
    self.bet = 0
    self.players_cards = []

  def add_cards(self, new_cards):
    if type(new_cards) == type([]):
      self.players_cards.extend(new_cards)
    else:
      self.players_cards.append(new_cards)

  def cards_value_sum(self):
    cards_value = 0
    for card in self.players_cards:
      cards_value += card.value
    #print(f'Value of {self.name}\'s cards is {cards_value}')
    return cards_value

  def show_one_card(self):
    print(f'{self.name}\'s one card:')
    print(self.players_cards[-1])

  def show_all_cards(self):
    print(f'{self.name}\'s all cards:')
    for card in self.players_cards:
      print(card)

  def place_bet(self, bet_amt):
    if self.cash >= bet_amt:
      self.cash -= bet_amt
      self.bet += bet_amt
      return f'{self.name}\'s bet is {bet_amt}'
    else:
      print('Not enough cash...')

  def add_cash(self, add_amt):
    self.cash += add_amt

  def sub_cash(self, sub_amt):
    self.cash -= sub_amt

  def hit_or_stand(self):
    self.bust = False
    self.player_stands = False
    while not self.bust:
      if self.cards_value_sum() > 21:
        print('You are Busted!')
        print(f'{dealer_1.name} wins!')
        self.bust = True
      else:
        #hit_or_stand_input = 'Hit'
        hit_or_stand_input = input(f'{self.name}, do you want to Hit or Stand? ')
        if hit_or_stand_input.capitalize() == 'Hit':
          self.add_cards(new_deck.deal(1))
          print(self.players_cards[-1])
        elif hit_or_stand_input.capitalize() == 'Stand':
          self.player_stands = True
          print(f'{self.name} stands...')
          break
    return self.player_stands

  def __str__(self):
    return f'{self.name} has {len(self.players_cards)} cards, and {self.cash} left'

# dealer class
class Dealer:
  def __init__(self):
    self.name = 'Dealer'
    self.dealers_cards = []

  def add_cards(self, new_cards):
    if type(new_cards) == type([]):
      self.dealers_cards.extend(new_cards)
    else:
      self.dealers_cards.append(new_cards)

  def cards_value_sum(self):
    cards_value = 0
    for card in self.dealers_cards:
      cards_value += card.value
    #print(f'Value of {self.name}\'s cards is {cards_value}')
    return cards_value

  def show_one_card(self):
    print(f'{self.name}\'s one card:')
    print(self.dealers_cards[-1])

  def show_all_cards(self):
    print(f'{self.name}\'s all cards:')
    for card in self.dealers_cards:
      print(card)

  def hit(self):
    dealer_bust = False
    while not dealer_bust:
      if self.cards_value_sum() < 17:
        print(f'{self.cards_value_sum()} djokara')
        print(f'{self.name} hits!')
        self.add_cards(new_deck.deal(1))
        print(self.dealers_cards[-1])
      else:
        dealer_bust = True
    else:
      print(f'{self.name} is done, and value of his cards is {self.cards_value_sum()}')

  def __str__(self):
    return f'{self.name} has {len(self.dealers_cards)} cards.'

class Referee:
  def __init__(self, player, dealer):
    self.name = 'Velibor'
    self.player = player
    self.dealer = dealer
    self.go_for_winner_check = True

  def player_busts(self, player, dealer):
    if player.cards_value_sum() > 21:
      print(f'{player.name} is busted!')
      print(f'{dealer.name} is winner!')
      self.go_for_winner_check = False
      game_on = False
      return game_on, self.go_for_winner_check

  def player_wins(self, player):
    if player.cards_value_sum() == 21:
      print(f'{player.name} is winner!')

      player.add_cash(player_1_bet*2)

      self.go_for_winner_check = False
      game_on = False
      return game_on, self.go_for_winner_check

  def dealer_busts(self, dealer, player):
    if dealer.cards_value_sum() > 21:
      print(f'{dealer.name} is busted!')
      print(f'{player.name} is winner!')

      player.add_cash(player_1_bet*2)

      self.go_for_winner_check = False
      game_on = False
      return game_on, self.go_for_winner_check
      
  def dealer_wins(self, dealer):
    if dealer.cards_value_sum() == 21:
      print(f'{dealer.name} is winner!')
      self.go_for_winner_check = False
      game_on = False
      return game_on, self.go_for_winner_check
      
  def winner(self, player, dealer):
    if player.cards_value_sum() > dealer.cards_value_sum():
      print(f'{player.name} is winnerrrr!')

      player.add_cash(player_1_bet*2)

      game_on = False
      return game_on

    elif player.cards_value_sum() < dealer.cards_value_sum():
      print(f'{dealer.name} is winnerrrr!')
      game_on = False
      return game_on

    else:
      player.add_cash(player_1_bet)
      print('It\'s a tie!')
      game_on = False
      return game_on




###############################
player_1_name = 'David'
#player_1_name = input('Please, enter your name: ')
player_1_cash = 1000
#player_1_cash = int(input('How much money you\'ve bringed with you: '))

dealer_1 = Dealer()
player_1 = Player(player_1_name, player_1_cash)
referee_1 = Referee(player_1, dealer_1)

player_1_bet = 100
#player_1_bet = int(input(f'{player_1.name} please, place your bet: '))
player_1.place_bet(player_1_bet)

new_deck = Deck()
new_deck.shuffle()
dealer_1.add_cards(new_deck.deal(2))
player_1.add_cards(new_deck.deal(2))
print(player_1_bet)
#dealer_1.show_one_card()
dealer_1.show_all_cards()
player_1.show_all_cards()

time.sleep(0.5)

referee_1.dealer_wins(dealer_1)
referee_1.player_wins(player_1)
referee_1.dealer_busts(dealer_1, player_1)
referee_1.player_busts(player_1, dealer_1)

player_1.hit_or_stand()

referee_1.player_wins(player_1)
referee_1.player_busts(player_1, dealer_1)

if player_1.player_stands:
  dealer_1.hit()

referee_1.dealer_wins(dealer_1)
referee_1.dealer_busts(dealer_1, player_1)

if referee_1.go_for_winner_check:
  referee_1.winner(player_1, dealer_1)

print(player_1.cash)