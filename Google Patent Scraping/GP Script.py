import time
import json
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pandas as pd

SERVICE_PATH = "C:/Users/hp/OneDrive/Bureau/Google Patent Scraping/chromedriver.exe"

service = Service(SERVICE_PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://patents.google.com/?q=(drone)&oq=drone")
time.sleep(10)
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

# Write DataFrame to Excel (XLSX)
xlsx_file = 'patent_data.xlsx'
df.to_excel(xlsx_file, index=False)

print("Data saved to Excel file:", xlsx_file)

   
