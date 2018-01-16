# Minha instalação do Home Assistant

Instalei o [Home Assistant](https://home-assistant.io/) em minha casa, e estes são meus arquivos de configuração (YAMLs)!

#Dispositivos
* Computador simples com o Home Assistant instalado (tentei usar o Windows, mas acabei migrando para o Linux). Uso um Itautec Infoway nt2010
* [Google Home](https://store.google.com/product/google_home) - Voice Assistant/Control
* [Google Chromecast 1](https://www.google.com.au/chromecast/tv/chromecast)
* [BroadLink RM Mini 3](http://www.ibroadlink.com/rmMini3/) x2 - Controlador de Infravermelho para o ar condicionado dos quartos
* [BroadLink RM Pro](http://www.ibroadlink.com/rm/) - Controlador de Infravermelho e Radiofrequência para a sala. Controla lâmpadas e demais dispositivos 433 da casa 
* Sensor de Ambiente [Broadlink A1](http://www.ibroadlink.com/a1/) - Controlador dentro do berço do bebê
* Central de segurança [Broadlink S1](http://www.ibroadlink.com/s1c/) - Sensor de movimento e porta
* 5 Cameras IP Genéricas (Wanscam, Tenvis e Motorola)
* Relé para lâmpadas da [MSS Eletrônica](http://www.msseletronica.com/produtos/automacao/modulos-reles-rf/65/254/#topo), controlando os interruptores comuns (mudei para intererruptores pulsadores simples) via 433 MHz
* Dispositivos montados usando [Wemos D1 Mini](https://www.banggood.com/WeMos-D1-Mini-V2-NodeMcu-4M-Bytes-Lua-WIFI-Internet-Of-Things-Development-Board-Based-ESP8266-p-1115398.html) (ESP8266):
   * Controle de temperatura e fumaça/gás na cozinha com DHT22 + MQ-02:
   * Central do tempo externa (ao sol) com DHT11 + Sensor de chuva
   * Temperatura na área de lazer com DHT22
   * Temperatura num quarto DHT22

#Automações
* Ao sair de casa, apagar as luzes
* Dar as boas-vindas quando eu chego em casa
* Avisar nas caixas de som se tem cheiro de gás ou fumaça
* Muda o tema para um tema escuro de noite
* Acende as luzes de noite
* Apaga as luzes a meia noite
* Avisa sobre o dia de jogar lixo

#Prints do Sistema
![001](https://raw.githubusercontent.com/aribarreto/homeassistant/master/www/h1.png)
![001](https://raw.githubusercontent.com/aribarreto/homeassistant/master/www/h2.png)
![001](https://raw.githubusercontent.com/aribarreto/homeassistant/master/www/h3.png)
![001](https://raw.githubusercontent.com/aribarreto/homeassistant/master/www/h4.png)
![001](https://raw.githubusercontent.com/aribarreto/homeassistant/master/www/h5.png)
