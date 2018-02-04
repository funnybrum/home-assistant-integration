#!/bin/sh

rsync -avz /brum/projects/homeassistant/*.yaml root@192.168.0.55:/mnt/dietpi_userdata/homeassistant
rsync -avz /brum/projects/homeassistant/custom_components/ root@192.168.0.55:/mnt/dietpi_userdata/homeassistant/custom_components

ssh root@192.168.0.55 'systemctl restart home-assistant.service'