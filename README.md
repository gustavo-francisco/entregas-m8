# Ponderada 2 - Implementação de SLAM

Vídeo de funcionamento:


# Instruções de instalação:
Para este projeto será necessário: <br>
1 Turtlebot3 Burger; <br>
1 dispositivo com Ubuntu instalado;<br>
ROS;<br>
NAV2.<br>

O primeiro passo para a instalação deste projeto, é a clonagem deste repositório. Dessa forma, será possível acessar os arquivos localmente.<br>
`git clone https://github.com/gustavo-francisco/entregas-m8.git`

Partindo do princípio que o seu turtlebot já esteja configurado e com Ubuntu instalado, é necessário acessar o turtlebot. Para tal, recomenda-se o acesso por SSH.<br>
`ssh <usuário>@<hostname>`

Após isso, é necessário setar a variável de ambiente que diz qual modelo de robô está sendo utilizado:<br>
`echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc && source ~/.bashrc`

Então, inicie a operação do pacote do turtlebot3:<br>
`ros2 launch turtlebot3_bringup robot.launch.py`

O presente projeto contém 1 pacote ROS e 2 launchers. O pacote ROS possui o arquivo py responsável por fazer os comandos de movimentação ao robô.<br>
Para buildar o pacote, rode na pasta raíz do projeto:<br>
`colcon build`<br
Esse comando basicamente compila o pacote ROS.<br>
Então, de um source no script de configuração do workspace. Para isso:<br>
`source install/local_setup.bash`

Feito!

O projeto tem 2 objetivos. O primeiro é disparar todos os comandos necessários para realizar o mapeamento através de um launcher.<br>
Para isso, o primeiro passo é rodar o teleop, para conseguir comandar o robô manualmente e fazer o mapeamento com mais precisão:<br>
`ros2 run turtlebot3_teleop teleop_keyboard`<br>
Agora, acesse a pasta launch:<br>
`cd src/launch`<br>
Então, rode o launcher de mapeamento:<br>
`ros2 launch mapping_launch.py`<br>

Agora está tudo pronto pra você mapear o local!

O segundo é disparar os comandos necessário para realizar a navegação em um mapeamento já salvo, também através de um launcher.<br>
Para isso, basta rodar o launcher de navegação, pois ele já possui um script de movimentação do robô, através Simple Commander API (ref: https://navigation.ros.org/commander_api/index.html)<br>
Novamente, acesse a pasta launch:<br>
`cd src/launch`<br>
Rode o launcher de navegação:<br>
`ros2 launch navigation_launch.py`<br>
Pronto! agora seu robô está navegando no mapa que você selecionou!<br>

OBS: É possível e recomendado alterar os waypoints do script de navegação, para que o robô percorra o caminho correto e desejado no seu mapa.

Valeu!