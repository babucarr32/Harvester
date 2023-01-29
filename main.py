from os import link
from urllib import request
import re


try:
    from bs4 import BeautifulSoup
    import requests
    from googlesearch import search
except Exception as e:
    print('Module not found: Make sure you have BeautifulSoup and google installed')

def Harvester():
    query = input('Enter query: ')
    targets = []
    targetLinks = []
    print("Searching...")
    try:
        for q in search(query, tld="co.in", num=10, stop=10, pause=3): # search the web 
            targets.append(q)
            # print(q)
        
        print(targets)
        for target in targets: # attacking target websites
            # print(target)
            htmlText = requests.get(target).text
            mySoup = BeautifulSoup(htmlText, 'lxml')
            links =  mySoup.find_all("a")
            for link in links:
                try:
                    x = link['href']
                    if 'taf' in x:
                        print(x)
                except Exception as e:
                    pass
                    # return targetLinks.append(link['href'])
            # # print(mySoup.prettify())
            # break
    except Exception as e:
        print(e)
        pass
    return targetLinks
if __name__ ==  '__main__':
    Harvester()
