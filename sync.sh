#!/bin/sh

rsync -avz /media/brum/dev/python/projects/homeassistant/*.yaml root@192.168.0.200:/mnt/dietpi_userdata/homeassistant
rsync -avz /media/brum/dev/python/projects/homeassistant/custom_components/ root@192.168.0.200:/mnt/dietpi_userdata/homeassistant/custom_components

ssh root@192.168.0.200 'systemctl restart home-assistant.service'