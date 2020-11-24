#cd Coursera-test\Python_stuff\Assignment\12.2\Beautiful Soup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#prompt user for url/count/position
url = input('Enter URL:')
user_position = input("Enter position:")
value_position = int(user_position)
user_repeat = input("Enter count:")
value_repeat = int(user_repeat)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
count = 0
repeat = 0
for tag in tags:
    web_links = tag.get('href', None)
    count = count + 1
    if count == value_position:
        print(url)
        print(web_links)

        #open new tab
        for loop in range(1,value_repeat):
            count = 0
            repeat = repeat + 1
            url = web_links
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            for tag in tags:
                web_links = tag.get('href', None)
                #print("this is a list of new open tabs", web_links)
                count = count + 1
                #print(count)
                if count == value_position:
                    print(web_links)
                    break
