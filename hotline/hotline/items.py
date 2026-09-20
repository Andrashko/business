# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass, field


@dataclass
class HotlineItem:
    name: str = ""
    price: float | str = 0.0
    url: str = ""

    image_urls: list[str] = field(default_factory=list)
    file_urls: list[str] = field(default_factory=list)
