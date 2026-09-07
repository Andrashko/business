import scrapy
from bs4 import BeautifulSoup
from hotline.items import HotlineItem


LAST_PAGE = 1
class LaptopsSpider(scrapy.Spider):
    name = "laptops"
    allowed_domains = ["hotline.ua", "localhost"]
    start_urls = [
        f"https://hotline.ua/ua/computer/noutbuki-netbuki/?p={page}" for page in range(1, LAST_PAGE+1)]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        # знаходимо список товарів
        items = soup.find(
            name="div", class_="list-body__content").find_all(class_="list-item")
        # Для кожного товару
        for item in items:
            # Знаходимо назву
            name = item.find(name="a", class_="item-title").find(
                string=True, recursive=False).strip()
            # url
            url = item.find(name="a", class_="item-title").get("href")
            # та ціну
            price = item.find(class_="list-item__value-price").find(
                string=True, recursive=False)
            # url картинки
            image_url = item.find(name="img").get("src")
            # повертаємо результат
            yield HotlineItem(
                name=name,
                price=price,
                url=f"https://hotline.ua{url}",
                image_urls=[f"https://hotline.ua{image_url}"]
            )
