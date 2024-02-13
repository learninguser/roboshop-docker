FROM mysql:5.7
ENV  MYSQL_ROOT_PASSWORD=RoboShop@1 \
     MYSQL_DATABASE=cities \
     MYSQL_USER=shipping
ADD  ./mysql/shipping.sql /docker-entrypoint-initdb.d