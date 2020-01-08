# This is sample program I try scraper

import urllib.request
import ssl
from bs4 import BeautifulSoup

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

class Scrper:
    # constract
    def __init__(self, site):
        self.site = site

    # do scrape method
    def scrape(self):
        # request for web site(self.site)
        # return Response object to r 
        r = urllib.request.urlopen(self.site, context=context)

        # return HTML date to html
        html = r.read()
        # parser message 
        parser = "html.parser"
        
        # parse HTML
        sp = BeautifulSoup(html, parser)

        outputfile = "output.txt"

        # find a tag
        with open(outputfile, "w") as f:
            for tag in sp.find_all("src"):
                url = tag.get("href")
                if url is None:
                    continue
                if "html" in url:
                    print("\n" + url)
                    f.write("\n" + url)
                    
        

news0 = "https://news.yahoo.co.jp"
news1 = "file:///Users/tsujibayashiyu/Desktop/mine/名称未設定フォルダ/list.html"
Scrper(news0).scrape()



