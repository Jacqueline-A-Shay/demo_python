# setup
# pip install webdriver-manager


from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


>>> opt = Options()
>>> opt.headless=True
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://duckduckgo.com')

sf = driver.find_element_by_id('search_form_input_homepage')
sf.send_keys('real python')
sf.submit()
results = driver.find_elements_by_class_name('result')
print(results[0].text)

driver.get('https://bandcamp.com')
driver.find_element_by_class_name("play-btn").click()
driver.find_element_by_class_name("carousel-bcweekly-play-button").click()


# to end the work
driver.close()
# exit python session
quit()