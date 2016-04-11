import urllib2
from BeautifulSoup import BeautifulSoup as BS

#url = "http://www.techniques-ingenieur.fr/ressources-documentaires/"

url = "http://www.techniques-ingenieur.fr/base-documentaire/electronique-automatique-th13/electronique-ti350/"

page = urllib2.urlopen(url)
html = page.read()

soup = BS(html)

l = []


##extract Titre section
for sect in soup.findAll('li', {'class' : 'treaty_dt puce-th13'}):
	for title in sect.findAll('span', {'class' : 'to-click color th13'}):
		print title.text


##extract Link vers doc
for ultag in soup.findAll('ul', {'class' : 'invisible clearfix'}):
		for li in soup.findAll('li', {'class' : 'sub_holder theme-th13'}):
			for link in li.findAll('a', href=True):
					if link['href'] not in l:
						l.append(link['href'])
		
		
print l