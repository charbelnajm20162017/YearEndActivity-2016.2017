#For PMSS Coding 2016-2017 Lab Assignment 5
#Charbel Najm
#
#This script will scan the HTML of wordpress sites with the theme and layout used in Mr. Chu's 2016 classes, and return the number of posts/articles in each site.
#The scraper can also be modified to return different data about articles.
#This will not work on other wordpress themes or websites with different structure.

import sys, os, time, datetime, json, logging
logging.basicConfig(level=logging.DEBUG, format="%(threadName)-10s %(message)s",)
#print("Last Modified:", datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(sys.path[0], "WordpressScraper.py"))))


#Code below will attempt to import non-default python modules used in this script from a sibling folder named modules.
#This allows portability, if unwanted, webscraper script can be run once and have results exported as static data to be fed into the pygame visualizer.

print("\nWordpressScraper: Importing external modules...")
modulePath = os.path.realpath(os.path.join(sys.path[0], "modules/lib/python3.5/site-packages"))#Form the full path to the modules directory.
sys.path.insert(0, modulePath)#Inject new dir path into this script's list of paths to look for modules in.
try:
    import requests # Official Website: http://docs.python-requests.org/
    from bs4 import BeautifulSoup as bs # https://www.crummy.com/software/BeautifulSoup/
except:
    print("WordpressScraper: Unable to import external modules, {}, exiting...\n".format(sys.exc_info()[0]))
    sys.exit()
else:
    print("WordpressScraper: Import complete from", sys.path[0])

#It's simple:
def countArticles(site):
    siteTotal = 0 #Define and clear the total article number
    index = 1 #Define and set the index of the first page to scan, since this wordpress theme uses an infinite scrolling design, we can iterate over each page subsection using an index until we can no longer find any more articles to count.
    print("-" * (len(site)+16))
    print("Using base url: " + site)
    print("-" * (len(site)+16))# "Using base url: " is 16 characters long
    while 1: #Loop over site's pages until there are no more articles to scan = end.
        artCount = 0
        siteSearch = "{}/page/{}/".format(site, str(index))
        #Commenting out to reduce console clutter#print("Scanning: " + siteSearch)
        parse = bs(requests.get(siteSearch).content, "html.parser")#Get the HTML using Requests and pass it to BeautifulSoup for parsing!
        for div in parse.find_all(id="main"): #Find the main body container
            for element in div.children: #Grab all children of main body container
                if (element.name == "article"): #Increment the article counter when we catch an <article> element
                    artCount += 1
        siteTotal += artCount #Add the current page's article counter to the total site's articles variable. This keeps tracks of how many articles are on this site.
        if artCount == 0: #If the current page has no articles, then we have scanned them all, so end the loop.
            print("Scan complete... Please wait...")
            print("{} articles found on {}\n\n".format(siteTotal, site))
            break
        else: #If not, display this page's article count and up the index to scan the next page.
            #Commenting out to reduce console clutter#print("Found " + str(artCount) + " articles")
            #print("-"*(len(site)+16))
            index += 1
    return siteTotal

def getData(siteList):
    try:
        with open('data.txt', 'r') as f:
            data = f.read()
    except:
        print(sys.exc_info()[1])
        print("Gathering data...")
        out = {}
        for site in siteList:
            out[site]=countArticles(site) #append the results to a dictionary    
        print("Writing data...")
        with open('data.txt', 'w') as fw:
            header = "SiteName:ArticleCount %s"%(datetime.date.today())
            fw.write(json.dumps((header, out), indent=2))
        return out
    else:
        print("Reading data...")
        out = json.loads(data)#This will read a list of 2 items: a header string + a dictionary with count data
        return out[1]#We are only interested in the dictionary data. If the data is to be temporarily cached later on, this header string can be returned and used for that purpose.
    
logging.debug("--EOF--")