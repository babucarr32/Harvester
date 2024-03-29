import os
from urllib import request
import re
import sys
import banner

try:
    os.remove("./.google-cookie")
except:
    pass

print(banner.bannerDisplay)

help = """
Usage: <main.py v> #This will scrape links
                 and sublinks for urls containig the query.

        <main.py> #This will only scrape the first link(s) 
                    for url conatining the query.
"""
print(help)

try:
    from bs4 import BeautifulSoup
    import requests
    from googlesearch import search
except Exception as e:
    print('Module not found: Make sure you have BeautifulSoup and google installed')

def Harvester():
    query = input('Enter query: ')
    targets = []
    secondTarget = []
    validTargets = []
    targetLinks = []
    count = 0
    print("Searching, this might take time...")
    try:
        for q in search(query, tld="co.in", num=10, stop=10, pause=3): # search the web 
            targets.append(q)
            print(q)

        for target in targets: # attacking target websites
            count += 1
            htmlText = requests.get(target).text
            mySoup = BeautifulSoup(htmlText, 'lxml')
            links =  mySoup.find_all("a")
            for link in links:
                try:
                    x = link['href']
                    if query in x:
                        secondTarget.append(x)
                        validTargets.append(x)
                        print(f"Found {count} urls")
                except Exception as e:
                    pass
        
        if "v" in sys.argv:
            for target in secondTarget:
                try:
                    htmlText = requests.get(target).text
                    mySoup = BeautifulSoup(htmlText, 'lxml')
                    links =  mySoup.find_all("a")
                    for link in links:
                        try:
                            x = link['href']
                            if query in x:
                                validTargets.append(x)
                                print(f"Found {count} urls")
                        except Exception as e:
                            pass
                except Exception:
                    pass
            print(validTargets)
        else:
            print(validTargets)
    except Exception as e:
        print(e)
        pass
    return targetLinks
if __name__ ==  '__main__':
    Harvester()
