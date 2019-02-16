from bs4 import BeautifulSoup
import requests

def get_imgs(link):
    html = requests.get(link).content
    soup = BeautifulSoup(html, 'html.parser')
    
    finditem = soup.find_all('img')

    link_array = []

    for l in finditem:

        if l['src'][:4] == 'http':
            link_array.append(l['src'])

    return link_array