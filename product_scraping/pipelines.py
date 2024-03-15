# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ProductPipeline:
    def process_item(self, item, spider):
        if item['name'] and item['name'].strip() != '':
          for field, value in item._values.items():
              item[field] = value.strip()
          item['price'] = float(item['price'])
          item['item_id'] = int(item['item_id'])
          return item    
        raise DropItem('Missing name')
