FROM nginx:latest
# delete default config
RUN rm /etc/nginx/conf.d/default.conf
# copy new config file
COPY ./default.conf /etc/nginx/conf.d/default.conf
