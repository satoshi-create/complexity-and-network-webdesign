#!/bin/bash
mosquitto_pub -h iot-endpoint.amazonaws.com -t 'iot/topic' -m '{"temp":25.5}'
