#https://dev-gang.ru/article/kak-ispolzovat-python-i-xpath-dlja-czistki-saitov-ht13ju9mu8/
# getting the data
import requests
from urllib.request import urlopen
from lxml import etree
import csv
# get html from site and write to local file

city_code='2398'

cookies = {
    'mg_geo_id': f'{city_code}'
}
    


url = 'https://magnit.ru/promo/'
headers = {'Content-Type': 'text/html',}
response = requests.get(url, headers=headers, cookies=cookies)
html = response.text
with open ('star_wars.html', 'w', encoding="utf_8_sig") as f:
     f.write(html)

# read local html file and set up lxml html parser
local = 'file:///C:/Users/dfg/Desktop/magn/star_wars.html'
response = urlopen(local)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)

city = tree.xpath('//span[@class="header__contacts-text"]/text()')[0]

data = []
card_title = tree.xpath('//div[@class="card-sale__title"]/p/text()')
card_discount = tree.xpath('//div[@class="label label_sm label_magnit card-sale__discount"]/text()')



card_price_old_integer = tree.xpath('//div[@class="label__price label__price_old"]/span[@class="label__price-integer"]/text()')
card_price_old_decimal = tree.xpath('//div[@class="label__price label__price_old"]/span[@class="label__price-decimal"]/text()')
card_old_price = f'{card_price_old_integer}.{card_price_old_decimal}'


        
card_price_new_integer = tree.xpath('//div[@class="label__price label__price_new"]/span[@class="label__price-integer"]/text()')
card_price_new_decimal = tree.xpath('//div[@class="label__price label__price_new"]/span[@class="label__price-decimal"]/text()')
card_price = f'{card_price_old_integer}.{card_price_old_decimal}'

data.append(
     [card_title, card_discount, card_old_price, card_price]
)

    
with open(f'{city}.csv', 'w', encoding="utf_8_sig") as file:
     writer = csv.writer(file)
        
     writer.writerow(
         [
            'Продукт',
            'Старая цена',
            'Новая цена',
            'Процент скидки',            
         ]
     )
     writer.writerows(
        data
    )
            
print(f'Файл {city}.csv успешно записан!')

