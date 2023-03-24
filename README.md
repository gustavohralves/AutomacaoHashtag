# AutomacaoHashtag

Esse código usa a biblioteca PyAutoGUI para automatizar tarefas no computador, incluindo o preenchimento de formulários e cliques do mouse. O script abre o navegador Brave, acessa um site específico, insere o nome de usuário e senha, e faz login em uma conta. Em seguida, o código lê um arquivo CSV, calcula algumas informações a partir dele e envia um e-mail contendo essas informações usando o Gmail.

As bibliotecas usadas no código são:

pyautogui: para interagir com a interface gráfica do usuário
pyperclip: para copiar e colar texto na área de transferência do sistema
pandas: para ler e manipular dados em formato de tabela
os: para remover o arquivo CSV depois de lido
datetime: para obter a data atual
O código usa métodos da biblioteca pyautogui, como pyautogui.click(), pyautogui.write(), pyautogui.press(), pyautogui.hotkey() para simular a entrada do usuário e realizar tarefas específicas no navegador e no Gmail. Ele também usa métodos da biblioteca pandas para ler e manipular dados do arquivo CSV.

Este código pode ser útil para automatizar tarefas repetitivas que envolvem a manipulação de dados em planilhas, o preenchimento de formulários e o envio de e-mails com informações geradas automaticamente. É importante lembrar que, ao utilizar esse tipo de código, é necessário ter cuidado para garantir que as informações sejam inseridas corretamente e que as ações realizadas pelo código não causem danos ou erros no sistema.
