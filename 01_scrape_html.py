# Import packages
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Url a scrapear
url = 'https://houm.com/co/arriendo-apartamentos-bogota'

# Abro el webdriver que me deja controlar chrome desde python
driver = webdriver.Chrome()

# Abro la pagina
def get_aptos(page):
    try:
        url_with_page = url + f"?page={page}"
        driver.get(url_with_page)
        
        # Sleep to allow the page to load fully
        time.sleep(3)
        
        aptos = driver.find_elements(By.XPATH, '//a[contains(@href, "/co/arriendo-departamento-bogota/")]')
        
        apartment_links = [elem.get_attribute('href') for elem in aptos if elem.get_attribute('href')]
        
        for link in apartment_links:
            print(link)

        # Me quedo con los validos
        print(f"Found {len(apartment_links)} valid apartment links.")
        
        # hay duplicados entonces me quedo con los unicos. 
        unique_links = []
        [unique_links.append(x) for x in apartment_links if x not in unique_links]
        
        n = len(unique_links)
        
        # Creo el diccionario
        dict = {"links": unique_links, "page": [page] * n}
        
        # Sleep to avoid overloading the server with requests
        time.sleep(2)
        
        return dict
    except Exception as e:
        print(f"An error occurred on page {page}: {e}")
        return None

apartments = []
for i in range(1, 13):
    dict = get_aptos(i)
    if dict is not None:
        apartments.append(dict)
