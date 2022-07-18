# Dockerfile

FROM python:3.9.13-buster

# copy source and install dependencies
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /scripts
WORKDIR /scripts
COPY requirements.txt /
COPY ditto_config.sh /scripts/
COPY create_mqtt_connection.sh /scripts/
COPY create_policy.sh /scripts/
RUN pip install -r ../requirements.txt --cache-dir /opt/app/pip_cache
RUN chmod +x ditto_config.sh

# start cliente
# EXPOSE 8020
STOPSIGNAL SIGTERM
#CMD ["ditto_config.sh"]
ENTRYPOINT ["/scripts/ditto_config.sh"]

