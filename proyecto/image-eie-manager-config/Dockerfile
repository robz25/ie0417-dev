# Dockerfile

FROM python:3.9.13-buster

# install nginx
# RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
# COPY nginx.default /etc/nginx/sites-available/default
# RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
#RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
#RUN mkdir -p /opt/app/psicocitas
RUN mkdir -p /scripts
WORKDIR /scripts
COPY requirements.txt /
COPY ditto_config.sh /scripts/
COPY create_mqtt_connection.sh /scripts/
COPY create_policy.sh /scripts/
RUN pip install -r ../requirements.txt --cache-dir /opt/app/pip_cache
RUN chmod +x ditto_config.sh
#RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
#CMD ["ditto_config.sh"]
ENTRYPOINT ["/scripts/ditto_config.sh"]

