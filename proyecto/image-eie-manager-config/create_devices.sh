curl -X PUT 'http://localhost:8080/api/2/things/eielabs:AirQualitySensor' -u 'ditto:ditto' -H 'Content-Type: application/json' -d '{
    "policyId": "eielabs:open_policy",
    "attributes": {
        "name": "Lab Air 1",
        "type": "Air Quality Sensor"
    },
    "features": {
        "air_sensor_ppm": {
            "properties": {
                "configuration": 0,
                "status": 105
            }
        },
        "air_sensor_sample_freq_minutes": {
            "properties": {
                "configuration": 5,
                "status": 5
            }
        },
        "fan_speed": {
            "properties": {
                "configuration": 2,
                "status": 2
            }
        },
        "power":{
            "properties": {
                "configuration": "on",
                "status": "on"
            }
        }
    }
}'

curl -X PUT 'http://localhost:8080/api/2/things/eielabs:lightingSystem' -u 'ditto:ditto' -H 'Content-Type: application/json' -d '{
    "policyId": "eielabs:open_policy",
    "attributes": {
        "name": "Main light",
        "type": "Lamp"
    },
    "features": {
        "light_intensity": {
            "properties": {
                "configuration": 85,
                "status": 85
            }
        },
        "light_color": {
            "properties": {
                "configuration": "bright white",
                "status": "bright white"
            }
        },
        "timer_minutes": {
            "properties": {
                "configuration": 15,
                "status": 14
            }
        },
        "power":{
            "properties": {
                "configuration": "on",
                "status": "on"
            }
        }
    }
}'
