Feature: As a creator of a csv file
  I wish to demonstrate
  How to normalize the broken content.

  Scenario Outline: Get user input
    Given an <infile> and <outfile> are received
    When the user enters the file names
    Then the input file will be normalized

    Examples: Files
    |infile | outfile |
    |sample.csv | fixed.csv |
