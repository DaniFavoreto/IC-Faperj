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
    
| ![kkk4](https://user-images.githubusercontent.com/39687418/127230147-9f679de3-fa59-4477-af54-5d30318a229d.PNG) |
|:--:|
|*Mensagem certa de instalação*|
    
Caso não obtenha a resposta esperada, abra seu .bashrc e adicione o seguinte comando no final do arquivo:

    gedit .bashrc
    

| ![kkk1](https://user-images.githubusercontent.com/39687418/127230126-acda760a-cba4-4969-991b-d27474cb547f.PNG) |
|:--:|
|*Adicione o comando **source /opt/ros/melodic/setup.bash** ao final do arquivo*|
    
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
    
|![kkk2](https://user-images.githubusercontent.com/39687418/127230132-788ae0a9-252b-4c04-9f4f-3d6d19ba05b5.PNG)|
|:--:|
|*Adicione o comando **source ~/catkin_ws/devel/setup.bash** ao final do arquivo*|

Damos um source novamente para finalizar:

    source .bashrc
    
Caso esteja utilizando uma máquina virtual, será necessário adicionar o seguinte comando no final do arquivo .bashrc:

|![kkk3](https://user-images.githubusercontent.com/39687418/127230144-6977d4bd-9733-4d29-8f11-51d2e037ec41.PNG)|
|:--:|
|*Adicione o comando **export SVGA_VGPU10=0** ao final do arquivo*|

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




### Controlando a movimentação do robô
É possível controlar a movimentação do robô com o script p3dx_teleop_key, usando as teclas w a s d:

    rosrun p3dxbot p3dx_teleop_key.py

### Gerando o mundo e o robô
Para verificar que o mundo e o robô estão funcionando e tudo está instalado corretamente, comece rodando o seguinte comando:

    roslaunch p3dxbot p3dxworld.launch


<img src="https://user-images.githubusercontent.com/39687418/127365356-e737f157-c927-4cbf-9d3d-0d91cbe61516.PNG" width="500">

### SLAM    
Para rodar o método slam gmapping, execute o seguinte comando:

    roslaunch p3dxbot p3dx_slam.launch
    
<img src="https://user-images.githubusercontent.com/39687418/127365366-a7e84f54-eb70-4378-b13f-21e0c989750e.PNG" width="300">
    
Para rodar o método slam rtab, execute o seguinte comando:

    roslaunch p3dxbot p3dx_rtab.launch

<img src="https://user-images.githubusercontent.com/39687418/127365371-7e9ef896-2798-40f4-8011-874192c88148.PNG" width="400">

### Gerando o mapa e os dados
Para obter o mapa da barragem e gravar os dados de posição obtidos nos tópicos /odom e /map, será necessário abrir 4 terminais ao mesmo tempo. **No primeiro terminal**, rode
o método slam desejado.

**Gmapping:**

    roslaunch p3dxbot p3dx_slam.launch
 
**Rtab:**
    
    roslaunch p3dxbot p3dx_rtab.launch
   
**No segundo e terceiro terminais**, iremos rodar os métodos que vão gravar os dados de posição em um csv. São dois, respectivamente, odom e map:
    
    rosrun p3dxbot gen_odom_csv.py
    rosrun p3dxbot gen_map_csv.py
   
**No quarto e último terminal**, rodamos o método que irá mover o robô até a posição desejada:

    rosrun p3dxbot p3dxbot_goal.py
    

Gmmapping            |  Rtab
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/39687418/127372104-24caf86d-b9f4-456b-ba35-8192a5f8b65e.PNG" width="300">  |  <img src="https://user-images.githubusercontent.com/39687418/127372120-859ef071-42f2-479c-9407-ea83955b2c6b.PNG" width="300">


### Gerando os gráficos
Para obter os gráficos que mostram o percurso do robô usamos os arquivos csv gerados no passo anterior. O código está representado abaixo:

```python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# lendo os arquivos csv
df1 = pd.read_csv("gmapping_map_data.csv")
df2 = pd.read_csv("gmapping_odom_data.csv")

df3 = pd.read_csv("rtab_map_data.csv")
df4 = pd.read_csv("rtab_odom_data.csv")

# plotando o gráfico do gmapping
figure(figsize=(8, 6), dpi=80)

plt.plot(df1.x_value, df1.y_value, ':', linewidth = 7)
plt.plot(df2.x_value, df2.y_value, 'r', linewidth = 2)

plt.legend(["Posição estimada", "Posição real do robô"])
plt.title("GMapping Slam")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

# plotando o gráfico do rtab
figure(figsize=(8, 6), dpi=80)

plt.plot(df3.x_value, df3.y_value, ':', linewidth = 7)
plt.plot(df4.x_value, df4.y_value, 'r', linewidth = 2)

plt.legend(["Posição estimada", "Posição real do robô"])
plt.title("Rtab Slam")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
```

Gráfico Gmapping            |  Gráfico Rtab
:-------------------------:|:-------------------------:
<img src="https://user-images.githubusercontent.com/39687418/127374574-fcc2a9c7-7107-4f0e-9c56-e29d545bc56f.PNG" width="300">  |  <img src="https://user-images.githubusercontent.com/39687418/127374564-5f87bf73-2869-4f7d-b35a-a8fd333f08cb.PNG" width="300">

## Experimental
Esses testes ainda não estão funcionando 100%. A navegação com o move_base não está com os parâmetros setados corretamente para o robô p3dx. Para rodar a navegação, rode o seguinte comando:

    roslaunch p3dxbot p3dx_navigation.launch
    
<img src="https://user-images.githubusercontent.com/39687418/127375122-bdd6fdda-c844-46d6-8ace-725affdcfbac.PNG" width="600"> 
   
Para rodar o explore_lite, execute o seguinte comando:

    roslaunch p3dxbot explore_lite.launch



