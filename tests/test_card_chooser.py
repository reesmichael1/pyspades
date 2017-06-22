import pydealer
import pytest

from pytest_bdd import given, when, then, parsers, scenarios
from pyspades.card_chooser import CardChooser
from pyspades.cards_in_trick import CardsInTrick
from pyspades.strategies import Strategy

scenarios('features/card_chooser.feature')


@given('I have a hand of cards')
def hand_of_cards():
    return pydealer.Stack()


@pytest.fixture
def card_chooser():
    return CardChooser()


@pytest.fixture
def cards_in_trick():
    return CardsInTrick()


@given(parsers.cfparse('My strategy is to {strategy}'))
def set_strategy(strategy, card_chooser):
    if strategy == 'avoid bags':
        card_chooser.strategy = Strategy.AVOID_BAGS
    elif strategy == 'help my partner go nil':
        card_chooser.strategy = Strategy.PARTNER_GOING_NIL
    elif strategy == 'go nil':
        card_chooser.strategy = Strategy.GO_NIL
    elif strategy == 'force my opponent to fail at going nil':
        card_chooser.strategy = Strategy.OPPONENT_GOING_NIL
    elif strategy == 'win tricks':
        card_chooser.strategy = Strategy.WIN_TRICKS
    else:
        raise RuntimeError('Unimplemented strategy')


@when(parsers.cfparse('The trick led with the {value} of {suit}'))
def trick_led_with(value, suit, cards_in_trick):
    cards_in_trick.play_card(pydealer.Card(value, suit))


@when(parsers.cfparse('My {player} played the {value} of {suit}'))
def card_was_played(value, suit, cards_in_trick):
    cards_in_trick.play_card(pydealer.Card(value, suit))


@when(parsers.cfparse('I have the {value} of {suit}'))
def add_card_to_hand(hand_of_cards, value, suit):
        hand_of_cards.add(pydealer.Card(value, suit))


@when('Spades have not been broken')
def spades_not_broken(card_chooser):
    card_chooser.spades_broken = False


@then(parsers.cfparse('I play the {value} of {suit}'))
def choose_card(hand_of_cards, value, suit, card_chooser, cards_in_trick):
    chosen_card = card_chooser.choose_card(hand_of_cards, cards_in_trick)
    assert chosen_card.value == value and chosen_card.suit == suit
