from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyautogui
import time
import os
import shutil


def del_file(path_data):
    for i in os.listdir(path_data) :# os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "\\" + i#当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:#os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)


def pass_VC(imgTmpPath, input, img, refresh):
    refresh.click()
    actions = ActionChains(browser)
    actions.context_click(img)
    actions.perform()
    pyautogui.press('v')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.typewrite(message=imgTmpPath)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

    # To-do：通过识图api识别验证码，如果不成功刷新后再识别


    del_file(imgTmpPath)

imgTmpPath = 'D:\OneDrive - emails.bjut.edu.cn\honorDesktop\WebCrawler\PatentAgencyHelper\img'

browser = webdriver.Chrome()
browser.get('http://dlgl.cnipa.gov.cn/txnqueryAgencyOrg.do')
browser.maximize_window()
browser.find_element_by_xpath("//*[text()='成立15年以上']").click()
browser.find_element_by_xpath("//*[text()='北京市']").click()

# 过验证码
input = browser.find_elements_by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[7]/span[2]/input")
refresh = browser.find_elements_by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[7]/span[2]/a")[0]
img = browser.find_elements_by_tag_name("img")[2]
pass_VC(imgTmpPath, input, img, refresh)
