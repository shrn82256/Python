from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
from pprint import pprint
import getpass
browser = RoboBrowser(
	history=True, 			
	user_agent='Mozilla/5.0 ... Safari/537.36',
	parser='lxml'
)
login_url = 'http://moodlecc.vit.ac.in/login/index.php'
browser.open(login_url)

form = browser.get_form(id="login")		#{'name':'stud_login'}
uid = input('Reg. No.:')
passwd = getpass.getpass()
form['username'].value = uid
form['password'].value = passwd
browser.submit_form(form)

soup = browser.parsed

for i in soup.find_all('h3')[2:]:
	print(i.get_text())
