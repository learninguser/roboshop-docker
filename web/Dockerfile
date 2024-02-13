FROM nginx
RUN rm -rf /usr/share/nginx/html/*
ADD ./web/static /usr/share/nginx/html/
COPY ./web/default.conf /etc/nginx/conf.d/default.conf