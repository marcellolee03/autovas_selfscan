import time
from getpass import getpass
from datetime import datetime
from common import check_pass
from feat import generate_prompt, scan, check_progress, ask_deepseek, ask_gemini, save_script
from feat.setup import setup


API_KEY = ''
API_URL = ''

headers = ['CVEs','NVT Name','Port','Port Protocol','Summary', 'Specific Result', 'Vulnerability Detection Method','Affected Software/OS','Solution']

password = getpass('Input user password: ')
openvas_password = getpass('Input OpenVAS admin password: ')

taskname = datetime.now().strftime("self_scan_%d-%m-%y_%H-%M")


if check_pass.check_sudo_pass(password):

    # Starting timer
    start = time.time()

    # Setting everything up on boot up
    setup.setup_autovas(password, openvas_password, taskname)
    scan.start_scan(password, openvas_password, taskname)

    # Waiting for scan to finish
    while not check_progress.check_progress(password, openvas_password, taskname):
        time.sleep(5)

    # Saving report as csv
    report_id = check_progress.get_report(password, openvas_password, taskname)['id']
    check_progress.save_report(report_id, password, openvas_password, taskname)

    # Generating shell script w/ Deepseek
    prompt = generate_prompt.generate_prompt(f'reports/{taskname}.csv', 0, headers)
    response = ask_gemini.ask_gemini(API_KEY, prompt)
    save_script.save_response(response,taskname)

    # Ending timer
    finish = time.time()

    print(response)
    print(f'time elapsed: {((finish - start)/60):.2f} minutes')

else:
    print("Wrong password. Shutting down.")
