
import whois
import sys
import time
import re
import time
import math
import urllib2
import urlparse
import optparse
import hashlib
import BeautifulSoup

def web_crawler(url):
    if (depth == 0):
        return None

    try:
        page = urllib2.urlopen(url)
    except (urllib2.URLError, ValueError):
        return None

    html = page.read()
    dom = lxml.html.fromstring(html)

    print ("level %d: %s" % (depth, url))
    for link in dom.xpath('//a/@href'):
        web_crawler(link, depth - 1)

class web_scanner_utils(object):
    def __init__(self, url):
        self.url = url

    def get_domain_name(url):
        domain_name = get_tld(url)
        return domain_name

    def get_ip_addr(self.url):
        command = "host " + url
        process os.popen(command)
        results = str(process.read())
        marker = reslts.find("addr") + 12
        return results[marker:].splitlines()[0]

    def whois(self.ip_addr):
        try:
            import pass
        except ImportError:
            command = "whois " + url
            process = os.popen(command)
            results = str(process.read())
            return reslts

if (__name__ == "__main__"):
    main()
