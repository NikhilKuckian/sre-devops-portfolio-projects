#!/bin/bash

#Script to restart apache service. This script will be called from a python function if it service is found to be not running
#Author: Nikhil Kuckian
#Usage: ./apache_restart.sh
#version: 1.0

echo "$(date): Restarting Apache..." >> /mnt/c/Nikhil/Personal/study/Projects/Github/sre-devops-portfolio-projects/python/apache-monitoring/apache_monitoring.log
sudo systemctl restart apache2