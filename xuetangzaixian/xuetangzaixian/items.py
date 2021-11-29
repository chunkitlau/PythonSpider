# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    courseName = scrapy.Field()
    teacher = scrapy.Field()
    affiliatedSchool = scrapy.Field()
    numberOfCoursesEnrolled = scrapy.Field()
    information = scrapy.Field()
    pass
