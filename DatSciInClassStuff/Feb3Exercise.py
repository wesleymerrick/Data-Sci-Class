from __future__ import print_function
from bs4 import BeautifulSoup
import urllib
"""
Exercises from 2/3/17
"""

# In python, pull and print out the main body text of the following website:
# http://www.thekitchn.com/17-outrageous-recipes-for-super-bowl-sunday-227804
# Then pull and list all the links.

r = urllib.urlopen("http://www.thekitchn.com/17-outrageous-recipes-for-super-bowl-sunday-227804").read()

soup = BeautifulSoup(r, "html.parser")

stuff = soup.find_all("div", class_="typset--longform")

otherstuff = stuff[0].find_all('p')

for i in otherstuff:
    print(i.get_text())

otherstuff2 = stuff[0].find_all('ul')

for i in otherstuff2:
    print(i.get_text())
