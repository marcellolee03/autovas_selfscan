from common import exec_tempscript


def start_scan(password, openvas_password):
        
    with open("feat/setup/startscan.csv", "w") as file:
        file.write("self_scan")
    
    script = f'''
    #!/bin/bash

    docker cp feat/setup/startscan.csv greenbone-community-edition-gvmd-1:/auto_vas/startscan.csv

    docker exec -i --user auto_vas greenbone-community-edition-gvmd-1 bash -c "
        source /path/to/venv/bin/activate &&
        cd auto_vas &&
        gvm-script --gmp-username admin --gmp-password {openvas_password} socket start-scans-from-csv.py startscan.csv"

    '''

    exec_tempscript.exec_tempscript(script, password)