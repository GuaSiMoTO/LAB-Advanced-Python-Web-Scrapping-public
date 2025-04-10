
#### Iteration 2 #############

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Driver configuration 
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # si quieres que no se abra la ventana del navegador
driver = webdriver.Chrome(options=options)
products_data = []

try:
    # Step 1: navega a la pagina principal con los listados de productos
    main_page_url = "https://guanxe.com/es/3628-portatiles?p=1"
    driver.get(main_page_url)
    
    # espera a que hasta que haya un elemento con el nombre del producto
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.product-name"))
    )
    
    # Step 2: coge todos los enlaces de los productos
    product_elements = driver.find_elements(By.CSS_SELECTOR, "a.product-name")
    product_links = [element.get_attribute('href') for element in product_elements]
    
    # borramos los enlaces duplicados
    product_links = list(dict.fromkeys(product_links))
    
    # Iterate sobre los enlaces de los productos
    for link in product_links:
        driver.get(link)
        
        # espera a que la pagina cargue completamente

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#derecha1")))
        
        # Step 3: Extract product information
        # extrae el nombre del producto
        product_name = driver.find_element(By.CSS_SELECTOR, "#derecha1 h1").text
    
        product_price = driver.find_element(By.CSS_SELECTOR, "span#our_price_display").text
        
        
        # extrae la descripcion del producto
        
        product_description = driver.find_element(By.CSS_SELECTOR, "div#short_description_content").text
        
        
        # imprimir los datos del producto
        print("Product Name:", product_name)
        print("Product Price:", product_price)
        print("Product Description:", product_description)
        print("--------------------------------------------------")

        
        # creamos un diccionario con los datos del producto
        # y lo añadimos a la lista de productos
        product_info = {
            "name": product_name,
            "price": product_price,
            "description": product_description
        }
        products_data.append(product_info)
        
        print("Product added:", product_info)
        
    # guardamos los datos en un archivo JSON
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(products_data, file, ensure_ascii=False, indent=4)
    
    print("File 'products.json' successfully created.")
        
except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()
