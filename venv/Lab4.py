
from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe')
import unittest
import time

# driver.get('http://127.0.0.1:3000/')

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.delayTime=1
        self.driver = webdriver.Chrome('chromedriver.exe')
        # self.driver = webdriver.Chrome('/Users/awen/Desktop/ST-Lab4/chromedriver')
        # self.driver.fullscreen_window()
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/div[2]/a').click()
        self.driver.find_element_by_name('email').send_keys('demo@keystonejs.com')
        self.driver.find_element_by_name('password').send_keys('demo')
        self.driver.find_element_by_class_name('css-2960tt').click()
        time.sleep(1)


    def tearDown(self):
        print("tearDown")
        time.sleep(2)
        self.driver.close()

    def test_CreatPost(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div[2]/div/div[1]/div[2]/div[1]/span/a[2]').click()
        # time.sleep(self.delay)
        # self.driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_name('name').send_keys('test1 post')
        time.sleep(self.delayTime)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/form/div[3]/button[1]').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-2960tt').click()


    def test_EditPpst(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div[2]/div/div[1]/div[2]/div[1]/span/a[1]').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_name('name').clear()
        time.sleep(self.delayTime)
        self.driver.find_element_by_name('name').send_keys('test2 post')
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-2960tt').click()

    def test_DeletePost(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div[2]/div/div[1]/div[2]/div[1]/span/a[1]').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-1mj7u0z').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-t4884').click()

if __name__ == '__main__':
    unittest.main()






