from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests

#os.environ['DISPLAY'] = ':0'
user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile',
'Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3',		
]

urls_GH=['8vfvjW','fimNJ0','LUUizyf','Wl6Zu4','wAsxdjj','hLhdpy','Fon7Ana','KgaSIF','DL5t0cE','VKAdw5e','oS8SKW','u93gAN','6qQ4uz','Ml3q2N','2GQCv2','mVlIaZ','mODth7j','g79adj','Ogm9Fe','pbB4FW','Wb4G42','vxsmiu','LtsqzD','W1dSue','NfLgjN','Ncvmrn','dsXNeT','JJzyo6i','qBsgAZc','cmhj27','LGfo9ZI','2T52Bt','R5DAtXN','oqPFU5','VQEqp9','0xrm94','v7AH3F','8vfvjW','fimNJ0','LUUizyf','Wl6Zu4','wAsxdjj','hLhdpy','Fon7Ana','KgaSIF','DL5t0cE','VKAdw5e','oS8SKW','u93gAN','6qQ4uz','Ml3q2N','2GQCv2','mVlIaZ','mODth7j','g79adj','Ogm9Fe','pbB4FW','Wb4G42','vxsmiu','LtsqzD','W1dSue','NfLgjN','Ncvmrn','dsXNeT','JJzyo6i','qBsgAZc','cmhj27','LGfo9ZI','2T52Bt','R5DAtXN','oqPFU5','VQEqp9','0xrm94','v7AH3F','8vfvjW','fimNJ0','LUUizyf','Wl6Zu4','wAsxdjj','hLhdpy','Fon7Ana','KgaSIF','DL5t0cE','VKAdw5e','oS8SKW','u93gAN','6qQ4uz','Ml3q2N','2GQCv2','mVlIaZ','mODth7j','khnRUV']
#["sn2vgs","M8BX8A","EyHrD3","ZZzgb1l","MdTnsuI","gN1mJQ","mI1T0i","l9jANS","8TPX61g","q1phNNH","5MIExQ","Xv9Nkf","2utWpm","zTStzf","JQmh5fX","tuT54V","KADHzC","jLCRoA","cMHri7","oyaoulR","9z5KG6","oVrrNo","njEU7u","Ttbmqjj","hPfQsN","Dooegb","UXeGw4m","zM7ygn","TeVc5QR","KQ6vNo","AphqLR","N5OG6Z","O2FzPd","kXo8RS","TS0YkTN","Le6NaU","7QPGmV","5OjOVA","2Nb0TO","fBWF3B","Yk3PlM"]
def get_url():
	url_booyah="https://ouo.io/"+random.choice(urls_GH)
	return url_booyah



def get_firefox_profile_dir():
    if sys.platform in ['linux', 'linux2']:
        import subprocess
        cmd = "ls -d /root/.mozilla/firefox/"
        p = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE)
        FF_PRF_DIR = p.communicate()[0][0:-2]
        FF_PRF_DIR_DEFAULT = str(FF_PRF_DIR,'utf-8')
    elif sys.platform == 'win32':
        import os
        import glob
        APPDATA = os.getenv('APPDATA')
        FF_PRF_DIR = "%s\\Mozilla\\Firefox\\Profiles\\" % APPDATA
        PATTERN = FF_PRF_DIR + "*default*"
        FF_PRF_DIR_DEFAULT = glob.glob(PATTERN)[0]
 
    return FF_PRF_DIR_DEFAULT

profile_name=get_firefox_profile_dir()
print(profile_name)




firefox_options = Firefox_Options()
firefox_options.binary = "/root/EXTRA/firefox-49.0b9/firefox/firefox";
display = Display(visible=1, size=(860, 860))


#firefox_options.add_argument("--headless")




def build_driver():
	print("############################################################")
	print("srvice")
	new_driver_path = '/usr/bin/geckodriver13'
	new_binary_path = '/root/EXTRA/firefox-53.0b9/firefox/firefox'
	serv = Service(new_driver_path)
	user_agent = random.choice(user_agent_list)
	#print(user_agent)
	fp=webdriver.FirefoxProfile()
	fp.set_preference("general.useragent.override",user_agent)
	fp.set_preference("http.response.timeout",25)
	fp.set_preference('webdriver.load.strategy','unstable')
	#fp.set_preference("modifyheaders.headers.count", 2)
	#fp.set_preference("modifyheaders.headers.action0", "Add")
	#fp.set_preference("modifyheaders.headers.name0", "x-msisdn")
	ops = Firefox_Options()
	ops.binary_location = new_binary_path
	driver = webdriver.Firefox(firefox_profile=fp , service=serv, options=ops)
	driver.maximize_window()
	driver.set_page_load_timeout(30)
	#driver.implicitly_wait(30)
	return driver


def iip ():
	sourceee="http://ipecho.net/ip"
	r = requests.get(sourceee)
	ip=r.text
	return ip

def my_vpn ():
	init_fire()
	print("############################################################")
	print("kill openvpn")
	starter()
	#random_vpn=random.choice(os.listdir("serverListTCP"))
	#os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	#time.sleep(3)
	#os.system("rm -rf /var/log/openvpn/openvpn.log")
	#c_ip=iip()
	#print("Current IP :"+c_ip)
	##print(random_vpn)
	#path = "/root/OUOIO/projet1/serverListTCP/"+random_vpn
	#print("STARTING VPN !!!")
	#x = subprocess.Popen(['openvpn', '--auth-nocache', '--config',path , '--log' , '/var/log/openvpn/openvpn.log'])
	#time.sleep(10)
	#with open ('/var/log/openvpn/openvpn.log', "r") as logfile:
	#			ac_ip=iip()
	#			if logfile.read().find('Sequence Completed') !=-1:
	#				print("VPN STATUS = OK || "+ random_vpn +"||"+ ac_ip)
	#				starter()
	#				return [x ,True]
	#			else :
	#				print("VPN STATUS = OFF || "+ random_vpn )
	#				return [x ,False]
	#				try:
	#					x.kill()
	#					init_fire()
	#				except:
	#					pass






def starter():
	#init_fire()
	print("############################################################")
	#my_vpn ()
	url_booyah=get_url()
	#print(url_booyah)
	

	#time.sleep(5)

	try:
		#init_fire()
		#l0g(" [ ok ] ")
		print("Starting stage 01  !!!")
		#display.stop()
		
		print("Display is Ok  !!!")
		#driver= ''https://buleor.com/fullpage.php?section=General&pub=253984&ga=a
		driver=build_driver()
		driver.get("https://serene-keller-a6f116.netlify.app/index.html")
		time.sleep(20)
		#driver.get("https://buleor.com/fullpage.php?section=General&pub=253984&ga=a")
		#time.sleep(10)
		print("Driver OK  !!!")
		#driver.set_page_load_timeout(18)
		driver.get(url_booyah)
		print("url is Ok  !!!")
		driver.maximize_window()# display.start()
		check_web(driver,url_booyah)

		driver.close()
		print("Driver Stop !!!")
		os.system("pkill openvpn")
		print("vpn close")
		#display.stop()
		print("Display Stop !!!")
		my_vpn()
	except Exception as a:
		print("something wrong   starter"+str(a))
		try:
			driver.close()
			#display.stop()
		except:
			pass
		#init_fire()
		my_vpn ()

def check_web(driver , uur):
	print("############################################################")
	try:
		print("header  CHECK .....")
		print(driver.execute_script("return navigator.userAgent;"))
		print("web page CHECK .....")
		driver.get(uur)
		#driver.set_page_load_timeout(2)
		time.sleep(10)
		
		main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'btn-main')))
		#driver.refrech()
		time.sleep(5)
		main_button.click()
		print("button  I'M HUMMEN BEEN !!!")#Get Link
		#driver.refrech()
		time.sleep(8)
		second_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'btn-main')))
		time.sleep(5)
		second_button.click()
		print("second_button cliked !!!")
		time.sleep(3)


		print("web page working GET THE LINK !!!")
		
		try:
			main_button=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'btn-main')))
		except:
			driver.get("https://buleor.com/fullpage.php?section=General&pub=253984&ga=a")
			print("EEEEEEEEEEEEEEEEE!!!")
			time.sleep(5)
			pass
	except Exception as a:
		print("something wrong check web issu drive "+str(a))
		try:
			display.stop()
		except:
			pass
		driver.close()
		#init_fire()
		my_vpn ()

def init_fire():
	try:
		#os.system("pkill firefox")#Xephyr geckodriver13
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#os.system("pkill Xephyr")
		#os.system("pkill geckodriver13")
		os.system("rm -rf /tmp/*") 
		#os.system("clear")
		#display.start()
		print("############################################################")
	except:
		print("some_Error init_fire")



my_vpn()
