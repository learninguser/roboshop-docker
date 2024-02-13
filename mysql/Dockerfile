FROM mysql:5.7
ADD  ./mysql/mysql-root /run/secrets/mysql-root
ENV  MYSQL_ROOT_PASSWORD_FILE=/run/secrets/mysql-root \
     MYSQL_DATABASE=cities \
     MYSQL_USER=shipping
ADD  ./mysql/shipping.sql /docker-entrypoint-initdb.d