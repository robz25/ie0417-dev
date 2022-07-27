curl -X PUT 'http://localhost:8080/api/2/things/eielabs:AirQualitySensor' -u 'ditto:ditto' -H 'Content-Type: application/json' -d '{
    "policyId": "eielabs:open_policy",
    "attributes": {
        "name": "Lab Air 1",
        "type": "Air Quality Sensor"
    },
    "features": {
        "configuration": {
            "properties": {
                "sample frequency minutes": 5,
		"fan speed": 2,
		"power": "on"
            }
        },
        "status": {
            "properties": {
                "ppm": 101,
		"battery": 85,
		"time on minutes": 30,
	        "maximum read": 460,
		"minumum read": 85	
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
        "configuration": {
            "properties": {
                "intensity": 85,
		"timer minutes": 25,
		"color": "bright white",
		"power": "on"
            }
        },
        "status": {
            "properties": {
		"timer left timer": 0,
		"time on minutes": 30
            }
        }
    }
}'


