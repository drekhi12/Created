from bs4 import BeautifulSoup
import HTMLParser
import urllib2
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

class FooterCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_canvas(page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self, page_count):
        page = "Page %s of %s" % (self._pageNumber, page_count)
        x = 128
        self.saveState()
        self.setStrokeColorRGB(0, 0, 0)
        self.setLineWidth(0.5)
        self.line(66, 78, LETTER[0] - 66, 78)
        self.setFont('Times-Roman', 10)
        self.drawString(LETTER[0]-x, 65, page)
        self.restoreState()



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
print styles
elements = []
elements.append(Paragraph(header, styles["Title"]))
elements.append(Paragraph("", styles["Normal"]))
for i in content:
    elements.append(Paragraph(i, styles["BodyText"]))
# Build
doc = SimpleDocTemplate("manga.pdf", pagesize=LETTER)
doc.multiBuild(elements, canvasmaker=FooterCanvas)
