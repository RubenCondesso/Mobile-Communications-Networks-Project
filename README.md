# Mobile-Communications-Networks-Project
Mobile Communications Networks  Project - 2018/2019

### Contributors

- [@RubenCondesso](https://github.com/RubenCondesso) - Rúben Condesso

- [@AndreMendes](https://github.com/andremendes95) - André Mendes

- [@miguelcarreiro](https://github.com/miguelcarreiro) - Miguel Carreiro

### About

Este projeto é referente ao desenvolvimento de um sistema real, baseado em Wireless LAN, que é capaz de detetar se os níveis de CO2 medidos ultrapassam um limite prejudicial para o ser humano. As ligações existentes, entre os vários componentes do sistema, são abrangidas por uma rede ad-hoc, e a informação recolhida é encaminhada ao longo dos vários nós, utilizando python sockets tendo como base uma arquitetura cliente-servidor. Poderão ser adicionados à rede ad-hoc, os sensores necessários (ou possíveis) para abranger a área em causa. No nosso caso foi usando apenas um sensor, para efeitos de simplicidade de implementação.

### How to run:

1) Ligar um PC, para servir de PC-Server (servidor do sistema);
2) No PC-Server, criar a AP referente à rede ad-hoc 2;
3) Executar o código server_PC.py, para criar a socket-server;
4) Ligar o RPi 2, onde este irá criar automaticamente a rede ad-hoc
1, e irá executar o programa da criação da socket que lhe diz
respeito, de forma automático;
5) Ligar o RPi 3, onde este irá conectar-se automaticamente à rede
ad-hoc 1, e irá executar o programa da criação da socket (lado do
cliente) que lhe diz respeito, de forma automática;
6) Montar o sistema do sensor, na breadboard, e ligar ao RPi 3;
7) Montagem concluída.
