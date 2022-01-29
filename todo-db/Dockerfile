FROM mariadb:10.3.5

RUN apt-get update & apt-get upgrade -y

ENV MYSQL_USER=todo \
    MYSQL_PASSWORD=password \
    MYSQL_DATABASE=todo \
    MYSQL_ROOT_PASSWORD=mypass

EXPOSE 3306
