FROM nginx
RUN rm -rf /usr/share/nginx/html/*
ADD ./web/static /usr/share/nginx/html/
RUN mkdir -p /etc/nginx/default.d/
# COPY ./web/default.conf /etc/nginx/conf.d/default.conf
COPY ./web/default.conf /etc/nginx/default.d/default.conf
COPY ./web/nginx.conf /etc/nginx/nginx.conf