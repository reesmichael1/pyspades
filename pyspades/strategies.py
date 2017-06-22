from enum import Enum


class Strategy(Enum):
    AVOID_BAGS = 1
    PARTNER_GOING_NIL = 2
    GO_NIL = 3
    OPPONENT_GOING_NIL = 4
    WIN_TRICKS = 5
