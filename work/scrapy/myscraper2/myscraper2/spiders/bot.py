import scrapy


class BotSpider(scrapy.Spider):
    name = 'bot'
    allowed_domains = ['https://movie.naver.com/movie/point/af/list.nhn']
    start_urls = ['http://https://movie.naver.com/movie/point/af/list.nhn/']

    def parse(self, response):
        pass
