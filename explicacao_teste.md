# Parte 1

# Utilizando o Robot Framework + Selenium Library: 
1. Acessar o website https://developer.clashroyale.com/  
2. Clicar no botão login  
3. Inserir usuário e senha (O cadastro não precisa ser feito pela automação, pode realizá-lo manualmente)  
4. Clicar em login 5 - Ir até o menu minha conta  
5. Criar uma nova chave  
Não é necessário, mas será um plus: Obter o endereço IP externo de maneira dinâmica ao invés de deixá-lo fixo no seu código.  


# Parte 2 

# Utilizando o Python Crie uma Custom Library que:  
6. Através da API do Clash Royale, obtenha as informações do clã de nome "The resistance", cuja tag começa com #9V2Y e que esteja localizado no Brasil.  
7. Utilizando a resposta da chamada do passo 1, realizar uma nova chamada para recuperar a lista de membros do clã.  
8. Por fim, escrever num arquivo .csv as seguintes informações de cada membro - nome(name), - level(expLevel), - troféus(trophies), - papel(role)

 
# Parte 3 

# Crie um logger: 
9. Que no level INFO, registre com mensagens claras e objetivas cada passo que o robô realiza. 
10. Que tenha o level DEBUG, mostrando conteúdo relevante para este level. 
11. Que tenha o level ERROR 
12. Escreva na tela durante a execução e também num arquivo para posterior consulta. 