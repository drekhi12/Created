from bs4 import BeautifulSoup
import HTMLParser
import urllib2

i=1
f=open("link.txt", "a+")
while i<=50:
	url ="https://www.justdial.com/Bangalore/Tutorials/nct-10502492/page-"+str(i)
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	page = urllib2.urlopen(req).read()
	soup=BeautifulSoup(page,'html.parser')

	urls = []
	address= soup.findAll('span',{'class':'jcn'})
	for addresses in address:
		urls.append(addresses.find('a').attrs['href'])

	for url in urls	:
		f.write(url)
		f.write('\n')
	print i
	i=i+1

f.close() 
