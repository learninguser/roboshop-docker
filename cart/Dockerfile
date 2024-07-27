FROM    node:18
RUN     adduser roboshop
USER    roboshop
WORKDIR /app
COPY    package.json .
COPY    server.js .
RUN     npm install
EXPOSE  8080
CMD     ["node", "server.js"]
