import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from data import maskpass
from selenium.webdriver.common.action_chains import ActionChains
import data
from Elements import elts
from selenium.webdriver.support import expected_conditions


class Pytest(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)



    def e_test_login(self):
        driver = self.driver
        driver.get(data.url)
        time.sleep(2)
        elt=elts["signinbtn"]
        driver.find_element(elt["prop"],elt["value"]).click()
        links_1 = driver.find_elements(By.TAG_NAME,"a")
        all_links=[x.get_attribute('href') for x in links_1]
        for link1 in all_links:
            print(link1)
            url=link1
            if url.startswith("http"):
                driver.get(url)
                print(driver.title)
                assert (len(driver.title)>0)
            else:
                print("not a link")

        driver.get(data.url)
        time.sleep(2)
        elt = elts["signinbtn"]
        driver.find_element(elt["prop"], elt["value"]).click()

        elt=elts["email"]
        driver.find_element(elt["prop"],elt["value"]).send_keys(data.email)
        elt = elts["continuebtn"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["password"]
        driver.find_element(elt["prop"], elt["value"]).send_keys(data.pwd)
        elt = elts["signinsubmitbtn"]
        driver.find_element(elt["prop"], elt["value"]).click()
        time.sleep(5)


        a = ActionChains(driver)
        elt=elts["NavLink"]
        m = driver.find_element(elt["prop"], elt["value"])
        a.move_to_element(m).perform()
        elt = elts["signout"]
        driver.find_element(elt["prop"], elt["value"]).click()
    def test_Cart(self):
        driver = self.driver
        driver.get(data.url)
        time.sleep(2)
        elt=elts["signinbtn"]
        driver.find_element(elt["prop"],elt["value"]).click()
        elt=elts["email"]
        driver.find_element(elt["prop"],elt["value"]).send_keys(data.email)
        time.sleep(2)
        elt = elts["continuebtn"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["password"]
        time.sleep(2)
        driver.find_element(elt["prop"], elt["value"]).send_keys(data.pwd)
        elt = elts["signinsubmitbtn"]
        driver.find_element(elt["prop"], elt["value"]).click()
        time.sleep(2)
        elt = elts["searchbar"]
        driver.find_element(elt["prop"], elt["value"]).send_keys(data.searchdata1)
        elt = elts["searchbtn"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["product1"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["addtocart"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["searchbar"]
        driver.find_element(elt["prop"], elt["value"]).send_keys(data.searchdata2)
        elt = elts["searchbtn"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["product2"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["addtocart"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["cartNav"]
        driver.find_element(elt["prop"], elt["value"]).click()
        time.sleep(5)
        elt = elts["product1CartPage"]
        p1=driver.find_elements(elt["prop"], elt["value"])
        elt = elts["product2CartPage"]
        p2 = driver.find_elements(elt["prop"], elt["value"])
        isPresentproduct1 = len(p1) > 0
        isPresentproduct2 = len(p2) > 0
        assert isPresentproduct1
        assert isPresentproduct2

        elt = elts["delete1"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["delete2"]
        driver.find_element(elt["prop"], elt["value"]).click()

    def e_test_browse(self):
        driver = self.driver
        driver.get(data.url)
        time.sleep(2)
        elt = elts["signinbtn"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["email"]
        driver.find_element(elt["prop"], elt["value"]).send_keys(data.email)
        elt = elts["continuebtn"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["password"]
        driver.find_element(elt["prop"], elt["value"]).send_keys(data.pwd)
        elt = elts["signinsubmitbtn"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["menu"]
        driver.find_element(elt["prop"], elt["value"]).click()
        time.sleep(2)
        elt = elts["seeallbtn"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["mensfashion"]
        mens=driver.find_element(elt["prop"], elt["value"])
        driver.execute_script("arguments[0].scrollIntoView();", mens)
        time.sleep(2)
        mens.click()
        elt = elts["clothing"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["sortby"]
        driver.find_element(elt["prop"], elt["value"]).click()
        elt = elts["sortOpt1"]
        driver.find_element(elt["prop"], elt["value"]).click()
        time.sleep(2)
        elt = elts["filterOpOurBrand"]
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((elt["prop"], elt["value"])))
        driver.find_element(elt["prop"], elt["value"]).click()



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

