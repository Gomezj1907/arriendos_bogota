
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://houm.com/co/arriendo-apartamentos-bogota'


driver = webdriver.Chrome()

driver.get(url)
# Parse html

aptos = driver.find_elements(By.XPATH, '//a[contains(@href, "/co/arriendo-departamento-bogota/")]')

apartment_links = [elem.get_attribute('href') for elem in aptos if elem.get_attribute('href')]

for link in apartment_links:
    print(link)

# Print the count of valid links
print(f"Found {len(apartment_links)} valid apartment links.")

unique_links = []
[unique_links.append(x) for x in apartment_links if x not in unique_links]