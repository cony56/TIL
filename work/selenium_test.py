from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = "C:\\Users\\user\\Desktop\\자연어처리과정\\TIL\\work\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(path)
#driver.get("https://google.com")
#print(driver.title)
#search_box = driver.find_element_by_name("q")
#search_box.send_keys('cloud computing')
# enter key
#search_box.submit()

# 페이스북 로그인
# elem_email = driver.find_element_by_id('email')
# elem_email.send_keys(['[페이스북 아이디]'])
# elem_pass =driver.find_element_by_id('pass')
# elem_pass.send_keys(['[페이스북 비밀번호]'])
# elemm_pass.send_keys(Keys.RETURN)

# github 로그인

driver.get('https://github.com/login')
elem_email = driver.find_element_by_id('login_field')
elem_email.send_keys('cony56')
elem_pass =driver.find_element_by_id('password')
elem_pass.send_keys(['tae940902'])
elem_pass.send_keys(Keys.RETURN)

profile_a = driver.find_element_by_xpath('a태그로 되어있는 정보')
print("Profile A =>", profile_a.get_attribute('href'))