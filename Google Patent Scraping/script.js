const { Builder } = require('selenium-webdriver');
const { Options } = require('selenium-webdriver/chrome');

const { JSDOM } = require('jsdom');
const fs = require('fs');

const SERVICE_PATH = "C:/Users/hp/OneDrive/Bureau/Google Patent Scraping/chromedriver.exe";

(async function() {
    const service = new chrome.ServiceBuilder(SERVICE_PATH).build();
    chrome.setDefaultService(service);

    const options = new Options();
    const driver = await new Builder().forBrowser('chrome').setChromeOptions(options).build();

    await driver.get("https://patents.google.com/?q=(drone)&oq=drone");
    await driver.sleep(4);

    const pageSource = await driver.getPageSource();
    const dom = new JSDOM(pageSource);
    const document = dom.window.document;

    const patentResults = [];
    const elList = document.querySelectorAll("search-result-item");
    elList.forEach(el => {
        const title = el.querySelector("h3").textContent;
        const link = "https://patents.google.com/" + el.querySelector("state-modifier").getAttribute('data-result');
        const image_url = el.querySelector('img').getAttribute('src');
        const metadata = el.querySelector('h4.metadata').textContent.trim().split(' ').join(' ');
        const date = el.querySelector('h4.dates').textContent.trim();
        const snippet = el.querySelector('span#htmlContent').textContent;

        patentResults.push({
            'title': title,
            'link': link,
            'image_filename': image_url,
            'metadata': metadata,
            'date': date,
            'snippet': snippet
        });
    });

    console.log(JSON.stringify(patentResults, null, 2));

    await driver.quit();

    // Convert data to CSV
    const csvData = patentResults.map(result => `${result.title},${result.link},${result.image_filename},${result.metadata},${result.date},${result.snippet}`).join('\n');
    const csvFile = 'patent_data.csv';
    fs.writeFileSync(csvFile, 'title,link,image_filename,metadata,date,snippet\n' + csvData);
    console.log("Data saved to CSV file:", csvFile);
})();
