from bs4 import BeautifulSoup
from sys import argv
import urllib2, re, os, pprint

script, rename_flag, s_no = argv;
rename_flag = int (rename_flag)
s_no = int(s_no)

'''
'[S]..[E].'
'[0-9]{1,}x[0-9]'
'''

show_name = "Sherlock"
ep_identifier = '[S]..[E].'
dir = "/media/Basic_data_partition/Users/Aryan/Videos/Shows/Sherlock S%s/"
url = "http://www.epguides.com/sherlock/"

dir = dir % str(s_no).zfill(2)
names = [[]]

def get_epno_url(x):
		k = re.search('[0-9]{1,}x[0-9]{2}', x)
		if k:
			k = k.group(0)
			return (int(i) for i in k.split('x'))

def get_names():
	temp_s = 0
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content, 'html.parser')
	for i in soup.find('div', id="eplist").find_all('a', target="_blank"):
		if get_epno_url(str(i)):
			s, e = get_epno_url(str(i))
			#name = str(i.get_text()).replace('?', '')
			try:
				name = str(i.get_text()).replace('?', '')
			except:
				name = "3RR0R"
			if temp_s == s - 1:
				names[s-1].append(name)
			else:
				temp_s += 1
				names.append([name])

def get_epno_file(x):
	i = re.search(ep_identifier, x)
	if i:
		i = i.end()
		return x[i-1 : i+1]

def get_formatno(s, e):
	return "S%sE%s" % (s.zfill(2), e.zfill(2))

def rename():
	for file in os.listdir(dir):
		if get_epno_file(file) and get_epno_file(file).isdigit():
			epno = int(get_epno_file(file))
			no = get_formatno(str(s_no), str(epno))
			l = -5 if file[-4] != '.' else -4	
			new_file = "%s %s - '%s'%s" % (show_name,
				no,
				names[s_no-1][epno-1],
				file[l:]
			)
			#new_file = "%s_%s%s" % (show_name, names[s_no-1][epno-1], file[l:])
			print file, new_file
			if rename_flag:
				try:
					os.rename(dir + file, dir + new_file)
				except:
					print "3RR0R at", file
		
get_names()
rename()
#pprint.pprint(names)