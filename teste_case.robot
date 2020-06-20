*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           BuiltIn
Library           Collections
Library           Process
Library           ipfinder.py
Library           clash.py
Variables           ipfinder.py
Variables           clash.py

*** Variables ***
${URL}          https://developer.clashroyale.com/#/login
${BROWSER}      chrome
${email}        lucasnaldo@gmail.com
${password}     123lu123
${key}          teste
${description}     testeDescription
${tokenstr}
${getc}   


*** Test Cases ***
Test Case
    Log level
    Open ClashRoyale by Chrome
    Log in    ${email}    ${password}
    Menu Superior
    New Key

*** Keywords ***
Retry
    Run Keyword N Times And Stop If Success    5    Login    @{args}

Log level
    Set Log Level    DEBUG

Open ClashRoyale by Chrome
    # Abre o chromedriver
    Open Browser    ${URL}    ${BROWSER}

Log in
    [Arguments]    ${email}    ${password}
    Wait Until Page Contains    Log In
    Wait Until Page Contains    Email
    # Maximiza o browser
    Maximize Browser Window 
    # Entra com email e senha
    Input Text     email     ${email}
    Wait Until Page Contains    Password
    Input Password      password     ${password}
    #Clica botão de login
    Click Button    Log In
    Wait Until Page Contains    Enter the Arena with Clash Royale API

Menu Superior
    # Clica no Menu superior direito
    Click Element         xpath=//*[@id="content"]/div[1]/div[2]/div[1]/header[1]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]/span[1]
    # Clica no item My Account
    Click Element         xpath=//*[@id="content"]/div[1]/div[2]/div[1]/header[1]/div[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[1]/a[1]
    Wait Until Page Contains    Create New Key
    # Clica no botão Create New Key
    Click Element         xpath=//*[@id="content"]/div[1]/div[2]/div[1]/div[1]/section[2]/div[1]/div[1]/div[2]/p[1]/a[1]/span[2]    
    Wait Until Page Contains    Create a Key

New Key
    # Digita Key Name, Description
    Input Text     xpath=//*[@id="name"]     ${key}
    Input Text     xpath=//*[@id="description"]     ${description}
    # Traz ip por chamada python a API
    ${var}=  evaluate  ipfinder.ip_get()  modules=ipfinder
    # Cola IP no campo
    Input Text     xpath=//*[@id="range-0"]     ${var}
    # Clica no botão Create Key
    Click Button    Create Key
    Wait Until Page Contains    teste
    # Clica no Key Name desejado
    Click Element         xpath=//*[@id="content"]/div[1]/div[2]/div[1]/div[1]/section[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]/div[1]/h4[1]
    Wait Until Page Contains    Back to My Keys
    # Copia o Token
    ${token}=   Get Text   xpath=//*[@id="content"]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/samp[1]
    ${tokenstr}=    Convert To String   ${token}
    Set Global Variable    ${tokenstr}
    # Executa funçao da API do clash royale
    ${xxx}=  evaluate  clash.get_clan()  modules=clash
    Log To Console      arquivo .robot finalizado com sucesso!
    # Close Browser
