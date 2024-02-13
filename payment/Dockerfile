FROM    python:3.6
WORKDIR /app
ADD     ./payment/ .
RUN     pip install -r requirements.txt
ENV     AMQP_USER=roboshop \
        AMQP_PASS=roboshop123
EXPOSE  8080
CMD     ["uwsgi", "--ini", "payment.ini"]