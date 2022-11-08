from selenium import webdriver
import time

chrome_web_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_web_path)
driver.get("https://www.tinder.com")

time.sleep(1)
accept_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
accept_button.click()

login_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')

login_button.click()
time.sleep(1)

try:
    facebook_button = driver.find_element_by_xpath(
        '//*[@id="q-1604738990"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    time.sleep(1)
    facebook_button.click()


except Exception:

    more_options = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div[1]/div/div[3]/span/button')
    time.sleep(1)
    more_options.click()
    time.sleep(2)
    facebook_login_button = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    time.sleep(1)
    facebook_login_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
print(driver.title)

email_input = driver.find_element_by_xpath('//*[@id="email"]')
time.sleep(1)
email_input.click()
email_input.send_keys("gitesh16patidar@gmail.com")

password_input = driver.find_element_by_xpath('//*[@id="pass"]')
time.sleep(1)
password_input.send_keys("laddlaop")

time.sleep(1)
login_facebook_button = driver.find_element_by_name("login")
login_facebook_button.click()

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
allow_button = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div/div/div[3]/button[1]')

allow_button.click()

notification_button = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div/div/div[3]/button[2]')

notification_button.click()

time.sleep(8)
print("done")

dislike = driver.find_element_by_xpath('//*[@id="q-1826079426"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
i=1
while(i<=99):
     time.sleep(1)
     print(i)
     try:
        dislike.click()
        i = i+1
     except Exception:
        pop_up = driver.find_element_by_xpath('//*[@id="q-1604738990"]/div/div/div[2]/button[2]')
        pop_up.click()
        i = i+1