import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import nexmo

client = nexmo.Client(key='9451745c', secret='JYSixtc4TkzKBfzI')
def parsedata_nepse(i):
    response = requests.get('http://www.nepalstock.com/main/todays_price/index/'+str(i)+'/')
    print(response)

    soup = BeautifulSoup(response.text, 'html.parser')
    data = []
    table = soup.find('table', attrs={'class': 'table table-condensed table-hover'})
    table_body = table.findAll('tr')
    # tabledata = table_body.findAll('td')[1]
    # tabledata_closingprice = table_body.findAll('td')[5]

    # tabledata_pcprice = table_body.findAll('td')[8]
    # print(table_body)
    total = len(table_body)
    totals = total - 4
    print(totals)

    for i in range(2, totals):
        # print(i)
        trvalues = table.findAll('tr')[i]
        # print(trvalues)
        #tsvalues = trvalues.find_all('td',text="80")
        #print(tsvalues)
        while trvalues.find_all('td',text="80"):
            tdvalues = trvalues.findAll('td')[1]
            print(tdvalues)
            tdvalues_close = trvalues.find_all('td',attrs={'class':'alnright'})[5]
            print(tdvalues_close)
            tdvalues_prevclose = trvalues.findAll('td')[8]
            print(tdvalues_prevclose)
            dictionarys = {"Company Name":tdvalues,"prev closing price":tdvalues_prevclose,"today closing price":tdvalues_close}
            data.append(dictionarys)
            print(data)
            client.send_message({
                'from': 'Razu Nepse Data',
                'to': '9779813973237',
                'text': data
            })
            exit()


for i in range(0,10):
    parsedata_nepse(i)
    print("hello")


#Muktinath Bikas Bank Ltd
#Nadep Laghubitta Bittiya Sanstha Ltd.