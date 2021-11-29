# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class MyPipeline:
    def process_item(self, item, spider):
        return item
    
    def open_spider(self, spider):
        try: # 打开 json 文件
            self.file = open('MyData.json', "w", encoding="utf-8")
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        dict_item = dict(item) # 生成字典对象
        json_str = json.dumps(dict_item, ensure_ascii=False) + "\n" # 生成 json 串
        self.file.write(json_str) # 将 json 串写入到文件中
        return item

    def close_spider(self, spider):
        self.file.close() # 关闭文件
