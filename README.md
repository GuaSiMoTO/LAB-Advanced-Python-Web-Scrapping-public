# LAB-Advanced-Python-Web-Scrapping

## Introduction

> ***Note:*** _This can be a pair programming activity or done independently._

Learn web scraping fundamentals by extracting product data from an e-commerce website. We'll use Selenium for browser automation and BeautifulSoup for HTML parsing. Let's build a robust scraper step by step!

Ready?

## Requirements

- [Learn how to fork this repo](https://guides.github.com/activities/forking/)
- Clone this repo into your `code/labs` folder
- Install required packages:

```bash
pip install selenium beautifulsoup4 csv
```


---
## Iteration 1: Basic Product Extraction
### Iteration 1.1 / Setup_and_Initial_Scrape
- Create a new Python file scraper.py
- Initialize Chrome WebDriver with headless mode
- Navigate to https://guanxe.com/es/3628-portatiles
- Implement explicit wait for product names to load
- Extract and print raw product names from the first page

### Iteration 1.2 / Data_Cleaning
- Clean extracted product names by removing extra whitespace
- Store cleaned names in a list
- Display total number of products found
- Print first 5 cleaned product names


## Iteration 2: Pagination Handling
## Iteration 2.1 / Single_Page_Navigation
- Locate and click the "Next Page" button
- Implement proper wait after navigation
- Extract product names from second page
- Combine results from both pages
- Display total unique products collected

### Iteration 2.2 / Multi_Page_Scraping
- Implement loop to handle 3 pages of products
- Add 2-second delay between page requests
- Handle disabled "Next Page" button at last page
- Store all products in a master list
- Display final count of scraped products


## BONUS - 


## Submission

Upon completion, run the following commands:

```
$ git add .
$ git commit -m "done"
$ git push origin main
```

Then create a Pull Request!!

![happy_coding](https://user-images.githubusercontent.com/970858/63899010-c23fc480-c9ea-11e9-84a2-542907e42362.png)
