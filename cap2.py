from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def stabilishConnection(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None;
	try:
		bsObj = BeautifulSoup(html.read(),features="html.parser")
	except AttributeError as e:
		return None
	return bsObj

#bsObj = stabilishConnection('https://www.pythonscraping.com/pages/warandpeace.html')
bsObj = stabilishConnection('https://bit.ly/1KGe2Qk')


if bsObj == None:
	print('Failed to connect or read the html file')
else:
	#nameList = bsObj.findAll("span",{"class": "green","class":"red"})
	#nameList = bsObj.findAll(text='the prince')
	for child in bsObj.find('table',{'id':'giftList'}).children:
		print(child)
	for child in bsObj.find('table',{'id':'giftList'}).descendants:
		print(child)

	for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
		print(sibling)

	print(bsObj.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
	#print(len(nameList))
	'''
	for name in nameList:
		print(name.get_text())
	'''