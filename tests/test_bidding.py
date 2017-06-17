from pytest_bdd import scenario, given, when, then
import pydealer
import pyspades.bidder
import random


@scenario('bidding.feature', 'Evaluating a strong hand')
def test_bidding_strong():
    pass


@scenario('bidding.feature', 'Evaluating a weak hand')
def test_bidding_weak():
    pass


@scenario('bidding.feature', 'Evaluating a good hand to go nil')
def test_bidding_nil():
    pass


@scenario('bidding.feature', 'Evaluating a hand with lots of Spades')
def test_bidding_many_spades():
    pass


def add_numbered_cards_of_suit_to_hand(hand, n, suit):
    numbered_cards = ['2', '3', '4', '5', '6', '7', '8', '9']
    for _ in range(n):
        random.shuffle(numbered_cards)
        hand.add(pydealer.Card(numbered_cards.pop(), suit))


@given('I have a hand of cards')
def hand_of_cards():
    return pydealer.Stack()


@given('I have the Ace of Spades')
def add_ace_of_spades(hand_of_cards):
    hand_of_cards.add(pydealer.Card('Ace', 'Spades'))


@given('I have the Ace of Hearts')
def add_ace_of_hearts(hand_of_cards):
    hand_of_cards.add(pydealer.Card('Ace', 'Hearts'))


@given('I have the King of Spades')
def add_king(hand_of_cards):
    hand_of_cards.add(pydealer.Card('King', 'Spades'))


@given('I have the three lowest Hearts')
def add_three_lowest_hearts(hand_of_cards):
    hand_of_cards.add(pydealer.Card('Two', 'Hearts'))
    hand_of_cards.add(pydealer.Card('Three', 'Hearts'))
    hand_of_cards.add(pydealer.Card('Four', 'Hearts'))


@given('I have one numbered Diamond')
def add_one_numbered_diamond(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 1, 'Diamonds')


@given('I have four numbered Hearts')
def add_four_numbered_hearts(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 4, 'Hearts')


@given('I have four numbered Clubs')
def add_four_numbered_clubs(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 4, 'Clubs')


@given('I have three numbered Diamonds')
def add_three_numbered_diamonds(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 3, 'Diamonds')


@given('I have two numbered Clubs')
def add_two_numbered_clubs(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 2, 'Clubs')


@given('I have two numbered Hearts')
def add_two_numbered_hearts(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 2, 'Hearts')


@given('I have the King of Clubs')
def add_king_of_clubs(hand_of_cards):
    hand_of_cards.add(pydealer.Card('King', 'Clubs'))


@given('I have the Eight of Spades')
def add_eight_of_spades(hand_of_cards):
    hand_of_cards.add(pydealer.Card('Eight', 'Spades'))


@given('I have two numbered Spades')
def add_two_numbered_spades(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 2, 'Spades')


@given('I have three numbered Hearts')
def add_three_numbered_hearts(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 3, 'Hearts')


@given('I have eight numbered Clubs')
def add_nine_numbered_clubs(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 8, 'Clubs')


@given('I have two numbered Diamonds')
def add_two_numbered_diamonds(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 2, 'Diamonds')


@given('I have seven numbered Spades')
def add_seven_numbered_spades(hand_of_cards):
    add_numbered_cards_of_suit_to_hand(hand_of_cards, 7, 'Spades')


@when('Asked to score my hand')
def score_hand(hand_of_cards):
    return pyspades.bidder.get_bid_for_hand(hand_of_cards)


@then('I expect to win four tricks')
def win_four_tricks(hand_of_cards):
    assert score_hand(hand_of_cards) is 4


@then('I expect to win one trick')
def win_one_trick(hand_of_cards):
    assert score_hand(hand_of_cards) is 1


@then('I expect to win zero tricks')
def win_zero_tricks(hand_of_cards):
    assert score_hand(hand_of_cards) is 0


@then('I expect to win five tricks')
def win_five_tricks(hand_of_cards):
    assert score_hand(hand_of_cards) is 5
