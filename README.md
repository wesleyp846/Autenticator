# Projeto em pausa

# Script Autenticador

Este script foi desenvolvido para oferecer uma solução de autenticação em duas etapas em um sistema maior.

## Sobre
Utilizando o **Python**, este script permite que os usuários se autentiquem no sistema por meio de uma verificação em duas etapas. 

Para realizar a verificação, é necessário ter um celular com um aplicativo de verificação em duas etapas, como o **Google Authenticator**, por exemplo.

>Na primeira utilização, o script irá gerar um **QR Code** que deverá ser escaneado pelo aplicativo no celular do usuário. Isso estabelece uma conexão segura entre o sistema e o dispositivo do usuário, fortalecendo a segurança do acesso.

## Criando o Script
Para utilizar o script, é necessário instalar as seguintes dependências:
-   pyotp
-   qrcode

### Exemplo de instalação de suas dependências.
    pip install pyotp
    pip install qrcode 

## Orientações finais
Este script serve como um ponto de partida para implementar a autenticação em duas etapas em um sistema maior. 
Ele fornece um "insight" sobre como implementar essa forma de segurança em seu próprio sistema.

## Agradecimentos

Caso você tenha alguma dúvida ou sugestão de melhoria, sinta-se à vontade para entrar em contato. Espero que esse script possa ser útil na implementação de uma camada adicional de segurança em seu sistema.
