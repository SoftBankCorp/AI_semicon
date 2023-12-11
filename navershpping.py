from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
url = "https://shopping.naver.com/logistics/home"

item_selector = "#content > div > div.homePageResponsive_best_wrap__3KGye > div > div > ul > li > div > div:nth-child(2) > strong"
price_selector = "#content > div > div.homePageResponsive_best_wrap__3KGye > div > div > ul > li  > div > div.productCardResponsive_information__1HK4_ > div.productCardResponsive_price_area__3lo44 > span"

driver.get(url)

items = driver.find_elements(By.CSS_SELECTOR, item_selector)
prices = driver.find_elements(By.CSS_SELECTOR, price_selector)

print("가져온 상품 수: ", len(items))
for item, price in zip(items, prices):
    print("상품: ", item.text)
    print("가격: ", price.text)
    print()