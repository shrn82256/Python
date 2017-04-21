from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
from pprint import pprint
import urllib.request

def get_raw_url(file_url):
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers={'User-Agent':user_agent,}
	
	request = urllib.request.Request(file_url, None, headers)
	response = urllib.request.urlopen(request)
	data = response.read()
	soup = BeautifulSoup(data, 'html.parser')

	raw_cmd = soup.find('a', {'target':'_blank', 'title':'View in plain-text'})
	return "https://notepad.pw" + raw_cmd['href']

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

files_url = []

for i in soup.find_all('a', {'target':'_blank'}, href=True)[:-1]:
	files_url.append("https://www.%s" % i['href'][2:])

files_raw_urls = [get_raw_url(file_url) for file_url in files_url]

pprint(files_raw_urls)
	