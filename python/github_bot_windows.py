import mechanize,cookielib
from mechanize import Browser
from bs4 import BeautifulSoup
import json, timeit
import HTMLParser

br= mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)


r=br.open('https://github.com/login?return_to=%2Fdrekhi12')
html=r.read()
soup=BeautifulSoup(html,"html.parser")
br.select_form(nr=0)
br.form['login']= 'drekhi12'
br.form['password'] = 'test'
response=br.submit()

if(response.geturl()=="https://github.com/drekhi12"):
	print"Success!"

else:
	print "Failed :("
	print "The Username or Password is incorrect"
