from calendar import month_name
import scrapy
from dynamic.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from dynamic.items import DynamicItem, TopicItem
import datetime
from selenium.webdriver.support import expected_conditions as EC



class UkrNetSpider(scrapy.Spider):
    name = "ukrnet"
    allowed_domains = ["ukr.net"]
    start_urls = ["https://www.ukr.net/"]
    # chrome_driver_path = '../chromedriver.exe'

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "section.feed__section")),
            )

    def parse(self, response):
        for topic in response.css('section.feed__section'):
            topic_name = topic.css('h2>a::text').get().strip()
            # print(topic_name)

            topic_link_end = topic.css('a::attr(href)').get()
            topic_url = response.urljoin(topic_link_end)
            # print(topic_url)
            yield TopicItem(
                topic=topic_name,
                topic_url=topic_url
            )
