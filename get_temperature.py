from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
from pprint import pprint
from sys import argv
import urllib.request
city_name = '+'.join(argv[1:])

url = "https://www.google.co.in/search?q=tempearture+in+" + city_name
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

request = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request)
data = response.read()
soup = BeautifulSoup(data, 'html.parser')

try:
	print(Fore.YELLOW + Style.NORMAL + soup.h3.get_text(), '\n')

	data3 = soup.find('td', {'style':'white-space:nowrap;padding-right:15px;color:#666'}).contents[0]
	print(Fore.GREEN + Style.NORMAL + "Weather outside:\t",Style.BRIGHT + data3)

	all_temps = soup.find_all('span', {'class':'wob_t'})

	cur_temp = all_temps[0].contents[0]
	print(Fore.CYAN + Style.NORMAL + "Current Temperature:\t",Style.BRIGHT + cur_temp)

	wind_spd = all_temps[1].contents[0]
	print(Fore.RED + Style.NORMAL + "Wind Speed:\t\t",Style.BRIGHT + wind_spd)

except:
	print(Fore.RED + Style.BRIGHT + "Error in fetching Data!")
