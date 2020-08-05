from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyautogui
import time


def pass_VC(input, img, refresh):
    refresh.click()
    actions = ActionChains(browser)
    actions.context_click(img)
    actions.perform()
    pyautogui.press('v')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.typewrite(message='D:\OneDrive - emails.bjut.edu.cn\honorDesktop\WebCrawler\GovAgent\img')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('enter')


browser = webdriver.Chrome()
browser.get('http://dlgl.cnipa.gov.cn/txnqueryAgencyOrg.do')
browser.maximize_window()
browser.find_element_by_xpath("//*[text()='成立15年以上']").click()
browser.find_element_by_xpath("//*[text()='北京市']").click()

# 过验证码
input = browser.find_elements_by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[7]/span[2]/input")
print(input)
refresh = browser.find_elements_by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[7]/span[2]/a")[0]
img = browser.find_elements_by_tag_name("img")[2]
# print(img.get_attribute("src"))
pass_VC(input, img, refresh)
