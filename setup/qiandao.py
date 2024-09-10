import ddddocr
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.firefox.service import Service
from PIL import Image
from selenium.webdriver.common.by import By
ocr = ddddocr.DdddOcr()
Account=['zl1110','zl1111','zl1112','zl1113','zl1114','zl1115','zl1116','zl1117','zl1118','zl1119']
def captchs():
    captcha_image = driver.find_element(By.ID,'verifyCode')
    driver.switch_to.window(driver.window_handles[0])
    driver.set_window_size(929, 883)  # 设置窗口大小为929*883像素
    location = captcha_image.location
    size = captcha_image.size
    driver.save_screenshot('screenshot.png')
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = Image.open('screenshot.png')
    im = im.crop((left, top, right, bottom))
    im.save('captcha.png')
    # captcha = main()
    image = open("captcha.png", "rb").read()
    captcha = ocr.classification(image)
    print(captcha)
    time.sleep(5)
    captcha_input = driver.find_element(By.NAME,'captcha')
    captcha_input.clear()
    time.sleep(1)
    captcha_input.send_keys(captcha)
    receive()
def min(account):
    username_input = driver.find_element(By.NAME,'account')
    username_input.clear()
    time.sleep(1)
    username_input.send_keys(account)
    driver.find_element(By.ID,'getRoleList').click()
    time.sleep(5)
    usernames=driver.find_element(By.ID,'roles')
    # print(usernames.text)
    Select(usernames).select_by_index(1)
    time.sleep(5)
    captchs()
def receive():
    submit_button = driver.find_element(By.ID,'SubmitBtn')
    submit_button.click()
    time.sleep(5)
    captch = driver.find_element(By.CLASS_NAME,'modal-body').text
    if captch=='领取成功！':
        print(captch)
        button = driver.find_element(By.CLASS_NAME,'btn-primary')
        button.click()
    elif '领取次数已达上限' in captch:
            print(captch)
            button = driver.find_element(By.CLASS_NAME,'btn-primary')
            button.click()
    else:
        print(captch)
        button=driver.find_element(By.CLASS_NAME,'btn-primary')
        button.click()
        time.sleep(5)
        driver.find_element(By.ID,'verifyCode').click()
        time.sleep(3)
        captchs()


if __name__ == '__main__':
    service = Service(executable_path=r"D:\himalaya_album_detail_spider\geckodriver-v0.34.0-win64\geckodriver.exe")
    option = webdriver.FirefoxOptions()
    option.add_argument('--headless')
    driver = webdriver.Firefox(options=option,service=service)
    # driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('http://zssgs.yxgmaet.com/index/gift?p=qd')
    time.sleep(3)
    server_input = driver.find_element(By.NAME,'server')
    options_list = Select(server_input).options
    Select(server_input).select_by_value("230004")
    for account in Account:
        print(account)
        min(account)
