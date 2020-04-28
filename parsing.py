from bs4 import BeautifulSoup
import requests
import argparse
import urllib.request

domain = 'https://www.python.org'
url = 'https://www.python.org/downloads'

parser = argparse.ArgumentParser(description = "Use this program to find and download a linux version of python by date")

parser.add_argument('-r', required=True, metavar= "date", type=str, help="Release date, for example: April 6, 2013 capitalizing the first letter of each month day and year.")

args = parser.parse_args()


args.r = "April 6, 2013"

versions = []

def get_soup(url):
    request = requests.get(url)
    return BeautifulSoup(requests.get(url).text, 'html.parser')
soup = get_soup(url)

for link in soup.select('.list-row-container li'):
    string = str(link.prettify())
    if (args.r) in string:

        splitstring = string.split()
        versions.append(splitstring[6])
        print (splitstring[6])

print (versions[0])
download = "https://www.python.org/ftp/python/"+versions[0]+"/Python-"+versions[0]+".tgz"


urllib.request.urlretrieve(download, 'RobNoakes_python'+versions[0]+".tgz")














