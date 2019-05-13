import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
#html = response.content
#print(response)

#PARSING html with beautiful soup library
# soup = BeautifulSoup(response,'html.parser')
# print(soup.findAll('a'))
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.findAll('a'))
#print(soup.prettify())

for i in range(36,len(soup.findAll('a'))+1):
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    download_url = 'http://web.mta.info/developers/'+ link
    print(download_url)
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
    time.sleep(1)