import requests
import array
from bs4 import BeautifulSoup
import urllib.request

def dl_img(url, path, name):
    f_path = path + name + '.png'
    urllib.request.urlretrieve(url, f_path)

print("Input the thread url")
url = input()
r = requests.get(url)
src = r.content
soup = BeautifulSoup(src, 'html.parser')
imgs = soup.find_all("img")
j = 0
for i in imgs:
    j+=1
    k = i.get('src')
    dl_img('https:' + k, 'images/', str(j))
    print(k)
        
    



