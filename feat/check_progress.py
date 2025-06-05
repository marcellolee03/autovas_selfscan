from common import exec_tempscript

def check_progress(password, openvas_username, openvas_password, task_name):
    report = get_report(password, openvas_username, openvas_password, task_name)

    status = report['status']
    progress = report['progress']

    if progress == '100%':
        print('Scan complete!')
        return True
    else:
        print(f'Status: {status} - Progress: {progress}')
        return False


def get_report(password, openvas_username, openvas_password, task_name):
    reports = list_reports(password, openvas_username, openvas_password)

    for report in reports:
        if report['task_name'] == task_name:
            return report
    return


def list_reports(password, openvas_username, openvas_password):

    script = f'''
    docker exec -i --user auto_vas greenbone-community-edition-gvmd-1 bash -c "source /path/to/venv/bin/activate &&\
        cd auto_vas &&\
        gvm-script --gmp-username {openvas_username} --gmp-password {openvas_password} socket list-reports.gmp.py"
    '''

    output = exec_tempscript.return_output_tempscript(script, password).stdout

    # Parse da saída
    lines = output.strip().splitlines()

    reports = []
    for line in lines:
        # Ignora cabeçalhos e linhas separadoras
        if line.strip().startswith("#") or line.strip().startswith("-") or line.strip() == "":
            continue

        parts = [part.strip() for part in line.split("|")]
        if len(parts) < 7:
            continue  # Linha incompleta, pula

        relatorio = {
            "id": parts[1],
            "creation_time": parts[2],
            "modification_time": parts[3],
            "task_name": parts[4],
            "status": parts[5],
            "progress": parts[6]
        }
        reports.append(relatorio)

    return reports


def save_report(report_id, password, openvas_username, openvas_password, filename):

    script = f'''
    #!/bin/bash

    docker exec greenbone-community-edition-gvmd-1 bash -c "chmod 777 /auto_vas"
    
    docker exec --user auto_vas greenbone-community-edition-gvmd-1 bash -c "source /path/to/venv/bin/activate && cd auto_vas && gvm-script --gmp-username {openvas_username} --gmp-password {openvas_password} socket export-csv-report.gmp.py {report_id} pretty_relatorio"
    docker cp greenbone-community-edition-gvmd-1:/auto_vas/pretty_relatorio.csv "reports/{filename}.csv"
    '''

    exec_tempscript.exec_tempscript(script, password)

    print('Report saved!')
    print(f'File location: reports/{filename}.csv')