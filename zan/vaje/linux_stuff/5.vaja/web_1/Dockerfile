FROM php:8.3-apache

RUN apt update && \
		apt install -y iputils-ping && \
		docker-php-ext-install mysqli && \
		docker-php-ext-enable mysqli

COPY php/* /var/www/html/
