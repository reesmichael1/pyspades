from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pydealer
import pyspades.bidder
import random

scenarios('features/bidding.feature')


def add_numbered_cards_of_suit_to_hand(hand, n, suit):
    numbered_cards = ['2', '3', '4', '5', '6', '7', '8', '9']
    for _ in range(n):
        random.shuffle(numbered_cards)
        hand.add(pydealer.Card(numbered_cards.pop(), suit))


@given('I have a hand of cards')
def hand_of_cards():
    return pydealer.Stack()


@when(parsers.cfparse('I have {num:d} numbered {suit}'))
def add_numbered_cards(hand_of_cards, num, suit):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, num, suit)


@when(parsers.cfparse('I have the {value} of {suit}'))
def add_card_of_value(hand_of_cards, value, suit):
    hand_of_cards.add(pydealer.Card(value, suit))


@when('I have the three lowest Hearts')
def add_three_lowest_hearts(hand_of_cards):
    hand_of_cards.add(pydealer.Card('Two', 'Hearts'))
    hand_of_cards.add(pydealer.Card('Three', 'Hearts'))
    hand_of_cards.add(pydealer.Card('Four', 'Hearts'))


@when('Asked to score my hand')
def score_hand(hand_of_cards):
    return pyspades.bidder.get_bid_for_hand(hand_of_cards)


@then(parsers.re(r'I expect to win (?P<num>\d+) trick(s*)'),
      converters=dict(num=int))
def win_number_of_tricks(hand_of_cards, num):
    assert score_hand(hand_of_cards) is num
