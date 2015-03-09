import httplib2
import webbrowser
import random
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
s= 'http://www.geeksforgeeks.org'
to_crawl=[]
to_crawl.append(s)
status, response = http.request(s)
crawled=[]
crawled.append(s)

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            li=link['href']
            if li.find('http://www.geeksforgeeks.org')==0 and li not in crawled and li.find('forums')<0:
                to_crawl.append(li)

while len(to_crawl):
    b=to_crawl.pop()
    if b.find('http://www.geeksforgeeks.org')==0 and b not in crawled and b.find('forums')<0:
        crawled.append(b)
        status, response = http.request(b)
        for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                li=link['href']
                if b.find('http://www.geeksforgeeks.org')==0 and li not in crawled:
                    to_crawl.append(li)
                    
ls=[]

for st in crawled:
    if st.find('company_name')>=0 and st.find('#')<0 and st.find('tag')<0 and st.find('forum')<0: #Replace company_name with the company name of your choice.
        ls.append(st)

var=len(ls)
i=random.randrange (0, var-1)
webbrowser.open(ls[i], new=1, autoraise=True)
# The script takes approx. 30 minutes to run. Set the timing accordingly in case you are automating it.

