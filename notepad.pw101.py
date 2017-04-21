from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
from pprint import pprint

browser = RoboBrowser(
	history=True, 			
	user_agent='Mozilla/5.0 ... Safari/537.36',
	parser='lxml'
)
login_url = 'https://notepad.pw/account/login'
browser.open(login_url)

form = browser.get_form(action="/account/check_account")
uid = 'shrn82256'
form['username'].value = uid
form['password'].value = uid
browser.submit_form(form)

soup = browser.parsed
"""
courses = [i.get_text().strip().split('_')[0] for i in soup.find_all('div', {'class':'m-l-1'})]
pprint(courses)
"""

files_url = []

for i in soup.find_all('a', {'target':'_blank'}, href=True)[:-1]:
	files_url.append("https://www.%s" % i['href'][2:])
pprint(files_url)

for i in files