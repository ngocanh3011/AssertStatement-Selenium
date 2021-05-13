import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testTitle(self):
        chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver_path)
        driver.maximize_window()

        driver.get("http://practice.automationtesting.in/")
        title = driver.title
        # print(get_title)
        self.assertTrue(title == "Automation Practice Site")
if __name__ == "__main__":
    unittest.main()

# driver.close()