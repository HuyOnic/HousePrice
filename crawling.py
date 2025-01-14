from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pandas import DataFrame
import time
import random


class DataScraping():
    def __init__(self, path, num_page=290):
        self.path = path
        self.num_page = num_page
        self.prices = []
        self.acreages = []
        self.locations = []
        self.links = []
        self.title = []
        self.time_uploads = []
        self.post_authors = []

    def Crawling(self):
        driver = webdriver.Chrome()
        driver.get(path)
        cur_page = 1
        while cur_page <= self.num_page:
            try:
                print(f'Page number {cur_page} Starting Craw Data ...')
                # Get title and link
                title_elems = driver.find_elements(
                    By.CSS_SELECTOR, ('h3.post-title'))
                for title_elem in title_elems:
                    title_child = title_elem.find_element(By.TAG_NAME, ('a'))
                    self.title.append(title_child.text)
                    self.links.append(title_child.get_attribute('href'))
                # Get price attribute
                price_elems = driver.find_elements(
                    By.CSS_SELECTOR, ('span.post-price'))
                for price_elem in price_elems[:20]:
                    self.prices.append(price_elem.text)
                # Get acreages attribute
                acreage_elems = driver.find_elements(
                    By.CSS_SELECTOR, 'span.post-acreage')
                for acreage_elem in acreage_elems:
                    self.acreages.append(acreage_elem.text)
                # Get location
                locations = driver.find_elements(
                    By.CSS_SELECTOR, 'span.post-location')
                for location in locations:
                    local = location.find_element(
                        By.TAG_NAME, 'a')
                    self.locations.append(local.text)

                # Get time uploads
                time_elems = driver.find_elements(By.CLASS_NAME, ('post-time'))
                for time_elem in time_elems[:20]:
                    self.time_uploads.append(time_elem.get_attribute('title'))
                # Get Post Author
                author_name_elems = driver.find_elements(
                    By.CSS_SELECTOR, ('span.author-name'))
                for author_name_elem in author_name_elems:
                    self.post_authors.append(author_name_elem.text)

                # Another service
                print(f'Page number {cur_page} Craw Data Successfully !')
                cur_page += 1
                time.sleep(1)
                # Move to next page
                next_pages = driver.find_elements(
                    By.CSS_SELECTOR, ('a.page-link'))
                for next_page in next_pages:
                    if next_page.text == 'Trang sau »':
                        next_link = next_page.get_attribute('href')

                driver.get(next_link)
                time.sleep(random.randint(2, 3))
            except:
                print(f'Page number {cur_page} have error, cancel craw!')
        driver.quit()

    def ExportToCSV(self):

        df = DataFrame({
            'Mô tả': self.title,
            'Diện tích': self.acreages,
            'Vị trí': self.locations,
            'Ngày đăng': self.time_uploads,
            'Người đăng': self.post_authors,
            'Đường link': self.links,
            'Gía phòng': self.prices
        })
        df.to_csv('houseprice_dataset.csv', index=False)
        print('Export to csv Successfully!')

    def RunTool(self):
        self.Crawling()
        self.ExportToCSV()

    def __str__(self):
        return f'{self.prices}\n{self.acreages}\n{self.locations}\n{self.links}\n{self.post_authors}\n{self.time_uploads}\n{self.title}'

if __name__ == '__main__':
    path = 'https://phongtro123.com/tinh-thanh/ha-noi'
    Obj = DataScraping(path)
    Obj.RunTool()
