# Ponderada 3
O presente projeto tem como objetivo a implementação de um chatbot, que utiliza expressões regulares como padrão de busca. O chatbot simula um robô de serviço que pode ir e retornar de 2 setores da empresa: almoxarifado e packaging.

## Vídeo de funcionamento do projeto
[Screencast from 28-11-2023 13:05:52.webm](https://github.com/gustavo-francisco/entregas-m8/assets/99208114/5340ffc2-507a-47c1-b134-c35ad3964e41)


## Instruções de instalação
O projeto está alocado em um pacote ROS.<br>
O primeiro passo da instalação é clonar o repositório remoto. Rode o seguinte comando no terminal:
`git clone https://github.com/gustavo-francisco/entregas-m8.git`

Após clonar, acesse o diretório ws localizado no diretório ponderada3:
`cd entregas-m8/ponderada3/ws`

Então, rode o comando para compilar o pacote:
`colcon build`

E garanta que você tenha feito o source no script de configuração do workspace. Para isso:
`source install/local_setup.bash`

Pronto! agora o projeto está devidamente instalado.

O funcionamento desse projeto acontece essencialmente através de um nó de ROS2. ROS2 é um framework para o desenvolvimento de robôs que facilita o fornecimento de bibliotecas e ferramentas para tal objetivo. Um nó no ROS2 é uma unidade de processamento independente que executa uma tarefa específica.

Por fim, para rodar o chatbot:
`ros2 run chatbot chatbot`

O projeto é simples e feito para aprendizagem e testagem, então é evidente que é um pouco limitado. Para o funcionamento esperado, recomenda-se frases que iniciam com "vá", "me leve/leve-me" ou "retorne" e que tenham nelas o local desejado entre almoxarifado e packaging. Lembrando que variações de letras maiúscula e acentos também funcionam.
Muito obrigado!
