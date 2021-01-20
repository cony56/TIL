import scrapy
from movie.items import MovieItem


# descs -> 40데이터 (공백포함) -> 10데이터 (공백제거)

def remove_space(descs:list) -> list:
    result = []
    # 공백 제거
    for i in range(len(descs)):
        if len(descs[i].strip()) > 0:
            result.append(descs[i].strip())
    return result

class MoviebotSpider(scrapy.Spider):
    name = 'moviebot'
    allowed_domains = ['naver.com']
    #/를 넣으면 디렉토리가 됨
    start_urls = ['http://movie.naver.com/movie/point/af/list.nhn']

    def parse(self, response):
        titles = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        stars = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/div/em/text()').extract()
        dates = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[3]/text()').extract()
        writers = response.css('.author::text').extract()
        descs = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/text()').extract()
        converted_descs = remove_space(descs)

        for row in zip(titles, stars, converted_descs, writers,dates):
            item = MovieItem()
            item['title'] = row[0]
            item['star'] = row[1]
            item['desc'] = row[2]
            item['writer'] = row[3]
            item['date'] = row[4]

            yield item