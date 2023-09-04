import scrapy


class Bet365Spider(scrapy.Spider):
    name = "Bet365"
    start_urls = ["https://www.bet365.com/#/AC/B1/C1/D1002/E88369731/G40/"]

    def parse(self, response):
        pass
