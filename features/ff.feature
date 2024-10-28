Feature: Github login page check

  Scenario:
    Given Launch Chrome browser
    When Open github sign in page
    And Enter a username "kiskutya" and a password "kismacska12"
    And Click on the Sign in button
    Then Error messages should appear

  Scenario Outline:
    Given Launch Chrome browser
    When Open github sign in page
    And Enter a username "<username>" and a password "<password>"
    And Click on the Sign in button
    Then Error messages should appear

    Examples:
      |  username | password |
      |  medve | 3mber45 |
      |  roka | fAr345kas |
      |  diszno | Teve007 |
      |  nyuszi | ZebRa@44 |



