*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kirke
    Set Password  Hello432
    Set Password Confirmation  Hello432
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  hi
    Set Password  Hello432
    Set Password Confirmation  Hello432
    Submit Register
    Register Should Fail With Message  Username too short, should be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  kirke
    Set Password  Hi12
    Set Password Confirmation  Hi12
    Submit Register
    Register Should Fail With Message  Password too short, should be at least 8 characters

Register With Valid Username And Invalid Password
    Set Username  kirke
    Set Password  Hellooo
    Set Password Confirmation  Hellooo
    Submit Register
    Register Should Fail With Message  Password must not constist of only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kirke
    Set Password  Hellooo
    Set Password Confirmation  dfdfdf
    Submit Register
    Register Should Fail With Message  Passwords do not match


Register With Username That Is Already In Use
    Create User    kalle    kalle123
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Register
    Register Should Fail With Message  User already exists

Login After Successful Registration
    Set Username    john
    Set Password    Password123!
    Set Password Confirmation    Password123!
    Submit Register
    Click Link  Continue to main page
    Submit Logout
    Login Page Should Be Open
    Set Username    john
    Set Password    Password123!
    Submit Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username    john123
    Set Password    Password123!
    Set Password Confirmation    Password123!
    Submit Register
    Page Should Contain    Username can only contain lowercase letters (a-z)
    Click Link  Login
    Login Page Should Be Open
    Set Username    john123
    Set Password    Password123!
    Submit Login
    Login Page Should Be Open
    Page Should Contain   Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register

Submit Login
    Click Button    Login

Submit Logout
    Click Button    Logout

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation 
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Welcome Page Should Be Open
    Title Should Be   Welcome to Ohtu Application!

Main Page Should Be Open
    Title Should Be   Ohtu Application main page

Login Page Should Be Open
    Title Should Be   Login

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page