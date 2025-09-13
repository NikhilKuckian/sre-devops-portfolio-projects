import requests # module to use http requests
import subprocess # moddule to use shell command
import datetime # module to use date time

# Defining variables for URL and Log path
URL='http://localhost'
LOG_PATH='/mnt/c/Nikhil/Personal/study/Projects/Github/sre-devops-portfolio-projects/python/apache-monitoring'

def log(message):
    timestamp=datetime.datetime.now()
    with open (LOG_PATH + '/apache_monitoring.log',"a") as log_file:
        log_file.write(f'{timestamp}:{message}\n')

def apacheresponse():
    try:
       response=requests.get(URL)
       status=response.status_code
       print(f'Reponse status code:{status}')
       log('Apache Service online')
    except requests.exceptions.RequestException as e:
        print(f'exception occured:{e}')
        log('Apache Service not online')
        log('Restarting apache...')
        subprocess.run(["/mnt/c/Nikhil/Personal/study/Projects/Github/sre-devops-portfolio-projects/python/apache-monitoring/scripts/apache_restart.sh"])

apacheresponse()