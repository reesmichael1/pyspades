class CardsInTrick:

    def __init__(self):
        self.first_card = None
        self.played_cards = []

    def play_card(self, card):
        if not self.first_card:
            self.first_card = card
        self.played_cards.append(card)

    def opponents_cards(self):
        if len(self.played_cards) == 3:
            return (self.played_cards[0], self.played_cards[2])
        elif len(self.played_cards) == 2:
            return (self.played_cards[1])
        elif len(self.played_cards) == 1:
            return (self.played_cards[0])
        elif len(self.played_cards) == 0:
            return ()
        else:
            raise RuntimeError('Extra cards previously played')

    def partners_card(self):
        if len(self.played_cards) == 3:
            return self.played_cards[1]
        elif len(self.played_cards) == 2:
            return self.played_cards[0]
        elif len(self.played_cards) in (0, 1):
            return ()
        else:
            raise RuntimeError('Extra cards previously played')
        pass

    def currently_winning_card(self):
        if not self.played_cards:
            return None
        elif len(self.played_cards) == 1:
            return self.first_card
        elif len(self.played_cards) < 4:
            spades = sorted([card for card in self.played_cards
                             if card.suit == 'Spades'])
            if spades:
                return max(spades)

            return max([card for card in self.played_cards
                        if card.suit == self.first_card.suit])
        else:
            raise RuntimeError('Extra cards previously played')
