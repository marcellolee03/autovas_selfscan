from common import check_pass
from feat import scan
from feat.setup import setup
from feat import check_progress

password = ''
openvas_password = ''

if check_pass.check_sudo_pass(password):

    setup.setup_autovas(password, openvas_password)
    scan.start_scan(password, openvas_password)
    check_progress.check_progress(password, openvas_password)

else:
    print("tente novamente")