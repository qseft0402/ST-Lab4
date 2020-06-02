
from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe')
import unittest
import time

# driver.get('http://127.0.0.1:3000/')

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver = webdriver.Chrome('/Users/awen/Desktop/ST-Lab4/chromedriver')
        self.driver.fullscreen_window()
        # self.driver.get('http://127.0.0.1:3000/')
        self.driver.get('http://140.124.181.47:3000/')
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/div[2]/a').click()
        self.driver.find_element_by_name('email').send_keys('demo@keystonejs.com')
        self.driver.find_element_by_name('password').send_keys('demo')
        self.driver.find_element_by_class_name('css-2960tt').click()
        # time.sleep(1)
    def tearDown(self):
        self.driver.close()

    def test_CreatPost(self):
        time.sleep(60)
if __name__ == '__main__':
    unittest.main()






