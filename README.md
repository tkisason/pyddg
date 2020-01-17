# pyddg
A library that helps you scrape duckduckgo's lite search in order to programatically use ddgs results. 

Design choices were:
1. Don't use LXML or BeautifulSoup, since if you are building a crawler you will use one or the other, so lets keep it stock, so i used regexes. Is ugly, but reduces dependancies. 
1. Only dependancy is requests, but that can also be rewritten to use urllib.
1. Return URL's and descriptions as a dictionary.

Usage is trivial:

* import pyddg (or copy those 2 functions to your crawler/code)
* Run: `pyddg.DDG(query,numpages)` where query is your search string, and numpages is number of results (in pages) you want.
* numpages is iterative, so if you write 4, you will get ~171 results, i.e. results pages, 1,2,3,4

