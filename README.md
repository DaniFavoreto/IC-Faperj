# IC-Faperj

<p align="center">
 <a href="#descrição">Descrição</a> •
 <a href="#tecnologias">Tecnologias</a> • 
 <a href="#requisitos">Requisitos</a> • 
 <a href="#instalação">Instalação</a> • 
 <a href="#como-usar">Como usar</a> • 
 <a href="#testes">Testes</a> • 
 <a href="#experimental">Experimental</a> 
</p>

## Descrição

<p align="center">Projeto de iniciação científica sobre o mapeamento de estruturas utilizando visão computacional, ROS e SLAM. </p>

## Tecnologias

* Gazebo
* Rviz
* ROS
* Gmapping
* Rtab
* Explore_lite
* ROSNavigation

## Requisitos

* Uma máquina com Ubuntu 18.04.
* 4Gb de RAM no mínimo para poder rodar as simulações.

## Instalação

### Instalação do ROS
Essa lista de comandos pode ser vista também pelo site oficial do ROS http://wiki.ros.org/melodic/Installation/Ubuntu

    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    sudo apt install curl
    curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
    sudo apt-get update
    sudo apt install ros-melodic-desktop-full
    sudo apt-get upgrade
    
### Instalação dos pacotes

#### Depth-image-to-laserscan
Instalamos esse pacote para converter a imagem obtida pelo kinect em um tópico /scan utilizável pelos métodos slam. Para instalar rode o seguinte comando:

    sudo apt-get install ros-melodic-depthimage-to-laserscan

#### Gmapping
Para instalar o método slam gmapping, rode o seguinte comando:
    
    sudo apt-get install ros-melodic-slam-gmapping
    
#### Rtab-map
Para instalar o método slam rtab-map, rode o seguinte comando:

    sudo apt-get install ros-melodic-rtabmap-ros
   
#### Navegação
Para a navegação funcionar, é necessário instalar o seguinte pacote:

    sudo apt-get install ros-melodic-navigation

#### Explore_lite
Esse método é para a navegação automática, sem que exista a necessidade de selecionar end-points.

    sudo apt-get install ros-melodic-explore-lite

## Como usar
Com todos os requisitos instalados, basta configurar seu workspace para utilizar o ROS. Os próximos comandos também podem ser visualizados no site oficial do ROS http://wiki.ros.org/pt_BR/ROS/Tutorials/InstallingandConfiguringROSEnvironment.

Primeiramente, verifique se o seu sistema está com o ROS devidamente instalado:

    export | grep ROS
    
![kkk4](https://user-images.githubusercontent.com/39687418/127230147-9f679de3-fa59-4477-af54-5d30318a229d.PNG)
    
Caso não obtenha a resposta esperada, abra seu .bashrc e adicione o seguinte comando no final do arquivo:

    gedit .bashrc
    

![kkk1](https://user-images.githubusercontent.com/39687418/127230126-acda760a-cba4-4969-991b-d27474cb547f.PNG)
    
Dê um source no arquivo .bashrc fazer tudo funcionar:

    source .bashrc

    
Agora basta criar um espaço de trabalho catkin e adicionar esse projeto no novo "workspace" criado. Para criar um novo espaço de trabalho catkin, execute os seguintes comandos:

    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/src
    catkin_init_workspace
    
Com o workspace criado, precisamos buildá-lo:
    
    cd ~/catkin_ws/
    catkin_make
    
Agora, novamente abrimos o arquivo .bashrc e adicionamos o seguinte comando:

    gedit .bashrc
    
![kkk2](https://user-images.githubusercontent.com/39687418/127230132-788ae0a9-252b-4c04-9f4f-3d6d19ba05b5.PNG)
    
Damos um source novamente para finalizar:

    source .bashrc
    
Caso esteja utilizando uma máquina virtual, será necessário adicionar o seguinte comando no final do arquivo .bashrc:

![kkk3](https://user-images.githubusercontent.com/39687418/127230144-6977d4bd-9733-4d29-8f11-51d2e037ec41.PNG)

Basta clonar esse repositório dentro da pasta src do catkin_ws com o nome de p3dxbot e dar um catkin make:
    
    cd ~/catkin_ws/src
    git clone https://github.com/DaniFavoreto/IC-Faperj.git p3dxbot
    cd ~/catkin_ws/
    catkin_make

Por fim, tornamos nossos arquivos python executáveis:

    cd ~/catkin_ws/src/p3dxbot/src/scripts/
    chmod +x gen_map_csv.py 
    chmod +x gen_odom_csv.py 
    chmod +x p3dxbot_goal.py 
    chmod +x p3dx_teleop_key.py
    cd ~

## Testes

É possível controlar a movimentação do robô com o script p3dx_teleop_key, usando as teclas w a s d:

    rosrun p3dxbot p3dx_teleop_key.py

Para verificar que o mundo e o robô estão funcionando e tudo está instalado corretamente, comece rodando o seguinte comando:

    roslaunch p3dxbot p3dxworld.launch
    
Para rodar o método slam gmapping, execute o seguinte comando:

    roslaunch p3dxbot p3dx_slam.launch
    
Para rodar o método slam rtab, execute o seguinte comando:

    roslaunch p3dxbot p3dx_rtab.launch
    

## Experimental
Esses testes ainda não estão funcionando 100%. A navegação com o move_base não está com os parâmetros setados corretamente para o robô p3dx. Para rodar a navegação, rode o seguinte comando:

    roslaunch p3dxbot p3dx_navigation.launch
    
Para rodar o explore_lite, execute o seguinte comando:

    roslaunch p3dxbot explore_lite.launch



