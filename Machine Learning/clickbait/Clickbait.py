from bs4 import BeautifulSoup as soup 
import numpy as np 
import requests
import pandas as pd 


#Gets headlines from a single page
def headlineretrive(link, tag, clas, name):
    nr_head = 0
    page = requests.get(link)
    #Downloads the html file
    data = page.text
    page_soup = soup(data, "html.parser")
    #Creates a file for the specific page
    f = open("textfiles/%s.txt" % name, "w")
    #Finds all header tags
    for header in page_soup.findAll(tag, {"class":clas}):
        try:
            title = header.getText()
            title = ' '.join(title.split())
        except:
            title = header.unwrap().getText()
            title = ' '.join(title.split())
        f.write(title + '\n')
        nr_head += 1
    f.close()
    return nr_head
#All tuples have (hyperlink, tag where header is, class of tag, name of page)
links = pd.read_csv("textfiles/webpages.csv")
links = np.copy(links)

total_headers = 0

for i in links:
    a = headlineretrive(i[0], i[1], i[2], i[3])
    total_headers += a

print(a)     

 

