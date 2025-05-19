from common import check_pass
from getpass import getpass
from feat import scan
from feat.setup import setup
from feat import check_progress
from feat import ask_deepseek

password = getpass('Input user password: ')
openvas_password = getpass('Input OpenVAS admin password: ')

if check_pass.check_sudo_pass(password):

    setup.setup_autovas(password, openvas_password)
    scan.start_scan(password, openvas_password)
    check_progress.check_progress(password, openvas_password)


else:
    print("tente novamente")