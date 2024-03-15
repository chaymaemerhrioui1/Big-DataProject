import time
import json
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pandas as pd

if value =="google_patents":

    SERVICE_PATH = "C:/Users/hp/OneDrive/Bureau/Google Patent Scraping/chromedriver.exe"

    service = Service(SERVICE_PATH)
    driver = webdriver.Chrome(service=service)

    driver.get("https://patents.google.com/?q=(drone)&oq=drone")
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    patent_results = []
    for el in soup.select("search-result-item"):
        title = el.select_one("h3").get_text()
        link = "https://patents.google.com/" + el.select_one("state-modifier")['data-result']
        image_url = el.select_one('img')['src']
        metadata = ' '.join(el.select_one('h4.metadata').get_text().split())
        date = el.select_one('h4.dates').get_text().strip()
        snippet = el.select_one('span#htmlContent').get_text()
        
        patent_results.append({
            'title': title,
            'link': link,
            'image_filename': image_url,
            'metadata': metadata,
            'date': date,
            'snippet': snippet
        })
        
    print(json.dumps(patent_results, indent=2))

    driver.quit()

    # Convert data to DataFrame
    df = pd.DataFrame(patent_results)

    # Write DataFrame to CSV
    csv_file = 'patent_data.csv'
    df.to_csv(csv_file, index=False)

    print("Data saved to CSV file:", csv_file)

if value == "pubmed":
    
    itemfull=[]

    for i in range(1,311):
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

        with open('drone.csv','w',newline='',encoding='utf-8') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(['Title', 'Author', 'Citation', 'PMID', 'Free Access', 'Abstract','url_article'])
            csvwriter.writerows(itemfull)

if value =="WIPO":
    

