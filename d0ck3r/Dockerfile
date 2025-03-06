FROM ubuntu:latest

MAINTAINER Edibaldo Ramirez aka edibauer "edibaldo_369@proton.me"

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install -y net-tools \
    iputils-ping\
    curl \
    git \
    nano \
    apache2 \
    php

COPY test.txt /var/www/html

EXPOSE 80

ENTRYPOINT service apache2 start && /bin/bash
