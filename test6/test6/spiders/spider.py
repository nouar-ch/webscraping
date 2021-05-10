import scrapy
from test6.items import Product
from selenium import webdriver
import time
import csv

class MySpider(scrapy.Spider):
    name = "test6"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas",
            callback=self.parse
        )
    
    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(10)
        print("getting elements")
        breadcrumbs = self.driver.find_elements_by_css_selector("li.breadcrumbs-link")
        breadcrumbs_titles = list(bc.text for bc in breadcrumbs)

        products_names = list(
            Product({"name": p.text})
            for p in self.driver.find_elements_by_css_selector("div.product-grid a.shelfProductTile-descriptionLink")
        )

        print(breadcrumbs_titles)
        print(products_names)

        with open("products.csv", "w") as fd:
            writer = csv.DictWriter(fd, fieldnames=["name"])
            writer.writerows(products_names)

