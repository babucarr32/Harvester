try:
    from bs4 import BeautifulSoup
    from googlesearch import search
except Exception as e:
    print('Module not found: Make sure you have BeautifulSoup and google installed')

def Harvester():
    query = input('Enter query: ')
    for q in search(query, tld="co.in", num=50, stop=50, pause=2):
        print(j)