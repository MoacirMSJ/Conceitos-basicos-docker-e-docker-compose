# Docker

## O que é o docker?
  O docker é um projeto, codigo livre, utilizado para automatizar a implantção de aplicações por meio de containers. A plataforma docker permite empacotar aplicações em ambientes isolados(conainer). [[1](https://docs.docker.com/get-started/overview/]#the-docker-platform)]

  A criação destes pacotes é possivel gerar ambientes padronizados e portateis, facilitando tanto no desenvolvimento quanto na implatação das aplicações.

## O que é container?
  
  O container é um unidade de software contém todo o codigo fonte da aplicação e as dependencias necessarias para sua execução. Esta unidade é bem isolada do SO mas tal isolamento pode ser gerenciado.[[2](https://www.docker.com/resources/what-container/)][[3](https://docs.docker.com/get-started/overview/#the-docker-platform)]

  Os container são construídos a partir de imagens, executando todas as dependências especificadas.

## O que é imagem?
  A imagem é um modelo contendo todas as instruções para a construção de um container. Como uma receita, possui passo-a-passo de cada especificação utilizada no container.

  Possuem diversas imagens prontas disponíveis na internet, mas se necessário é possível criar suas **proprias imagens atravém de um arquivo dockerfile**. As imagens personalizadas geralmente utilizam uma imagem como base.

## Construindo imagens
  Para construir imagens personalizadas, é preciso criar um arquivo chamado dockerfile, neste arquivo contem os comandos para a imagem gerada.

  Alguns comandos utilizados no dockerfile:

  * FROM: Especifica a imagem base utilizada para compor a nova.
  * WORKDIR: Especifica o diretório padrão de trabalho do container.
  * COPY: Copia arquivo ou diretório para o sistema de arquvo do container.
  * ENV: Especifica uma variavel de ambiente que será disponibilizada no container.
  * RUN: Especifica comando que será executado ao contruir o container.
  * EXPOSE: Define a porta que será exposta pelo container.
  * CMD: Define o comando padrão que será executado pelo container(ex: executar a aplicação).

  #### Construindo a imagem:
  Um exemplo é apresentado dentro da pasta em [ex_1]().
  
  * No terminal entre na pasta ex_1, e para construir a imagem execute:
  
    `docker build .`

  * Adicione uma tag a imagem com **-t**, pode ser utilizada como identificado personalizado.

    `docker build -t my-image .`

  #### Executando container com a imagem

  Utilizando a imagem criada (my-image),executaremos um container.

  * No terminal execute o comando utiliza **-p** para mapear a porta do seu computador com a do container:

    `docker -p 8000:8000 run my-image`
  
    Com o comando acima o docker criará uma container com nome escolhido por ele(aleatório).

  * Para adicionar um nome ao container adicione a flag '--name':

    `docker run -p 8000:8000 --name my-container my-image`
  
  * Para parar o container execute:

    `docker stop <identificador_do_container>`
  
  Existem diversas flags que podem ser adicionadas que podem ser vistas em [Run](https://docs.docker.com/engine/reference/commandline/run/).
  
## CLI - Comandos frequentes
  * [Listar as imagens](https://docs.docker.com/engine/reference/commandline/images/):

    `docker images -a`

  * Listar containers em excução:

    `docker ps` ou `docker container ls`

  * Listar todos os containers:
    
    `docker ps -a` ou `docker container ls -a`

  * Remover container(deve estar parado):
    
    `docker rm <identificador_do_container>`

  * Verficar logs do container:

    `docker logs -f <identificador_do_container>`

  * Acesso ao bash do container:

    `docker exec -it <identificador_do_container> /bin/bash`
    
    para sair precione ctr+d

  * Mais comando podem ser em contrados na pagina [oficial do docker](https://docs.docker.com/engine/reference/commandline/docker/)
