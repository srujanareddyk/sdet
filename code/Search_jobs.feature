Feature: Search jobs in Dice.com
  Scenario: Search for a specific job title at a specific location
    Given User enters "SDET" and "Oregon" in Jobs and location text boxes respectively
    When the user clicks Search Jobs
    Then all the related jobs are displayed in the search results

# Feature: Search jobs in Dice.com
#  Scenario Outline: Search for jobs for a list of job titles and locations
#    Given Two lists for <Location> and <JobTitle> are available
#    When each value for <Location> and <JobTitle> are entered in the Jobs and location text boxes rspectively
#    And the user clicks Search Jobs
#    Then all the related jobs are displayed in the search results
# Examples: Location and JobTitles
#    |Location |JobTitles|
#    |SDET    |ATlanta    |
#    |SDET    |Oregon    |
#    |Python Developer    |New York    |
#    |Java    |San Francisco    |