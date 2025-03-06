FROM ubuntu:14.04
MAINTAINER edibaldo ramirez aka edibauer "edibauer_369@proton.me"

EXPOSE 22

RUN apt update && apt install ssh -y

ENTRYPOINT service ssh start && /bin/bash