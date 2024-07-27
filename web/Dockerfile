FROM nginx
RUN rm -rf /usr/share/nginx/html/*
ADD static /usr/share/nginx/html/
RUN mkdir -p /etc/nginx/default.d/
# COPY ./web/default.conf /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/default.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
