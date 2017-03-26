import scrapy
import datetime


from amethyst.items import AmethystItem

class LantigaSpider(scrapy.Spider):
    name = "lantiga"
    allowed_domains = ["lantiga.biz"]
    start_urls = [
            "http://www.lantiga.biz/comprar.php"
    ]

    def parse(self, response):
        #Pillamos todos los div de productos indiferentemente si termina en odd o no
        for productes in response.xpath('//tr'):
            item = AmethystItem()
            #xpath('td[1]/font/text()').extract()
            #item['identificador']=productes.xpath('h3/span/text()').extract()
            #item['tipo']=productes.xpath('div[1]/p[1]/text()').extract()
            #item['poblacion']=productes.xpath('div[1]/p[2]/text()').extract()
            #item['superficie']=productes.xpath('div[1]/p[3]/text()').extract()


            item['precio']=productes.xpath('td[2]/font/text()').extract()
            item['last_update']=datetime.datetime.now().strftime("%Y%m%d") 
            item['web']="lantiga"
            item['compra']=True
            yield item

