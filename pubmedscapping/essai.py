from bs4 import BeautifulSoup
import requests
import csv


itemfull=[]

for i in range(1,2):
    url = "https://pubmed.ncbi.nlm.nih.gov/?term=drone&page="+str(i)
    p = requests.get(url)
    soup = BeautifulSoup(p.content, 'html.parser')
    content = soup.find_all('div', class_='docsum-wrap')
    for item in content:
        title=item.find('a',class_='docsum-title')
        author = item.find('span', class_='docsum-authors full-authors')
        citation = item.find('div', class_='docsum-citation full-citation')
        pmid = item.find('span',class_='docsum-pmid')
        free=item.find('span',class_="free-resources spaced-citation-item citation-part")
        free_text= "No" if free is None else "Yes"
        abstract =item.find("div",class_="full-view-snippet")
        url_article='https://pubmed.ncbi.nlm.nih.gov/'+str(pmid.text)+'/'
        itemfull.append([title.text,author.text,citation.text.split,pmid.text,free_text,abstract.text,url_article])
        #print(i,end=" ")

    print("title :",title.text)
    print('citation :',citation.text)
    print('author :',author.text)
    print('pmid :',pmid.text)
    print('url article',url_article)

    #items.append(name.text)
    #items.append(cite.text)
    #items.append(author.text)
    #items.append(background.text)
    #itemsfull.append(items)

    with open('drone3.csv','w',newline='',encoding='utf-8') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(['Title', 'Author', 'Citation', 'PMID', 'Free Access', 'Abstract','url_article'])
        csvwriter.writerows(itemfull)




