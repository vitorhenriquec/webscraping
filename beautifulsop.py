from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(),features="html.parser")
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title

title = getTitle('https://www.pythonscraping.com/exercises/exercise1.html')
if title == None:
	print("Title was not found")
else:
	print(title)

"""
try:
	html = urlopen('https://www.pythonscraping.com/exercises/exercise1.html')
except HTTPerror as e:
	print(e)
if html is None:
	print('URL is not found')
else:
	bsObj = BeautifulSoup(html.read(),features="html.parser")
	try:
		badContent = bsObj.find("nonExistingTag").h1
	except AttributeError:
		print('Tag was not found')
	else:
		if badContent == None:
			print('Tag was not found')
		else:
			#print(bsObj.h1)
			print(badContent)
"""
