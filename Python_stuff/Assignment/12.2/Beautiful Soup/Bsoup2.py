# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#prompt user for count/position
user_position = input("Enter position:")
value_position = int(user_position)
user_repeat = input("Enter count:")
value_repeat = int(user_repeat)
#print(type(value_position))

# Retrieve all of the anchor tags
web_list = list()
repeat = 0
count = 0
tags = soup('a')
for tag in tags:
    web_address = tag.get('href', None)
    #print(web_address)
    #print(type(web_address))
    count = count + 1
    #print(count)
    if count == value_position:
        web_list.append(web_address)
        print(web_address)

        #open new tab
        #url = web_address
        #html = urllib.request.urlopen(url, context=ctx).read()
        #soup = BeautifulSoup(html, 'html.parser')
        #newtags = soup('a')
        #for newtag in newtags:
            #newweb_address = newtag.get('href', None)
            #print("new urls", newweb_address)
            #count = count + 1
            #if count == value_position:
                #web_list.append(newweb_address)
                #print(newweb_address)


#print(web_list)
#find_index = web_list.index("http://py4e-data.dr-chuck.net/known_by_Reean.html")
#print(find_index)
#print(web_list[value_position-1])
