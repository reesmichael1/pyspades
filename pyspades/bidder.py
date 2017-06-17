import math
from pydealer.const import VALUES, SUITS

NON_SPADE_SUITS = [suit for suit in SUITS if suit != 'Spades']


def get_bid_for_hand(hand):
    if _should_go_nil(hand):
        return 0
    return (_get_guaranteed_number(hand) +
            _get_non_spades_aces(hand) +
            _get_expected_tricks_from_kings(hand) +
            _get_expected_from_surprise_spades(hand) +
            _get_extra_from_spades(hand))


def _get_guaranteed_number(hand):
    spades = sorted(_get_all_spades(hand))
    spades.reverse()

    guaranteed = 0

    for index, spade in enumerate(spades):
        if spade.value == VALUES[-(index+1)]:
            guaranteed += 1
        else:
            break

    return guaranteed


def _get_non_spades_aces(hand):
    return len([card for card in hand if card.value == 'Ace' and
                card.suit in NON_SPADE_SUITS])


def _get_expected_tricks_from_kings(hand):
    kings = [card for card in hand if card.value == 'King']
    expected_kings = 0
    for king in kings:
        if 1 < len(_get_all_cards_of_suit(hand, king.suit)) < 5:
            expected_kings += 1
    return expected_kings


def _get_extra_from_spades(hand):
    all_spades = _get_all_spades(hand)
    unused_spades = (len(all_spades) -
                     _get_guaranteed_number(hand) -
                     _get_expected_from_surprise_spades(hand))
    # Arbitrary for now
    return int(math.floor(0.5 * unused_spades))


def _get_expected_from_surprise_spades(hand):
    accumulated_spades = 0
    surprise_spades = 0
    spades = _get_all_spades(hand)
    available_spades = len(spades) - _get_guaranteed_number(hand)
    for suit in NON_SPADE_SUITS:
        cards = _get_all_cards_of_suit(hand, suit)
        if len(cards) <= 2 and accumulated_spades < available_spades:
            surprise_spades += 1
            accumulated_spades += 1

    return surprise_spades


def _should_go_nil(hand):
    if _get_guaranteed_number(hand) > 0:
        return False
    for suit in NON_SPADE_SUITS:
        cards = sorted(_get_all_cards_of_suit(hand, suit))
        numbered_cards = [card for card in cards if card.value in VALUES[:8]]
        face_cards = cards[len(numbered_cards):]
        if len(face_cards) - 2 >= numbered_cards:
            return False
    spades = _get_all_spades(hand)
    if len(spades) > 3:
        return False
    face_spades = [spade for spade in spades if spade.value in VALUES[:8]]
    if len(face_spades) > 1:
        return False
    return True


def _get_all_cards_of_suit(hand, suit):
    return [card for card in hand if card.suit == suit]


def _get_all_spades(hand):
    return _get_all_cards_of_suit(hand, 'Spades')
