import scrapy
import json
import copy
from xuetangzaixian.items import MyItem # 从 items.py 中引入 MyItem 对象

class mySpider(scrapy.spiders.Spider):
    name = "xuetangzaixian" # 爬虫的名字是 xuetangzaixian
    allowed_domains = ["www.xuetangx.com/"] # 允许爬取的网站域名
    url = "https://www.xuetangx.com/api/v1/lms/get_product_list/?page={}" # URL ，即爬虫爬取的URL
    data = '{"query":"","chief_org":[],"classify":["1"],"selling_type":[],"status":[],"appid":10000}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh',
        'Content-Type': 'application/json',
        'app-name': 'xtzx',
        'terminal-type': 'web',
        'django-language': 'zh',
        'xtbz': 'xt',
        'x-client': 'web',
        'Origin': 'https://www.xuetangx.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.xuetangx.com/search?query=&org=&classify=1&type=&status=&page={}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Cache-Control': 'max-age=0',
        'TE': 'trailers',
    }
    cookies = {
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217d5797683b77e-0c88409d528625-326f464a-1049088-17d5797683c6ba%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217d5797683b77e-0c88409d528625-326f464a-1049088-17d5797683c6ba%22%7D',
        '_ga': 'GA1.2.1549222731.1637852081',
        '_gid': 'GA1.2.863783125.1637997808',
        'provider': 'xuetang',
        'django_language': 'zh',
        'JG_016f5b1907c3bc045f8f48de1_PV': '1638069168637|1638072842031',
    }

    def start_requests(self):
        for i in range(1, 53):
            headers = copy.deepcopy(self.headers)
            headers['Referer'] = headers['Referer'].format(i)
            yield scrapy.Request(self.url.format(i),
                                 method='POST',
                                 headers=headers,
                                 body=self.data,
                                 cookies=self.cookies,
                                 callback=self.parse)

    def parse(self, response):
        msg= json.loads(response.body)
        for each in msg['data']['product_list']:
            item = MyItem()
            item['courseName'] = each['name']
            item['affiliatedSchool'] = each['org']['name']
            item['numberOfCoursesEnrolled'] = each['count']
            item['information'] = each['short_intro'].replace('\n', ' ').replace('\r', '')
            teacherList = []
            for teacher in each['teacher']:
                teacherList.append(teacher['name'])
                item['teacher'] = ','.join(teacherList)
            yield item