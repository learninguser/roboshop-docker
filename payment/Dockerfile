FROM    python:3.6
RUN     useradd roboshop
USER    roboshop
WORKDIR /app
ADD     ./payment/ .
RUN     pip install -r requirements.txt
ENV     AMQP_USER=roboshop \
        AMQP_PASS=roboshop123
CMD     ["uwsgi", "--ini", "payment.ini"]