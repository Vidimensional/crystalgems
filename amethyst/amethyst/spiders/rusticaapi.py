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

        

        #Cargamos el items.json para poder comparar cambios
        with open('items.json') as data_file:    
            data = json.load(data_file)

        for productes in response.xpath('//div[contains(@class,"container producte-container ") or contains(@class ,"container producte-container odd")]'):
            item = AmethystItem()
            
            identificador = productes.xpath('div/div[@class="productes-texte"]/h3/span/text()').extract_first()
            precio = productes.xpath('div/div[@class="productes-texte"]/div[2]/p[1]/text()').extract_first()
            
            precio=int(filter(unicode.isdigit, precio))

            encontrado = False

            #Problema el json lo identifica como array de dicts, entonces dificulta comprobar si existe o no
            for d in data:
                if d["identificador"] == identificador:
                    encontrado = True
                    if d["precio"] != precio: #Si ha cambiado el precio
                        print "El precio cambia"
                        d["precio"]=precio    #Modifico con el nuevo precio
                        d["last_update"]=datetime.datetime.now().strftime("%Y%m%d") #Actualizo producto
                    
            
            if not encontrado:
                print "########## Item Nuevo ##########"
                item = AmethystItem()
                item['identificador']=identificador
                item['precio']=precio
                item['url']='http://www.rusticaapi.com/es/finca/'+productes.xpath('@item-data').extract_first()
                item['tipo']=productes.xpath('div/div[@class="productes-texte"]/div[1]/p[1]/text()').extract_first()
                item['poblacion']=productes.xpath('div/div[@class="productes-texte"]/div[1]/p[2]/text()').extract_first()
                item['superficie']=productes.xpath('div/div[@class="productes-texte"]/div[1]/p[3]/text()').extract_first()
                item['precio']=productes.xpath('div/div[@class="productes-texte"]/div[2]/p[1]/text()').extract_first()
                item['last_update']=datetime.datetime.now().strftime("%Y%m%d")
                item['web']="rusticaapi"
                item['compra']=True
                if item['poblacion'] is not None:
                    item['maps']=requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=Barcelona&destinations='+item['poblacion']+'&language=es&key=%20AIzaSyCCknBknkbHncZNzCXRPwrRWwnShdSdDhw').json()
                yield item
            else:
                with open('items.json', 'w') as data_file:
                    json.dump(data, data_file)

