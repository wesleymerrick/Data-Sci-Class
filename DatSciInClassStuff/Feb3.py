from __future__ import print_function
from bs4 import BeautifulSoup
import urllib
"""
Notes from 2/3/17
"""

r = urllib.urlopen("http://www.gamespot.com/articles/free-sp4pvita-playstation-plus-games-for-februar/" +
                   "1100-6447249").read()

soup = BeautifulSoup(r, "html.parser")

stuff = soup.find_all("div", class_="js-content-entity-body")

stuff[0].get_text()

otherstuff = stuff[0].find_all('p')

for i in otherstuff:
    print(i.get_text())
