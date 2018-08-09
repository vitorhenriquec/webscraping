from urllib.request import urlopen
html = urlopen('http://www.codcad.com/')
print(html.read())
