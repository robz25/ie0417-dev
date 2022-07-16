# Dockerfile

FROM python:3.9.13-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
# COPY nginx.default /etc/nginx/sites-available/default
# RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
#RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
#RUN mkdir -p /opt/app/psicocitas
#COPY requirements.txt start-server.sh /opt/app/
#COPY .pip_cache /opt/app/pip_cache/
#COPY psicocitas /opt/app/psicocitas/
#WORKDIR /opt/app
RUN mkdir -p /app
COPY requirements.txt /
COPY ditto_config.sh /app/
COPY create_mqtt_connection.sh /app/
COPY create_policy.sh /app/
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
#RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/app/ditto_config.sh"]
