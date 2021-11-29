import scrapy
from lianjia.items import MyItem # 从 items.py 中引入 MyItem 对象

class mySpider(scrapy.spiders.Spider):
    name = "lianjia" # 爬虫的名字是 lianjia
    allowed_domains = ["bj.lianjia.com/"] # 允许爬取的网站域名
    url_format = "https://bj.lianjia.com/ershoufang/{}/pg{}/" # URL 格式 ，即爬虫爬取的 URL 格式
    locations = ['dongcheng', 'xicheng', 'haidian', 'chaoyang'] # 四个城区
    start_urls = []
    for location in locations:
        for page in range(1, 6):
            start_urls.append(url_format.format(location, page))

    def parse(self, response):
        item = MyItem()
        for each in response.xpath("/html/body/div[4]/div[1]/ul/li"):
            item['location'] = response.url.split('/')[-3] # 楼盘区域
            item['name'] = each.xpath("div[1]/div[1]/a/text()").extract()[0] # 楼盘名称
            item['area'] = each.xpath("./div[1]/div[3]/div/text()").extract()[0].split(' | ')[1] # 面积，平米数
            item['totalPrice'] = str(each.xpath("div[1]/div[6]/div[1]/span/text()").extract()[0]) + '万' # 总价，单位：万
            item['unitPrice'] = each.xpath("div[1]/div[6]/div[2]/span/text()").extract()[0] # 单价
            yield(item)
        