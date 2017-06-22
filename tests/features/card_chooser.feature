Feature: Choose next card to play
    The correct cards to play are chosen given the game state.

Scenario: Card choice dictated by trick leading
        Given I have a hand of cards
        And My strategy is to avoid bags
        When The trick led with the 4 of Hearts
        And I have the Ace of Hearts
        And I have the 3 of Clubs
        Then I play the Ace of Hearts

Scenario: Choosing card when I am trying to avoid bags
        Given I have a hand of cards
        And My strategy is to avoid bags
        When The trick led with the 6 of Diamonds
        And I have the Ace of Diamonds
        And I have the 3 of Diamonds
        Then I play the 3 of Diamonds

Scenario: Choosing card in round when partner is going nil
        Given I have a hand of cards
        And My strategy is to help my partner go nil
        When I have the Ace of Hearts
        And The trick led with the 2 of Hearts
        And I have the 6 of Hearts
        And I have the 8 of Diamonds
        And I have the 3 of Spades
        And Spades have not been broken
        Then I play the Ace of Hearts

Scenario: Choosing card when leading trick when partner is going nil
        Given I have a hand of cards
        And My strategy is to help my partner go nil
        When I have the Ace of Hearts
        And I have the 6 of Hearts
        And I have the 8 of Diamonds
        And I have the 3 of Spades
        And Spades have not been broken
        Then I play the Ace of Hearts

Scenario: Choosing card when partner goes nil and has already played
        Given I have a hand of cards
        And My strategy is to help my partner go nil
        When I have the 3 of Diamonds
        And The trick led with the 3 of Hearts
        And My partner played the 2 of Hearts
        And My opponent played the 6 of Clubs
        And I have the Ace of Spades
        Then I play the 3 of Diamonds

Scenario: Choosing card when opponent is going nil
        Given I have a hand of cards
        And My strategy is to force my opponent to fail at going nil
        When The trick led with the 4 of Hearts
        And I have the 6 of Hearts
        And I have the 5 of Hearts
        And I have the 3 of Hearts
        And I have the Ace of Hearts
        Then I play the 5 of Hearts

Scenario: Choosing card when I am going nil and leading the trick
        Given I have a hand of cards
        And My strategy is to go nil
        When I have the 5 of Hearts
        And I have the Ace of Hearts
        And I have the 2 of Diamonds
        Then I play the 2 of Diamonds

Scenario: Choosing card when I am going nil in round
        Given I have a hand of cards
        And My strategy is to go nil
        When I have the 5 of Hearts
        And I have the 2 of Hearts
        And I have the Ace of Hearts
        And The trick led with the 6 of Hearts
        Then I play the 5 of Hearts

Scenario: Choosing card when I need to win tricks and am leading the trick
        Given I have a hand of cards
        And My strategy is to win tricks
        When I have the Ace of Hearts
        And I have the Ace of Spades
        And I have the 3 of Spades
        And Spades have not been broken
        Then I play the Ace of Hearts

Scenario: Choosing card in round when I need to win tricks
        Given I have a hand of cards
        And My strategy is to win tricks
        When I have the Ace of Hearts
        And The trick led with the Ace of Diamonds
        And I have the Ace of Spades
        And I have the 3 of Spades
        And Spades have not been broken
        Then I play the 3 of Spades 
