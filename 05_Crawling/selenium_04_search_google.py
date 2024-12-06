from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com/search?q="+'Python') # +'검색어'

driver.implicitly_wait(3)

search_results=driver.find_elements(By.CSS_SELECTOR,"div.yuRUbf") 
print(len(search_results))


# Extract and print the title and URL of each search result
for result in search_results:
    title_element =	result.find_element(By.CSS_SELECTOR, "h3")
    title = title_element.text.strip()
    print(f'{title}')

driver.quit()