# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class MyPipeline(object):
    labels = ['courseName', 'teacher', 'affiliatedSchool', 'numberOfCoursesEnrolled', 'information']

    def open_spider(self, spider):
        try: # 打开 json 文件
            self.file = open('MyData.csv', "w", encoding="utf-8", newline='')
            self.writer = csv.DictWriter(self.file, fieldnames=self.labels)
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        self.writer.writerow(item) # 将条目写入到文件中
        return item

    def close_spider(self, spider):
        self.file.close() # 关闭文件