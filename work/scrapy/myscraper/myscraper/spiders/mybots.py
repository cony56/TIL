import scrapy
from myscraper.items import MyscraperItem
import sys
from scrapy.http import Request

URL = 'http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=258/&page=%s'
start_page = 1
# print(URL % start_page)
# print(URL.format(start_page))
class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']

    start_urls = [URL % start_page]


    def start_requests(self):
        for i in range(2):
            #request에 대한 생성자를 반환시킴
            # request를 실행한 다음에 parse함수를 실행시키게 연동시키는게 callback의 기능임
            yield Request(url=URL %(i + start_page),callback=self.parse)

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').extract()
        writers = response.css('.writing::text').extract()
        previews = response.css('.lede::text').extract()

        items = []
        # items에 대해 XPATH, CSS를 통해 추출한 데이터를 저장
        
        for idx in range(len(titles)):
            item = MyscraperItem()
            item['title'] = titles[idx]
            item['writer'] = writers[idx]
            item['preview'] = previews[idx]

            items.append(item)

        return items
            
        
