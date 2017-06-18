Feature: Bidding
    Hands are assigned the correct bid scores.

Scenario: Evaluating a strong hand
        Given I have a hand of cards
        When I have the Ace of Spades
        And I have the King of Spades # Guaranteed two tricks
        And I have the three lowest Hearts # No tricks expected
        And I have 1 numbered Diamond # Expected trick from Spades 
        And I have 4 numbered Clubs
        And I have the King of Clubs # Expected trick
        And I have 2 numbered Spades # One will be used on second Diamond
        When Asked to score my hand
        Then I expect to win 4 tricks

Scenario: Evaluating a weak hand
        Given I have a hand of cards
        When I have the King of Clubs # would normally expect one trick, but...
        And I have 8 numbered Clubs # one opponent will probably have 0 Clubs
        And I have the Ace of Spades # cannot go nil
        And I have 3 numbered Hearts
        When Asked to score my hand
        Then I expect to win 1 trick

Scenario: Evaluating a good hand to go nil
        Given I have a hand of cards
        When I have 4 numbered Clubs
        And I have 4 numbered Hearts
        And I have the Ace of Hearts
        And I have 3 numbered Diamonds
        And I have the Eight of Spades
        When Asked to score my hand
        Then I expect to win 0 tricks

Scenario: Evaluating a hand with lots of Spades
        Given I have a hand of cards
        When I have 2 numbered Clubs # one surprise
        And I have 2 numbered Hearts # another surprise
        And I have 2 numbered Diamonds # one last surprise
        And I have 7 numbered Spades # can expect two more
        Then I expect to win 5 tricks
