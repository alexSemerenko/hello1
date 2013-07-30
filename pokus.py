import urllib2
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
   def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.links = []
        self.titles = []


   def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                self.links.append(attr)
                #print "     link:", attr

p = MyHTMLParser()
f = urllib2.urlopen('http://www.9gag.com')
html = f.read()
p.feed(html)
data = p.links
links = []
titles = []
output = []
i=0
while i < len(data):
    if "badge-item-img" in data[i]:
        links.append(data[i+1])
        titles.append(data[i+2])
        i=i+1
    else:
        i=i+1
for i in range(len(links)):
    output.append('{"title":"'+titles[i][1]+',"img":'+links[i][1]+',"url":'+links[i][1]+'"}')
print '{"gag":['
print ','.join(output)
print ']}' 

