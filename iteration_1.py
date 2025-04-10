from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# este codigo comentado es para usarlo para Firefox
"""# Set up the Librewolf driver (using Firefox webdriver)
options = webdriver.FirefoxOptions()
# Headless mode , because it's faster
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)"""

options = webdriver.ChromeOptions()
options.add_argument('--headless')  
driver = webdriver.Chrome(options=options)

try:
    # navega a la pagina principal con los listados de productos
    main_page_url = "https://guanxe.com/es/3628-portatiles?p=1"
    driver.get(main_page_url)
    print("Loaded main page")

    # espera hasta que haya un elemento con el nombre del producto
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.product-name"))
    )
    print("Product links found")

    #coge los enlaces de los productos
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # los metemos en una lista
    product_links = soup.select("a.product-name")

    # cogemos el url del primer producto
    first_product_url = product_links[0]['href']
    print(f"URL: {first_product_url}")

    # navega a la pagina del primer producto
    driver.get(first_product_url)
    print("Navigated to product page")

    # espera a que la pagina cargue completamente
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span#our_price_display_right"))
    )
    print("Product page loaded")

    # extrae el nombre del producto
    product_name_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#derecha1 h1")))

        
    product_name = product_name_element.text.strip()
    
    # extrae el precio del producto
    
    product_price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span#our_price_display_right"))
        )
    product_price = product_price_element.text.strip()
    
    

    # extrae la descripcion del producto
   
    product_description_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#short_description_content"))
        )
    product_description = product_description_element.text.strip()
    

    # imprimir los datos del producto
    print("\nExtracted Product Information:")
    print("Product Name:", product_name)
    print("Product Price:", product_price)
    print("Product Description:", product_description)

except Exception as e:
    print("An error occurred:", e)
finally:
    print("Closing browser")
    time.sleep(2)
    driver.quit()
