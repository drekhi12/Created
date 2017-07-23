from bs4 import BeautifulSoup
import HTMLParser
import urllib2
import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
w=0

i=0
f=open("link2.txt", "r")
contents =f.readlines()
for x in contents:
	url =str(x)
	# print url
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	page = urllib2.urlopen(req).read()
	soup=BeautifulSoup(page,'html.parser')

	contact = []

	for name in soup.findAll("span", { "class" : "fn" }):
		sheet1.write(w, 0, name.text)
	for contacts in soup.findAll("a",{"class":"tel"}):
		contact.append(contacts)
	sheet1.write(w, 1, contact[0].text)
	sheet1.write(w, 2, contact[1].text)
	for address in soup.findAll("span",{"class":"jaddt"}):
		sheet1.write(w, 3, address.text)
	print i
	w=w+1
	i=i+1
	book.save("school3.xls")
