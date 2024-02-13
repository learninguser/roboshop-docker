FROM    node:18
RUN     adduser roboshop
USER    roboshop
WORKDIR /app
COPY    ./user/package.json .
COPY    ./user/server.js .
RUN     npm install
EXPOSE  8080
ENV     MONGO=true
CMD     ["node", "server.js"]