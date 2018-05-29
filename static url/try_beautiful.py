from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://jr.jd.com')

bs_obj = BeautifulSoup(html.read(),'html.parser')
txt_list = bs_obj.find_all('a','nav-item-primary')

for txt in txt_list:
    print(txt.get_text())
    
html.close()
