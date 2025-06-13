FROM ubuntu:24.04

EXPOSE 1337

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install socat coreutils

WORKDIR /app

COPY flag.txt /app
COPY server /app
COPY entrypoint.sh /app

CMD ["/app/entrypoint.sh"]
