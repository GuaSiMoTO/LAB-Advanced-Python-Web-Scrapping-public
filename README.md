# LAB-Advanced-Python-Web-Scrapping

## Introduction

> **Note:** This lab can be completed in pairs or individually.

In this lab, you will learn how to:
- Access a webpage using Selenium.
- Extract a list of products from the main page.
- Click on the **first product** to enter its detail page and extract specific information (e.g., the price).
- Later modify your script to extract the same detailed information for **all products** on the page without navigating to additional pages.

Let's get started! 🚀

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

# Iteration 2: Extract Information for All Products on the Page

## 2.1 Iterate Through All Products

1. **Iterate Over All Products:**  
   Modify your script so that, instead of processing only the first product, it iterates over **all** products listed on the main page.  
   > **Note:** In the provided solution, all product links are extracted (using the `href` attribute) and stored in a list, allowing direct navigation to each product detail page using `driver.get(link)`.

2. **For Each Product:**
   - Retrieve the product link (`href` attribute) and navigate to its detail page using `driver.get(link)`.
   - Wait until the main content of the detail page is loaded (e.g., a container that includes the product title).
   - Extract the required information, such as **product name**, **price**, and **description**.
     - If any of these details are missing, assign the value `"No available"`.
   - Print the extracted information for each product to the console.
   > **Tip:** To avoid "stale element" issues, first collect all product links and navigate directly using `driver.get()`, rather than clicking the product link and using the browser's back functionality.

## 2.2 Store and Present Data

1. **Store the Extracted Data:**  
   Save the extracted product information (name, price, and description) in an appropriate data structure, such as a list of dictionaries. Each dictionary represents a product.

2. **Console Output:**  
   Print the complete list of products with their details to the console to ensure the extraction was successful.

3. **Export the Data:**  
   Export the aggregated data to a file. In the provided solution, the data is saved in JSON format in a file named `products.json`.  
   > **Alternative:** You may also export the data to a CSV file (e.g., `products_detail.csv`) with appropriate headers such as `Name`, `Price`, and `Description`.


---

## BONUS: Extend the Scraper to Iterate Through Pages 1 to 10

Now that you have a working scraper for a single page, extend its functionality by iterating through multiple pages.

1. **Navigate Through Multiple Pages:**  
   - Modify your script to loop through pages 1 to 10.  

2. **Extract Data from Each Page:**  
   - Retrieve all product links on each page.  
   - Visit each product’s detail page, extract the required information, and return to the listing.  

3. **Aggregate and Store Data:**  
   - Combine product details from all pages into a single dataset.  
   - Save the extracted data in `products_detail_all_pages.csv` (or JSON if preferred).  

4. **Additional Challenges:**  
   - Implement error handling to manage potential issues.  
   - Add logging messages to track progress.  
   - *(Optional)* Explore optimization techniques to improve efficiency.  

## Submission

Upon completion, run the following commands:

```
$ git add .
$ git commit -m "done"
$ git push origin main
```

Then create a Pull Request!!
