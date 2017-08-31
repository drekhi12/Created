from bs4 import BeautifulSoup
import HTMLParser
import urllib2
import xlwt

url = raw_input("Enter the link : ")
#"https://www.justdial.com/Bangalore/Tutorials/nct-10502492/page-"
number_of_pages = input("Enter how many Pages are there : ")
i=1
f=open("link.txt", "a+")
while i<=number_of_pages:
	url =  url + str(i)
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

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
w=0

i=0
f=open("link.txt", "r")
contents =f.readlines()
for x in contents:
	url =str(x)
	print url
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	page = urllib2.urlopen(req).read()
	soup=BeautifulSoup(page,'html.parser')
	contact = []
	flag=0
	for name in soup.findAll("span", { "class" : "fn" }):
		sheet1.write(w, 0, name.text)
	for contacts in soup.findAll("a",{"class":"tel"}):
		contact.append(contacts)
		flag=1
	if flag==1:
		sheet1.write(w, 1, contact[0].text)
		sheet1.write(w, 2, contact[1].text)
	for address in soup.findAll("span",{"class":"jaddt"}):
		sheet1.write(w, 3, address.text)
	print i
	w=w+1
	i=i+1
	book.save("coaching.xls")