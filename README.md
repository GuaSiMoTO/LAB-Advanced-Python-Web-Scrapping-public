# LAB-Advanced-Python-Web-Scrapping

# LAB-Web-Scraping-Detailed-Product-Information-with-Selenium-and-BeautifulSoup

## Introduction

> **Note:** This lab can be completed in pairs or individually.

In this lab, you will learn how to:
- Access a webpage using Selenium.
- Extract a list of products from the main page.
- Click on the **first product** to enter its detail page and extract specific information (e.g., the price).
- Later modify your script to extract the same detailed information for **all products** on the page without navigating to additional pages.

Let's get started!

---

## Requirements

- [Learn how to fork this repo](https://guides.github.com/activities/forking/)
- Clone this repository into your `code/labs` folder.
- Install the following dependencies:
  - **Selenium**
  - **BeautifulSoup4**
  - *(Optional)* **webdriver-manager** for easier ChromeDriver management

> **Tip:** Using webdriver-manager can simplify the management of your ChromeDriver, eliminating the need for manual downloads.

---

## Iteration 1: Extract Information from the First Product

### 1.1 / Access and Setup

1. Configure the Chrome driver using Selenium's ChromeOptions.
2. Navigate to the main page:  
   `https://guanxe.com/es/3628-portatiles?p=1`
3. Use a waiting mechanism (such as WebDriverWait) to ensure that elements with the class `product-name` are present on the page.

### 1.2 / List and Select the First Product

1. Use BeautifulSoup to extract the list of products (for example, by retrieving all `<a>` elements with the class `product-name`).
2. Save the list of product links.
3. Click on the **first product** in the list to navigate to its detail page.

### 1.3 / Extract Detailed Information

1. Once on the product detail page, extract the required information:
   - **Price:** Locate the element that contains the price (adjust the selector based on the page’s HTML structure).
   - *(Optional)* Other details such as product name, description, etc.
2. Store the extracted information in variables and print them to the console for verification.

---

## Iteration 2: Extract Information for All Products on the Page

### 2.1 / Iterate Through All Products

1. Modify your script so that, instead of processing only the first product, it iterates over **all** products listed on the main page.
2. For each product:
   - Click on the product link to navigate to its detail page.
   - Extract the desired information (e.g., product name and price).
   - Return to the main page to continue processing the next product.
     - **Tip:** Consider using the browser's back functionality or opening each product in a new tab and closing it after extraction.

### 2.2 / Store and Present Data

1. Save the information extracted from each product in a suitable data structure (for example, a list of dictionaries).
2. Print the complete list of products with their details to the console.
3. Export the aggregated data to a CSV file named `products_detail.csv` with appropriate headers (such as `Name` and `Price`).

---

## BONUS - Error Handling and Optimization

- Implement error handling using try/except/finally blocks to manage potential issues (e.g., missing elements).
- Add logging messages to help track the progress and identify issues in your script.
- *(Optional)* Enhance the challenge by using the **Pandas** library to:
  - Read the generated CSV file.
  - Display a summary (for example, count the total number of products or filter based on specific conditions).
  - Save any updated or analyzed data to a new CSV file.

---

## Submission

Once you have completed the lab, follow these steps to submit your work:

1. Add your changes using Git.
2. Commit your changes with a meaningful commit message (e.g., "Lab completed: Detailed Product Information Extraction (first product then all products)").
3. Push your changes to the main branch.
4. Create a Pull Request to merge your changes.

---

This lab will help you deepen your understanding of Selenium and BeautifulSoup by dynamically navigating web pages and extracting detailed product information. Enjoy the challenge and happy coding!
