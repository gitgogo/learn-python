#encoding=utf-8

Feature: login and logout

   Scenario: Successful Login with Valid Credentials
      Given Launch a browser
      When User visit to http://mail.126.com Page
      And User enters UserName"testman1980" and Password"wulaoshi1978"
      Then Message displayed Login Successfully

    Scenario: Successful LogOut
        When User LogOut from the Application
        Then Message displayed LogOut Successfully
