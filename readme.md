# Para executar o Projeto
1. pip install -r requirements.txt
2. alterar variaveis (usuário e senha) no arquivo teste_case.robot
3. robot teste_case.robot
4. python clash.py


1. - sobre o fluxo:
Vc precisa pegar o IP, gerar a key e usar ela na chamada da API
2. - vc importou um módulo da api do robot mas não usou ele pra nada, nos 2 arquivos .py
<!-- 3. - bota um .gitignore -->
4. - da uma pesquisada sobre criar locators na internet, is locator que usam índices são muito frágeis e podem fazer seu código não funcionar se houver alga mudança no html.
Na doc da Selenium library fala sobre locators tbm.
5. - um robô deve ser construído pra nunca falhar, se vc enxerga alguma possibilidade de falha, é legal contornar ou por um retry pelo menos, ao invés de parar o robo.
6. - aparentemente tem umas keywords que vc não tá usando no seu arquivo .robot 
<!-- 7. - Coloca no seu readme os passos pra inicializar seu projeto. -->