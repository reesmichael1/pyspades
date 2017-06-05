def get_bid_for_hand(hand):
    return (_get_guaranteed_number(hand) +
            _get_non_spades_aces(hand) +
            _get_expected_tricks_from_kings(hand) +
            _get_extra_from_spades(hand))


def _get_guaranteed_number(hand):
    return 0


def _get_non_spades_aces(hand):
    return 0


def _get_expected_tricks_from_kings(hand):
    return 0


def _get_extra_from_spades(hand):
    return 0


def _get_expected_from_surprise_spades(hand):
    return 0
