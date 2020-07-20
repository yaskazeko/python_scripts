from bs4 import BeautifulSoup
import urllib.request

request = urllib.request.urlopen('https://www.livescore.com/')
html = request.read()

html_pars = BeautifulSoup(html, 'html.parser')

print(html_pars)
