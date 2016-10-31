from bs4 import BeautifulSoup
import HTMLParser
import urllib2
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER


url="http://japtem.com/arifureta-volume-4-chapter-8/"
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
page = urllib2.urlopen(req).read()
soup=BeautifulSoup(page,'html.parser')
for cont in soup.findAll("div", {"class": "post-content"}):
    para= cont.findAll('p')
    hdr= cont.find('h3')
header= hdr.text
content=[]
for p in para:
    content.append(p.text)
    content.append("\n")

# Content
styles = getSampleStyleSheet()
elements = []
elements.append(Paragraph(header, styles["Normal"]))
elements.append(Paragraph("", styles["Normal"]))
for i in content:
    elements.append(Paragraph(i, styles["Normal"]))
# Build
doc = SimpleDocTemplate("manga.pdf", pagesize=LETTER)
doc.build(elements)
