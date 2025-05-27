import time
from getpass import getpass

from common import check_pass
from feat import generate_prompt, scan, check_progress, ask_deepseek
from feat.setup import setup


API_KEY = ''
API_URL = ''

headers = []

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
    #prompt = generate_prompt.generate_prompt('results/out.csv', 0, headers)
    #response = ask_deepseek.ask_deepseek(API_KEY, API_URL, prompt)

    # Ending timer
    finish = time.time()

    #print(response)
    print(f'time elapsed: {finish - start}')

else:
    print("Wrong password. Shutting down.")