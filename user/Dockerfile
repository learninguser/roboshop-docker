FROM    node:18
RUN     adduser roboshop
USER    roboshop
WORKDIR /app
COPY    package.json .
COPY    server.js .
RUN     npm install
EXPOSE  8080
ENV     MONGO=true
CMD     ["node", "server.js"]