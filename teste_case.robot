*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           BuiltIn
Library           Collections
Library           Process
Library           clash.py

*** Variables ***
${URL}          https://developer.clashroyale.com/#/login
${BROWSER}      chrome
${email}        lucasnaldo@gmail.com
${password}     123lu123
${key}          teste
${description}     testeDescription
${path}         
${tokenstr}
${getc}
${getm}
${save}        



*** Test Cases ***
Log in
    Open Browser    ${URL}    ${BROWSER}
    Log in    ${email}    ${password}
    Menu Superior
    New Key
    Proc


*** Keywords ***
My Keyword
    [Arguments]    ${path}
    Directory Should Exist    ${path}
    LOG TO CONSOLE            ${path}
    Set Log Level    DEBUG

Open ClashRoyale by Chrome
    # Abre o chromedriver
    Open Browser    ${URL}    ${BROWSER}
    LOG TO CONSOLE            ${URL}

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
    ${var}=  evaluate  clash.ip_get()  modules=clash
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
    Log To Console      ${tokenstr}

Proc
    ${getc}=   Start Process           python   clash.get_clan(${tokenstr})
    Log To Console      ${getc}