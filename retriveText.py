from bs4 import BeautifulSoup
import requests
import os 
import os.path
import csv 


#def writerows(rows, filename):
#    with open(filename, 'a', encoding='utf-8') as toWrite:
#        writer = csv.writer(toWrite)
#        writer.writerows(rows)
 

def getlistings(listingurl):

    with open(listingurl) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    mainText = soup.find("div", class_='css-2t3g1w-Text')
    #i fixed multiplying the same lines of text, i swaped 
    #mainText.findAll()
    #mainText.get_text()
    #for what is now:

    for tag in mainText:
        for childTag in tag:
            try: 
                print(childTag.get_text())
            except:
                print(childTag)

    
    return mainText


if __name__ == "__main__":

    #filename = "footballers.csv"
    #if os.path.exists(filename):
    #    os.remove(filename)
    

    listingurl = "testowy.html"



    listings = getlistings(listingurl)
    #print(listings)