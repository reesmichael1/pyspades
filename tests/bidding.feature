Feature: Bidding
    Hands are assigned the correct bid scores.

Scenario: Evaluating a strong hand
        Given I have a hand of cards
        And I have the Ace of Spades
        And I have the King of Spades # Guaranteed two tricks
        And I have the three lowest Hearts # No tricks expected
        And I have one numbered Diamond # Expected trick from Spades 
        And I have four numbered Clubs
        And I have the King of Clubs # Expected trick
        And I have two numbered Spades # One will be used on second Diamond
        When Asked to score my hand
        Then I expect to win four tricks

Scenario: Evaluating a weak hand
        Given I have a hand of cards
        And I have the King of Clubs # would normally expect one trick, but...
        And I have eight numbered Clubs # one opponent will probably have 0 Clubs
        And I have the Ace of Spades # cannot go nil
        And I have three numbered Hearts
        When Asked to score my hand
        Then I expect to win one trick

Scenario: Evaluating a good hand to go nil
        Given I have a hand of cards
        And I have four numbered Clubs
        And I have four numbered Hearts
        And I have the Ace of Hearts
        And I have three numbered Diamonds
        And I have the Eight of Spades
        When Asked to score my hand
        Then I expect to win zero tricks

Scenario: Evaluating a hand with lots of Spades
        Given I have a hand of cards
        And I have two numbered Clubs # one surprise
        And I have two numbered Hearts # another surprise
        And I have two numbered Diamonds # one last surprise
        And I have seven numbered Spades # can expect two more
        Then I expect to win five tricks
