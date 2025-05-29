from common import exec_tempscript
import socket


def setup_autovas(password, openvas_password, task_name):
    print('Setting up AutoVAS...')

    with open("scripts/setup.sh") as file:
        script = file.read()
        exec_tempscript.exec_tempscript(script, password)
    
    create_target(password, openvas_password)
    create_task(password, openvas_password, task_name)


def create_target(password, openvas_password):

    # storing localhost ip
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    with open("feat/setup/ip.txt", "w") as file:
        file.write(ip_address)
        print(f"Creating target for {ip_address}...")
    

    # creating target for localhost
    script = f'''
        #!/bin/bash

        docker cp feat/setup/ip.txt greenbone-community-edition-gvmd-1:/auto_vas/ip.txt

        docker exec -i --user auto_vas greenbone-community-edition-gvmd-1 bash -c "
            source /path/to/venv/bin/activate &&
            cd auto_vas &&
            gvm-script --gmp-username admin --gmp-password {openvas_password} socket create-targets-from-host-list.gmp.py teste ip.txt"
        '''
    
    exec_tempscript.exec_tempscript(script, password)


def create_task(password, openvas_password, task_name):
    print(f'Creating task "{task_name}"...')

    with open("feat/setup/ip.txt", "r") as file:
            localhost = file.read()

    csv_content = f'"{task_name}","Target for {localhost}","OpenVAS Default","Full and fast",,,,,,,'

    with open("feat/setup/task.csv", "w") as file:
        file.write(csv_content)


    script = f'''
    #!/bin/bash

    docker cp feat/setup/task.csv greenbone-community-edition-gvmd-1:/auto_vas/task.csv

    docker exec -i --user auto_vas greenbone-community-edition-gvmd-1 bash -c "
        source /path/to/venv/bin/activate &&
        cd auto_vas &&
        gvm-script --gmp-username admin --gmp-password {openvas_password} socket create-tasks-from-csv.gmp.py task.csv"
    '''

    exec_tempscript.exec_tempscript(script, password)