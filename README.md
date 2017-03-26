# crystalgems
Cosis de 🐐

##RUN

#Para crear un nuevo spider:

scrapy genspider nombre nombre.com

#Para ejecutar cada uno de los spiders:

scrapy crawl rusticaapi -o items.json
scrapy crawl lantiga -o items.json

#Cuantas mas veces se ejecute mas items anade en items.json. Es necesario aun hacer algun metodo donde no incorpore items si estos ya existen.

##TODO

https://maps.googleapis.com/maps/api/distancematrix/json?origins=Barcelona&destinations=Ginestar&language=es&key=%20AIzaSyCCknBknkbHncZNzCXRPwrRWwnShdSdDhw



##DONE

#lantiga
#http://www.lantiga.biz/comprar.php

#rusticaapi
#http://www.rusticaapi.com/finques.php/finques/undefined/undefined/?tipus=undefined&poble=undefined&idioma=es&pagina=undefined

##COSAS A REVISAR

#Integracion server web con scrapy
#http://stackoverflow.com/questions/36384286/how-to-integrate-flask-scrapy
#http://stackoverflow.com/questions/21133976/flask-load-local-json
By Raúl & Vidi
