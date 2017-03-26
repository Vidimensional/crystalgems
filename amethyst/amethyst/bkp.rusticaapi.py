import scrapy
import datetime
import requests
import json

from amethyst.items import AmethystItem

class RusticaapiSpider(scrapy.Spider):
    name = "rusticaapi"
    allowed_domains = ["rusticaapi.com"]
    start_urls = [
            "http://www.rusticaapi.com/finques.php/finques/undefined/undefined/?tipus=undefined&poble=undefined&idioma=es&pagina=undefined"
    ]

    def parse(self, response):
         for productes in response.xpath('//div[contains(@class,"container producte-container ") or contains(@class ,"container producte-container odd")]'):
            item = AmethystItem()
            item['url']='http://www.rusticaapi.com/es/finca/'+productes.xpath('@item-data').extract_first()
            item['identificador']=productes.xpath('div/div[@class="productes-texte"]/h3/span/text()').extract_first()
            item['tipo']=productes.xpath('div/div[@class="productes-texte"]/div[1]/p[1]/text()').extract_first()
            item['poblacion']=productes.xpath('div/div[@class="productes-texte"]/div[1]/p[2]/text()').extract_first()
            item['superficie']=productes.xpath('div/div[@class="productes-texte"]/div[1]/p[3]/text()').extract_first()
            item['precio']=productes.xpath('div/div[@class="productes-texte"]/div[2]/p[1]/text()').extract_first()
            #http://www.rusticaapi.com/es/finca/salt-de-monral
            #item['url']=
            item['last_update']=datetime.datetime.now().strftime("%Y%m%d")
            item['web']="rusticaapi"
            item['compra']=True
            if item['poblacion'] is not None:
                item['maps']=requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=Barcelona&destinations='+item['poblacion']+'&language=es&key=%20AIzaSyCCknBknkbHncZNzCXRPwrRWwnShdSdDhw').json()
            yield item

