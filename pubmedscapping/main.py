import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import jovian

def pubmed_url(base_url):
  #create a list of URL
  urls = []
  #i taked the value of the page number and gets added to the base URL
  for i in range(11):
    urls.append(base_url+ str(i+1))
    #returns a list of URL within the range
  return urls

def get_pubmed_url(url):     # get response from url, else raise an exception if response fails.
  response = requests.get(url)

  if response.status_code != 200:
        print('Status code:', response.status_code)
        raise Exception('Failed to fetch web page ' + url) #if response is recieved, pass the response.text through 'html.parser'

  return BeautifulSoup(response.text, 'html.parser')

def getting_info(tag):  #get the information asked for and parse it into a dictionary

    Title = tag.find('a').text.strip()
    Authors = tag.find('span', class_ = 'docsum-authors full-authors').text.strip()
    Citation =  tag.find('span', class_ = 'docsum-journal-citation full-journal-citation').text.strip()
    PubMedId = tag.find('span', class_ = 'docsum-pmid').text.strip()
    Link = tag.find('a')['href']


    return{'Name_of_title' : Title,
                  'Name_ofAuthors' : Authors,
                  'Cite' :  Citation,
                  'PubMedId' : PubMedId ,
                  'Links': 'https://pubmed.ncbi.nlm.nih.gov' + Link }

def scrapping_pubmed(doc):  #find the tag that defines an article and find the matching tags using the above function

  find_tag = doc.find_all('article', class_='full-docsum')

#parsing tags to dictionary
  results = [getting_info(tag) for tag in find_tag]
  return results


def get_csv(items,path): # function to write information to a csb
  #names for headers
  a = items[0].keys()
  print(a)

  #write information to a new file
  with open(path, 'w', newline= '', encoding ='utf-8')  as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=a)
    dict_writer.writeheader()
    #for a row in items
    dict_writer.writerows(items)

def flatten(t):
    return [item for sublist in t for item in sublist]


def Parser(base_url, path):
#final function

#list that stores all the data
  an_article = []

#get urls using the pubmed_url() function
  urls= pubmed_url(base_url)

#looping over the list of urls
  for i in urls:

#request for url, download it, get the tags
    an_article.extend(scrapping_pubmed(get_pubmed_url(i)))

#write information to csv
  get_csv(an_article,path)
  print(f'Total number of articles scraped:{len(an_article)}')
  return an_article


base_url = 'https://pubmed.ncbi.nlm.nih.gov/?term=Drone'
an_article = Parser(base_url, 'drone.csv')