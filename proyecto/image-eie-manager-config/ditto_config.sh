#!/bin/bash

# -e to consider \n char

# get status code of a call to REST API from Ditto
status_code=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/api/2/things -u ditto:ditto)

while [ $status_code -ne 200 ] # if status code is not 200, API is not ready
do
	echo -e "ditto REST API host not ready, waiting 5 seconds and reattempting"
	sleep 5
	status_code=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/api/2/things -u ditto:ditto)
done

echo -e "\nConfigure ditto policy to allow access for ditto user"
bash create_policy.sh

if [ $? -gt 0 ]
then
	echo ***Error while configuring Ditto access policy***
fi

echo -e "\nOpen MQTTT connection with Ditto"
bash create_mqtt_connection.sh

if [ $? -gt 0 ]
then
	echo ***Error while configuring MQTT connection***
fi

echo -e "\n Configuration done, ready to use Ditto with Mosquitto!"


echo -e "\nCreating devices for demonstration purposes"
bash create_devices.sh

if [ $? -gt 0 ]
then
	echo ***Error while creating things***
fi

echo -e "\n Things were created, ready to use them with eieManager2.0"


