from calendar import month_name
import scrapy
from dynamic.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from dynamic.items import DynamicItem
import datetime


class EkSpider(scrapy.Spider):
    name = "ek"
    start_urls = [
        f'https://ek.ua/ua/list/186/{page}'
        for page in range(7)]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=30,
                wait_until=expected_conditions.element_to_be_clickable(
                    (By.XPATH,
                     '//td[@class="model-shop-name"]')
                ),
            )

    def parse(self, response):
        for card in response.css('.list-item--goods'):
            try:
                name = card.xpath('.//span[@class="u"]/text()').get()
                for row in card.xpath('.//table[@class="model-hot-prices"]//tr'):
                    shop = row.xpath(
                        './/td[@class="model-shop-name"]//u/text()').get()
                    city = row.xpath(
                        './/span[@class="model-shop-city"]//text()').get()
                    price = row.xpath(
                        './/td[@class="model-shop-price"]//a/text()').get()
                    price = int (price.replace("\xa0", "").replace("грн.",""))
                    yield DynamicItem(
                        name=name,
                        shop=shop,
                        city=city[3:-1],
                        price=price
                    )
            except Error as e:
                print(e)
