'''
@文件名    :   webkeys.py
@邮箱好    ：   helinfengxs@163.com
@Author   :    helinfeng
------------      -------    --------    -----------
创建时间    :  2021/3/14 21:24
'''
import datetime
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebKey:
    def __init__(self):
        '''
        构造函数
        '''
        self.driver = None
    def openBrowser(self, br='gc'):
        '''
        打开浏览器
        :param br: gc = 谷歌浏览器，ff = 火狐浏览器，ie = ie浏览器
        :return: None
        '''
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver = webdriver.Firefox()
        elif br == 'ie':
            self.driver = webdriver.Ie()
        else:
            print("暂时不支持其他浏览器")
        # 默认设置隐式等待10s
        self.driver.implicitly_wait(10)
    def openUrl(self,url=None):
        '''
        打开网页
        :param url:网页地址
        :return:None
        '''
        if url.startswith('https://') or url.startswith('http://'):
            self.driver.get(url)
        else:
            self.driver.get('http://'+url)
    def __find_element(self, locator=None):
        '''
        八种定位元素方式
        :param locator:xpath=//*[@id="username"]
        :return: 返回定位到的元素
        '''
        element = None
        self.ele = None
        if locator.startswith("xpath="):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, locator.split("xpath=")[1])))
        elif locator.startswith("name="):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, locator.split("name=")[1])))
        elif locator.startswith("id="):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, locator.split("id=")[1])))
        elif locator.startswith("tag_name="):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, locator.split("tag_name=")[1])))
        elif locator.startswith("link_text="):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, locator.split("link_text=")[1])))
        elif locator.startswith("partial_link_text="):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, locator.split("partial_link_text=")[1])))
        elif locator.startswith("css_selector="):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator.split("css_selector=")[1])))
        elif locator.startswith("class_name="):
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, locator.split("class_name=")[1])))
        else:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        self.ele = element
        return self.ele
    def click(self, locator=None):
        '''
        找到元素，并进行点击
        :param locator: 定位器，默认XPATH
        :return:None
        '''
        self.__find_element(locator).click()
    def sendKeys(self,locator=None,value=None):
        '''
        找到元素，并进行输入
        :param value:
        :return: None
        '''
        self.__find_element(locator).send_keys(str(value))
    def changeIframe(self,locator):
        '''
        切换iframe
        :param locator:定位器，默认XPATH
        :return: None
        '''
        ele = self.__find_element(locator)
        self.driver.switch_to.frame(ele)
    def closeBorwser(self):
        '''
        退出浏览器
        :return:None
        '''
        self.driver.quit()
    def sleep(self,t=1):
        '''
        强制等待
        :param t: 默认1秒
        :return: None
        '''
        time.sleep(t)


