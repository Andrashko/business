from calendar import month_name
import scrapy
from dynamic.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from dynamic.items import DynamicItem
import datetime


class OlxSpider(scrapy.Spider):
    name = "olx"

    async def start(self):

        for url in  [f'https://www.olx.ua/uk/transport/legkovye-avtomobili/q-Audi/?currency=UAH&page={
                    page}'
                for page in range(1, 2)]:

            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=5,
                wait_until=expected_conditions.element_to_be_clickable(
                    (By.XPATH,
                     '//a//img')
                ),
            )
    month_names = {
        "квітня": 4,
        "травня": 5
    }

    def parse(self, response):
        for auto in response.xpath('//div[@data-cy="l-card"]'):
            try:
                price = int("".join(auto.xpath(
                    './/p[@data-testid="ad-price"]/text()').get().split()[0:-1]))
                text = auto.xpath('.//h6/text()').get()
                location, _, date = auto.xpath(
                    './/p[@data-testid="location-date"]/text()').getall()
                location = location.split(",")[0]
                if "Сьогодні" in date:
                    date = datetime.date.today()
                else:
                    day, month, year, _ = date.split()
                    date = datetime.date(
                        int(year), self.month_names.get(month), int(day))

                history = auto.xpath('.//span/svg/path[@d="M12 3.5c5.514 0 10 4.487 10 10.002 0 2.181-.272 4.684-2.293 6.705L19 20.5H5l-.708-.294C2.272 18.178 2 15.679 2 13.501 2.001 7.987 6.487 3.5 12 3.5zm0 2c-4.41 0-8 3.59-8 8.001 0 2.341.42 3.827 1.435 4.999h13.131C19.58 17.332 20 15.847 20 13.502 20 9.09 16.411 5.5 12 5.5zm5 3v1.414l-1.27 1.271-1.026 1.025c.188.392.296.829.296 1.292 0 1.654-1.345 3-3 3-1.654 0-3-1.346-3-3 0-1.655 1.346-3 3-3 .462 0 .898.108 1.29.295l1.025-1.026 1.27-1.271H17zm-5 4.002a1.001 1.001 0 0 0 0 2 1.001 1.001 0 0 0 0-2z"]/../../text()').get().split()
                year = int(history[0])
                print(history)
                if history[-1] == "тис.км.":
                    run = int("".join(history[1:-1])) * 1000

                yield DynamicItem(
                    price=price,
                    text=text,
                    location=location,
                    date=date,
                    year=year,
                    run=run
                )
            except Error as e:
                print(e)
