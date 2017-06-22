import pydealer
from strategies import Strategy
from pydealer.const import DEFAULT_RANKS as ranks


def _likely_to_win(eligible_cards, cards_in_trick, spades_broken):
    cards_to_return = sorted([card for card in eligible_cards
                              if card.suit == 'Spades'])
    if not cards_to_return:
        cards_to_return = sorted(eligible_cards)
    else:
        if not spades_broken:
            return cards_to_return[0]
    return cards_to_return[len(cards_to_return) - 1]


def _most_likely_to_lose(eligible_cards, cards_in_trick):
    sorted_cards = sorted(eligible_cards)
    if (cards_in_trick.first_card and
            sorted_cards[0].suit == cards_in_trick.first_card.suit):
        # Return highest card we can safely play
        good_cards = [card for card in sorted_cards
                      if card < cards_in_trick.currently_winning_card()]
        if good_cards:
            return good_cards[len(good_cards) - 1]
        return sorted_cards[0]
    elif not cards_in_trick.first_card:
        return sorted_cards[0]
    else:
        # Return highest non-Spade we have
        # Better would be to return highest card with minimum low cards
        cards_to_return = [card for card in eligible_cards
                           if card.suit != 'Spades']
        if not cards_to_return:
            return sorted_cards[0]
        return cards_to_return[len(cards_to_return) - 1]


def _most_likely_to_force_opponent_out(eligible_cards, cards_in_trick):
    currently_winning_card = cards_in_trick.currently_winning_card()
    if currently_winning_card:
        if eligible_cards[0].suit != currently_winning_card.suit:
            return _most_likely_to_lose(eligible_cards, cards_in_trick)
        sorted_cards = sorted(eligible_cards)
        last_card = sorted_cards[0]
        for card in sorted_cards:
            if card < currently_winning_card:
                last_card = card
            else:
                if (ranks['values'][card.value] -
                        ranks['values'][currently_winning_card.value] == 1):
                    last_card = card

        return last_card
    else:
        return sorted(eligible_cards)[0]


def _help_partner_going_nil(eligible_cards, cards_in_trick):
    # If partner has already played,
    partners_card = cards_in_trick.partners_card()
    if partners_card:
        if partners_card == cards_in_trick.currently_winning_card():
            # Need to play higher card
            return _likely_to_win(eligible_cards, cards_in_trick)
        else:
            # Play lowest card we can
            return sorted(eligible_cards)[0]
    else:
        return sorted(eligible_cards)[len(eligible_cards) - 1]


class CardChooser:
    def __init__(self):
        self.spades_broken = False
        self.strategy = Strategy.WIN_TRICKS

    def choose_card(self, hand, cards_in_trick):
        first_card = cards_in_trick.first_card
        if first_card:
            eligible_cards = [card for card in hand
                              if card.suit == first_card.suit]
            if not eligible_cards:
                eligible_cards = hand
        else:
            if self.spades_broken:
                eligible_cards = hand
            else:
                eligible_cards = [card for card in hand
                                  if card.suit != 'Spades']

        if self.strategy == Strategy.WIN_TRICKS:
            return _likely_to_win(eligible_cards, cards_in_trick,
                                  self.spades_broken)

        elif self.strategy in (Strategy.GO_NIL, Strategy.AVOID_BAGS):
            return _most_likely_to_lose(eligible_cards, cards_in_trick)

        elif self.strategy == Strategy.OPPONENT_GOING_NIL:
            return _most_likely_to_force_opponent_out(eligible_cards,
                                                      cards_in_trick)

        elif self.strategy == Strategy.PARTNER_GOING_NIL:
            return _help_partner_going_nil(eligible_cards, cards_in_trick)

        else:
            raise RuntimeError("Unimplemented strategy {}".format(
                self.strategy))

        return eligible_cards[len(eligible_cards) - 1]
