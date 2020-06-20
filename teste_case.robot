*** Settings ***
Library           SeleniumLibrary
Variables         ptest.py

*** Variables ***
${URL}          https://developer.clashroyale.com/#/login
${BROWSER}      chrome
${email}        lucasnaldo@gmail.com
${password}     123lu123
${key}          teste
${description}     testeDescription
${var}=         ${varip}     


*** Test Cases ***
Log in
    Open Browser    ${URL}    ${BROWSER}
    Log in    ${email}    ${password}

*** Keywords ***
My Keyword
    [Arguments]    ${path}
    Directory Should Exist    ${path}
    LOG                       ${path}

Open ClashRoyale by Chrome
    Open Browser    ${URL}    ${BROWSER}
    LOG                       ${URL}
    LOG                       ${BROWSER}
    Wait Until Page Contains    Log In

Log in
    [Arguments]    ${email}    ${password}
    Wait Until Page Contains    Log In
    Wait Until Page Contains    Email
    Maximize Browser Window 
    Input Text     email     ${email}
    Wait Until Page Contains    Password
    Input Password      password     ${password}
    Click Button    Log In
    Wait Until Page Contains    Enter the Arena with Clash Royale API
    Click Element         xpath=//*[@id="content"]/div[1]/div[2]/div[1]/header[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]
    Click Element         xpath=//*[@id="content"]/div[1]/div[2]/div[1]/header[1]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[1]/a[1]
    Wait Until Page Contains    Create New Key
    Click Element         xpath=//*[@id="content"]/div[1]/div[2]/div[1]/div[1]/section[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/div[1]
    ${token} = Get Text   xpath=//*[@id="content"]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/samp[1]
    # Click Element         xpath=//*[@id="content"]/div[1]/div[2]/div[1]/div[1]/section[2]/div[1]/div[1]/div[2]/p[1]/a[1]/span[2]
    # Wait Until Page Contains    Create a Key
    # Input Text     xpath=//*[@id="name"]     ${key}
    # Input Text     xpath=//*[@id="description"]     ${description}
    # Input Text     xpath=//*[@id="range-0"]     ${var}
    # Click Button    Create Key
