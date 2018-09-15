Feature: As a creator of a csv file
  I wish to demonstrate
  How to normalize the broken content.

  Background:
    Given I am using a csv file with broken content

  Scenario: Reformat the timestamp to be YYYY-MM-DD
    Given it reads "4/1/11 11:00:00 AM" 
    Then I should see "2011-04-01 14:00:00"
