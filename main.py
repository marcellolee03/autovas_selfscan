import time
from getpass import getpass

from common import check_pass
from feat import generate_prompt, scan, check_progress, ask_deepseek, ask_gemini
from feat.setup import setup


API_KEY = 'AIzaSyDyacoxBNh1tn8aB_QCcUslYYHUWb-_iZs'
API_URL = ''

headers = ['NVT Name', 'Summary', 'Specific Result', 'Vulnerability Detection Method']

password = getpass('Input user password: ')
openvas_password = getpass('Input OpenVAS admin password: ')

if check_pass.check_sudo_pass(password):

    # Starting timer
    start = time.time()

    # Setting everything up on boot up
    setup.setup_autovas(password, openvas_password)
    scan.start_scan(password, openvas_password)

    # Waiting for scan to finish
    while not check_progress.check_progress(password, openvas_password, 'self_scan'):
        time.sleep(5)

    # Saving report as csv
    report_id = check_progress.get_report(password, openvas_password, 'self_scan')['id']
    check_progress.save_report(report_id, password, openvas_password, 'out')

    # Generating shell script w/ Deepseek
    prompt = generate_prompt.generate_prompt('reports/out.csv', 0, headers)
    response = ask_gemini.ask_gemini(API_KEY, prompt)

    # Ending timer
    finish = time.time()

    print(response)
    print(f'time elapsed: {((finish - start)/60):.2f} minutes')

else:
    print("Wrong password. Shutting down.")