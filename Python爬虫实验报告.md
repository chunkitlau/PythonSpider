<div class="cover" style="page-break-after:always;font-family:方正公文仿宋;width:100%;height:100%;border:none;margin: 0 auto;text-align:center;">
    </br></br></br>
    <div style="width:70%;margin: 0 auto;height:0;padding-bottom:10%;">
        </br>
        <img src="buptname.png" alt="校名" style="width:100%;"/>
    </div>
    </br></br></br></br>
    <span style="font-family:华文黑体Bold;text-align:center;font-size:25pt;margin: 10pt auto;line-height:30pt;">实验报告</span>
    </br></br>
    <div style="width:20%;margin: 0 auto;height:0;padding-bottom:30%;">
        <img src="buptseal.png" alt="校徽" style="width:100%;"/>
	</div>
    </br>
    <table style="border:none;text-align:center;width:80%;font-family:仿宋;font-size:24px; margin: 0 auto;">
    <tbody style="font-family:方正公文仿宋;font-size:20pt;">
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">题　　目</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> 数据获取实验报告</td>     </tr>
    </tbody>              
    </table>
	</br></br></br>
    <table style="border:none;text-align:center;width:72%;font-family:仿宋;font-size:14px; margin: 0 auto;">
    <tbody style="font-family:方正公文仿宋;font-size:12pt;">
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">课程名称</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> Python程序设计</td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">上课学期</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> 2021春</td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">授课教师</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">杨亚 </td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">姓　　名</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> </td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">学　　号</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋"> </td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:20%;text-align:right;">日　　期</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">2021年11月23日</td>     </tr>
    </tbody>              
    </table>
	</br></br></br></br></br>
</div>

<!-- 注释语句：导出PDF时会在这里分页 -->

# 目录

[TOC]

## 爬取学堂在线的计算机类课程页面内容

### 实验内容

　　爬取学堂在线的计算机类课程页面内容，目标网页：https://www.xuetangx.com/search?query=&org=&classify=1&type=&status=&page=1

​		要求将课程名称、老师、所属学校和选课人数信息，保存到一个 csv 文件中。

### 实验步骤

#### 配置环境

​		使用 conda 创建一个 Python 3.8 环境并激活该环境。

​		在终端输入```conda install -c conda-forge scrapy```安装 scrapy 库。

​		使用 cd 命令进入项目根目录，在终端输入```scrapy startproject xuetangzaixian```创建学堂在线爬虫项目。

#### 创建主运行文件

​		使用 Visual Studio Code 打开该项目，在该目录下创建一个 begin.py 文件（与 scrapy.cfg 在同一级目录下）内容如下：

```
from scrapy import cmdline
cmdline.execute("scrapy crawl xuetangzaixian".split())
# xuetangzaixian 为爬虫的名字，在 spider.py 中定义
```

#### 创建 Item 类

​		修改 items.py 文件：调用 scrapy.Field() 方法，从 scrapy 提取出 courseName、teacher、affiliatedSchool、numberOfCoursesEnrolled 和 information 五个参数作为 Item 类的成员变量。

```
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

```

#### 编写 Spider 爬虫类、请求和解析方法

​		新建一个 spider.py 文件（在 spider 目录下），设置允许的域名、url、data、headers 和 cookies。

```
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
```

​		在 spider.py 文件中的 calss mySpider 中，添加 start_requests 函数，使用 headers、data 和 cookies 生成 52 个对目标 url 的 POST 请求来抓取 52 个页面，并设置回调函数。

```
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
```

​		在 spider.py 文件中的 calss mySpider 中，添加 parse 函数，从响应中提取出课程列表，对列表的每个元素提取出课程的名字、学校、授课老师、选课人数和信息，将提取出的信息形成一个 Item 类返回。

```
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
```

#### 编写 Pipeline 类、数据保存方法

​		修改 pipelines.py，使用 UTF-8 格式以写模式打开 csv 文件并设置不换行，创建写字典类实例来将字典写到 csv 文件，处理数据时使用写字典类实例方法来将数据项写到文件中。

```
from itemadapter import ItemAdapter
import csv

class MyPipeline(object):
    labels = ['courseName', 'teacher', 'affiliatedSchool', 'numberOfCoursesEnrolled', 'information']

    def open_spider(self, spider):
        try: # 打开 csv 文件
            self.file = open('MyData.csv', "w", encoding="utf-8", newline='')
            self.writer = csv.DictWriter(self.file, fieldnames=self.labels)
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        self.writer.writerow(item) # 将条目写入到文件中
        return item

    def close_spider(self, spider):
        self.file.close() # 关闭文件
```

​		修改 setting.py，其他设置不变，使用 pipeline 并且不遵守机器人规则。

```
添加 ITEM_PIPELINES = {
    'xuetangzaixian.pipelines.MyPipeline': 300,
}
修改 ROBOTSTXT_OBEY = False
```

- 参数是分配给每个类的整型值，确定了它们运行的顺序，item 按数字从低到高的顺序，通过 pipeline。

- 通常将这些数字定义在 0 - 1000 范围内。

​		运行 begin.py

​		或者运行 spider.py ，并将其运行时的 Script path 配置项修改为 begin.py

### 获取的 CSV 文件：MyData.csv

​		获取到 519 条课程信息，其中前 50 条信息如下：

```
VC++面向对象与可视化程序设计（下）：MFC编程基础,黄维通,清华大学,69490,本部分课程是介绍基于MFC的面向对象程序设计，内容涉及MFC构架、一系列常用控件、资源、单文档、多文档、数据库编程、多媒体编程等内容。 
大学计算机基础,"徐红云,刘欣欣,曹晓叶",华南理工大学,52760,《大学计算机基础》是为非计算机专业学生开设的第一门计算机基础课。想一网打尽计算机的基础知识，培养计算思维能力，了解常用软件的用途及操作技巧，在互联网+时代成为精通计算机及相关技术的专业人才，那就快来学习这门课程吧！
软件工程,"刘强,刘璘",清华大学,103434,"用正确的方式建造有价值的软件，软件工程课程为您讲授软件系统的构建之道！ 本课程为国家级精品在线开放课程和国家级一流本科课程，并入围首批中国高校计算机教育慕课联盟—华为技术公司""智能基座""课程。"
计算机文化基础,"李秀,姚瑞霞,安颖莲,全成斌",清华大学,91338,面对无处不在的信息技术，你一定希望应用工具和技术解决常见的学习工作问题。甚至希望能够将信息技术应用到新的地方，那么，请加入课程学习！
Web前端攻城狮,"刘强,吴亮,赵文博",清华大学,64233,作为一名合格的前端攻城狮，要写得了样式磕得了脚本，玩得转ES6，架得起业务框架拎得起动画效果，撑得住浏览器抵得住服务端，这门课值得拥有！
大学计算机教程,"张莉,马钦",中国农业大学,63595,新时代、新技术、新发展，不能没有新知识新技能，在越来越多中小学生加入到学编程玩竞赛的今天，智者有志必先行。 本课程作为高校新生入学第一门计算机导论和公共基础核心课，跟随新时代新技术发展，不断建设不断提升，已成为深入系统自主创新学习、自我全面提升必修环节。本课程基于新版教材，是长期主持“大学计算机基础”教改立项建设积累的提升发展，校内外广泛应用至今，获奖多项。本课程是高校学科交叉融合人才培养必不可少核心课程，相关内容也是国内外高校重基础理论，强化计算思维综合能力系统提升的必备基础核心课程（core courses）。
JAVA程序设计进阶,许斌,清华大学,52680,本课程内容主要包括java线程、网络编程、java虚拟机、垃圾回收机制、java集合类详解、java反射与代理以及java的字节码技术。
大学计算机——计算思维的视角,郝兴伟,山东大学,52341,全面培养学生的计算科学修养，信息素养，培养学生良好的计算思维能力，提高学生的计算机应用水平和计算机问题求解能力。
软件理论基础,罗贵明,清华大学,21030,本课程介绍形式语言、自动机、文法、可判定性问题及计算复杂性。
C++语言程序设计基础,"郑莉,李超,徐明星",清华大学,466889,C++是从C语言发展演变而来的一种面向对象的程序设计语言，本课程是一门面向广大初学者的入门课程。
数据结构(上),邓俊辉,清华大学,456221,本课程旨在围绕各类数据结构的设计与实现，揭示其中的规律原理与方法技巧；同时针对算法设计及其性能分析，使学生了解并掌握主要的套路与手段。
程序设计基础,"徐明星,王瑀屏,邬晓钧",清华大学,89903,如何从生活中提炼算法，使计算机能象人一样解决问题？如何运用计算思维，用计算机来提高人的能力？我们将为你呈现一个既熟悉又陌生的精彩世界，带你感悟不一样的计算人生。
人工智能原理,王文敏,北京大学,79361,"本课程在系统回顾人工智能发展史的基础上，重点介绍人工智能的核心思想、基本理论，基本方法与部分应用。 课程以英文原版教材为主，并根据人工智能、特别是机器学习领域的发展和变化，编撰和充实了大量内容。采用中英文PPT,中文讲授。"
组合数学,马昱春,清华大学,78961,"本课程是计算机专业核心的基础理论课，是计算机理论分析和算法设计的基础,侧重介绍组合数学的概念和思想，研究离散对象的计数方法和相关理论。"
C语言程序设计,"丁海燕,武浩",云南大学,26910,程序设计是信息类和其他理工科一门重要的基础性课程。《C语言程序设计》面向低年级学生，内容包括：C语言概述、数据类型、运算符、表达式、结构化程序设计的三种基本结构、数组、函数、指针、结构体等。通过课程内容的讲解和编程训练，使学生具备用C语言开发应用软件的基本能力，为今后的软件开发工作奠定坚实的基础
互联网大规模数据分析技术,"李琳,张蕊",武汉理工大学,26348,如今我们处于大数据的时代，互联网大规模数据分析这门课程带大家进入分析和处理大数据的世界。海纳百川，有容乃大，让我们以开放的心态，创新的勇气拥抱大数据。
C君带你玩编程,"方娇莉,潘晟旻,普运伟,耿植林,郭玲,田春瑾,刘领兵,黎志,杜文方,郑明雄",昆明理工大学,26239,C君牵你的手，采撷精彩代码，谱写人类独有的智慧之诗。我们将亲手为冰冷的机器注入灵魂、打开CPU的世界、探索1和0构建的神奇二次元。结合专业知识、驱动硬件、兼顾NCRE证书的获取……快来快来，和C君一起玩编程吧！
物联网概论,何源,清华大学,32493,在万物互联的时代即将到来之时，让我们一起通过这门课程，认识物联网的基本概念，掌握物联网的关键技术，了解物联网的前沿动态，领略物联网的应用发展。
网络安全概述,纪平,学堂在线,32457,本课程主要在六个方面进行介绍：计算机网络基础知识－简短回顾；网络安全研究的是什么问题；编码解码学；网络安全协议；无线网络安全；防火墙及攻防系统。 
大数据治理与政策,"孟庆国,张楠,郑磊",清华大学,32138,通过对本课程的学习，让学生从治理和政策的角度，对大数据在公共管理领域中的应用及其应用中可能引发的问题有更深入认识和系统的理解。
计算机应用基础,"宋承继,王坤,李龙龙,李莹,陈小健,白雨鑫,毛小乐,梁菲菲,党佳奇",陕西工业职业技术学院,62522,        《计算机应用基础》课程将以计算机应用技能培养为导向，以计算机原理、概念为基础，以新技术新方法为牵引，以信息化办公和计算机维护为突破口，以创新思维能力培养为目标，和学习者一起了解计算机的发展史及软硬件结构，掌握计算机操作系统及各种办公软件的使用技巧，熟悉计算机网络基础知识、Internet技术和计算机安全维护等相关知识，为学习者职业生涯发展、终身学习和社会服务奠定基础。
汇编语言程序设计,"张悠慧,翟季冬",清华大学,60111,不仅仅是一门编程语言，汇编语言更是计算机系统软硬件的分界与桥梁，是理解整个计算机系统的有效起点，为学习后续的计算机系统课程打下基础。
大学计算机基础,卫春芳,湖北大学,59128,“大学计算机基础”分为两大部分，一部分是计算机理论教学，另一部分是计算机的应用能力的培养。
面向对象程序设计（C++）,"黄震春,徐明星",清华大学,51815,以C++语言为基础，从设计层面介绍程序设计的重要设计思想和经典设计模式，如面向对象程序设计、基于接口编程、泛型编程等，还将介绍对标准模板库STL。 
计算几何,邓俊辉,清华大学,47959,体味几何之趣，领悟算法之美
R语言数据分析,艾新波,北京邮电大学,45128,数据赋人工系统以智能。《R语言数据分析》从问道、执具、博术三个方面，阐述机器学习/数据挖掘的方法论（道）、编程工具R语言（具）以及经典算法模型（术）。通过课程的学习，可一起领悟数据分析之哲理、掌握模型算法之要义、提升工程实践之素养，推开人工智能的大门，为同学们在机器学习/数据挖掘领域登堂入室奠定基础
Python程序设计基础,许志良,深圳信息职业技术学院,44720,"本课程以任务驱动的方式引导学生完成""十点半游戏”和“2048游戏”开发，融入Python语言的基础知识，掌握面向对象的程序设计技术，掌握Python基本语法、函数、面向对象、图形图像、数据库编程等方面的知识与技能，为从事Python应用程序开发打下基础。"
单片机原理及应用,"杨居义,王颖丽,蒲敏,向兵",绵阳职业技术学院,40847,在数字化转型的大变革中，每天都会遇到上百片单片机的应用，你想学习一门技能吗？你想为人工智能的到来做点准备吗？本课程为你轻松解决学习单片机知识和技能。今天学的将是明天用的！
Web开发技术,"王成良,陈静,徐玲,杨正益,蔡斌",重庆大学,39558,在学习Web开发基本概念、Web开发环境搭建和Web开发工具的使用基础上，通过学习Web前后端开发技术，引导你构建整个Web开发的知识体系，循序渐进地将你领进Web开发的大门，使你掌握开发一个完整的Web应用系统的基本原则、方法和步骤，提高应用Web技术进行软件开发的能力。
ARM微控制器与嵌入式系统,"曾鸣,薛涛,龚光华",清华大学,39448,国家精品在线开放课程。 本课程基于清华大学本科生课程“数字电路与嵌入式系统”，同时是“全国大学生智能车竞赛”微控制器培训课程。 本课程讲授ARM嵌入式系统，鼓励动手实践和自由创新，适合想参与科技活动的本科生和爱好者。
分数域信号与信息处理及其应用,陶然,北京理工大学,20826,你想知道什么是分数傅里叶变换吗？你想知道它与经典的傅里叶变换之间具有怎样的关系吗？你想知道什么是分数域信号与信息处理吗？你想知道分数域信号与信息处理有哪些新理论和新应用吗？想知道这些问题的答案，跟随北京理工大学教授、北京市教学名师陶然教授走进“分数域信号与信息处理及其应用”进行学习吧！
C语言程序设计基础,"李丹,耿植,杨琼,高腾刚",贵州理工学院,20651,是否尝试过学习C语言然后又放弃了，或者学得一知半解无法编程？在本课程里，你将重新发现C语言的关键所在——方法，你将发现编程的魅力!
玩转计算机二级—office高级修炼,"苟燕,刘志国,王强,侯欣舒,王莉",内蒙古师范大学,20506,       你还在为如何通过全国计算机等级考试而苦恼吗？你还在为毕业论文如何排版而发愁吗？你还在为初入职场却因为小白级别的计算机实操能力心中郁闷吗？还等什么？赶快加入“玩转计算机二级—office高级修炼”课程的学习吧！
数据结构（下）,邓俊辉,清华大学,381149,本课程旨在围绕各类数据结构的设计与实现，揭示其中的规律原理与方法技巧；同时针对算法设计及其性能分析，使学生了解并掌握主要的套路与手段。   
操作系统,"向勇,陈渝",清华大学,218894,操作系统课讲解操作系统中如何管理和协调应用程序对计算机系统中软硬件资源的使用。
Java程序设计,郑莉,清华大学,213223,【国家精品课】课程介绍Java的基础语法和面向对象的程序设计方法和GUI程序开发方法。
大数据系统基础,"王建民,徐葳,陈康,陈文光",清华大学,78893,大数据是一门交叉学科。本门课程重点介绍大数据管理的工具平台、开发环境、基本原理。
Office办公软件应用,"史巧硕,朱怀忠,刘洪普,李娟",河北工业大学,75083,Microsoft Office是微软公司开发的一套应用较为广泛的办公软件套装，是日常工作和生活中信息处理的重要工具。本课程主要介绍Microsoft Office中的文字处理软件Word、电子表格处理软件Excel、演示文稿处理软件PowerPoint三个常用组件的基本操作方法。
算法设计与分析,王振波,清华大学,73178,信息时代，算法为王，和我一起进入算法的世界。
数据库系统（上）：模型与语言,战德臣,哈尔滨工业大学,25154,《数据库系统》不仅是计算机、软件工程等专业的核心课程，而且也是非计算机专业学生必修的信息技术课程。当前互联网+与大数据，一切都建立在数据库之上，以数据说话，首先需要聚集数据、需要分析和管理数据。数据库技术已成为各种计算系统的核心技术，数据库相关知识也已成为每个人必须掌握的知识。  ​
学做小程序——实战篇：树洞小程序,"刘强,施建锋,伊甸,小程序慕课讲师",清华大学,24078,本课程是由清华大学软件学院和乐享其约共同制作的微信小程序学习教程，由“乐享其约”资深项目经理、产品经理、前端和后端工程师主讲，微信团队担任技术顾问。通过“需求分析”、“原型设计”、“小程序前端实现”、“后台接口开发”、“小程序对接接口”一步步教同学们如何“从无到有”完成一个小程序项目的开发。
计算机操作系统,"骆斌,葛季栋",南京大学,23855,《计算机操作系统》课程的教学内容：计算机操作系统概述、处理器管理、存储管理、设备管理、文件管理、并发程序设计。学习者能够认知操作系统的基本概念与实现原理，并深入理解操作系统的设计方法与实现技术。
微机原理与接口技术,吴宁,西安交通大学,23701,本课程面向有志于从事计算机控制系统设计、或对计算机硬件结构感兴趣的学习者。总体目标是：具备输入/输出接口控制系统软硬件初步设计能力。课程以“家庭安全防盗系统”案例引导，主要介绍：计算机基础知识、微型机基本工作原理、80x86基本指令集、汇编程序设计、存储器接口设计、I/O接口控制技术等。
Android应用开发基础,"赖红,李钦,李华忠",深圳信息职业技术学院,31177,你是否渴望进入移动互联网开发行业，看到一本本安卓书籍却无从下手！你是否憧憬能够快速开发App，却因案例实践不够，无法入门？现在，就让我们与有着丰富企业开发经验的赖红老师一起，通过案例依次学习Android基本语法和常见组件，通过实例学习Android四大组件和网络框架，最终快速学习如何制作App；
物联网工程导论,"普园媛,何乐生,余鹏飞,杨艳华,艾昌文,尉洪,常俊,周永录,刘宏杰",云南大学,31059,本课程是面向大学一年级物联网工程专业学生开设的物联网导论课程，主要介绍物联网技术的基本概念、关键技术、应用领域及发展现状，帮助大学一年级学生了解物联网工程专业知识与课程体系，尽早确立专业方向，树立创新意识和工程意识。 
大学计算机,"李凤霞,陈宇峰,赵三元",北京理工大学,30084,大学计算机课程将以计算思维为导向，以计算机原理、概念为基础，以新技术新方法为牵引，以创新思维能力培养为目标，和学习者一起了解计算机科学，学习计算技术，掌握思维方法。
学做小程序——基础篇,"刘强,小程序慕课讲师",清华大学,57109,《学做小程序》为中国高校微信应用教育联盟推出的小程序开发系列课程，由资深前端工程师主讲，微信团队担任技术顾问。
基于Linux的C++,乔林,清华大学,56120,本课程旨在建立Linux环境下进行C++程序开发和系统编程时的正确思维和方法，构筑计算思维与实践能力之间的桥梁。
微软亚洲研究院大数据系列讲座,"洪小文,宋睿华,谢幸,郑宇,张洪宇",Microsoft,54240,“这门课程涵盖了互联网搜索、城市计算、社会计算、软件分析、可视化等大数据研究中的热门和前沿领域，课程设计兼具前所未有的广度和深度，我真诚地推荐所有对大数据研究感兴趣的同学去学习这门课程。
计算机网络,"袁华,杜广龙,张凌",华南理工大学,53106,本课程是计算机类专业的基础课程，是研究生入学考试中的计综科目之一。本课程围绕参考模型，探讨信息从源到目的，穿越中间交换设备所遇到的问题和解决办法；涉及到基本原理和重要协议。
```

### 源程序

#### begin.py

```
from scrapy import cmdline
cmdline.execute("scrapy crawl xuetangzaixian".split())
# xuetangzaixian 为爬虫的名字，在 spider.py 中定义
```

#### spider.py

```
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
```

#### items.py

```
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

```

#### pipeline.py

```
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
        try: # 打开 csv 文件
            self.file = open('MyData.csv', "w", encoding="utf-8", newline='')
            self.writer = csv.DictWriter(self.file, fieldnames=self.labels)
        except Exception as err:
            print(err)

    def process_item(self, item, spider):
        self.writer.writerow(item) # 将条目写入到文件中
        return item

    def close_spider(self, spider):
        self.file.close() # 关闭文件
```

#### settings.py

```python
# Scrapy settings for xuetangzaixian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xuetangzaixian'

SPIDER_MODULES = ['xuetangzaixian.spiders']
NEWSPIDER_MODULE = 'xuetangzaixian.spiders'
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'xuetangzaixian.pipelines.MyPipeline': 300,
}
```

## 爬取链家官网二手房的数据

### 实验内容

　　爬取链家官网二手房的数据，目标网页：https://bj.lianjia.com/ershoufang/

​		要求爬取北京市东城、西城、海淀和朝阳四个城区的数据（每个区爬取5 页），将楼盘名称、总价、平米数、单价保存到 json 文件中。

### 实验步骤

#### 配置环境

​		使用 conda 创建一个 Python 3.8 环境并激活该环境。

​		在终端输入```conda install -c conda-forge scrapy```安装 scrapy 库。

​		使用 cd 命令进入项目根目录，在终端输入```scrapy startproject lianjia```创建链家爬虫项目。

#### 创建主运行文件

​		使用 Visual Studio Code 打开该项目，在该目录下创建一个 begin.py 文件（与 scrapy.cfg 在同一级目录下）内容如下：

```
from scrapy import cmdline
cmdline.execute("scrapy crawl lianjia".split())
# lianjia 为爬虫的名字，在 spider.py 中定义
```

#### 创建 Item 类

​		修改 items.py 文件：调用 scrapy.Field() 方法，从 scrapy 提取出 location、name、totalPrice、area 和 unitPrice 五个参数作为 Item 类的成员变量。

```
import scrapy

class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    location = scrapy.Field()
    name = scrapy.Field()
    totalPrice = scrapy.Field()
    area = scrapy.Field()
    unitPrice = scrapy.Field()
    pass

```

#### 编写 Spider 爬虫类和解析方法

​		新建一个 spider.py 文件（在 spider 目录下），设置允许的域名和目标 url 集合。

```
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
```

​		在 spider.py 文件中的 calss mySpider 中，添加 parse 函数，使用 xpath 从响应中提取出楼盘区域、名称、面积、总价和单价，将提取出的信息形成一个 Item 类返回。

```
    def parse(self, response):
        item = MyItem()
        for each in response.xpath("/html/body/div[4]/div[1]/ul/li"):
            item['location'] = response.url.split('/')[-3] # 楼盘区域
            item['name'] = each.xpath("div[1]/div[1]/a/text()").extract()[0] # 楼盘名称
            item['area'] = each.xpath("./div[1]/div[3]/div/text()").extract()[0].split(' | ')[1] # 面积，平米数
            item['totalPrice'] = str(each.xpath("div[1]/div[6]/div[1]/span/text()").extract()[0]) + '万' # 总价，单位：万
            item['unitPrice'] = each.xpath("div[1]/div[6]/div[2]/span/text()").extract()[0] # 单价
            yield(item)
```

#### 编写 Pipeline 类、数据保存方法

​		修改 pipelines.py，使用 UTF-8 格式以写模式打开 csv 文件并设置不换行，创建写字典类实例来将字典写到 csv 文件，处理数据时使用写字典类实例方法来将数据项写到文件中。

```
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
```

​		修改 setting.py，其他设置不变，使用 pipeline 并且不遵守机器人规则。

```
添加 ITEM_PIPELINES = {
    'lianjia.pipelines.MyPipeline': 300,
}
修改 ROBOTSTXT_OBEY = False
```

- 参数是分配给每个类的整型值，确定了它们运行的顺序，item 按数字从低到高的顺序，通过 pipeline。

- 通常将这些数字定义在 0 - 1000 范围内。

​		运行 begin.py

​		或者运行 spider.py ，并将其运行时的 Script path 配置项修改为 begin.py

### 

### 获取的 JSON 文件：MyData.json

​		获取到 600 条课程信息，其中前 50 条信息如下：

```
{"location": "dongcheng", "name": "光明楼 南北通透两居室   中间楼层 不临街", "area": "54.19平米", "totalPrice": "588万", "unitPrice": "108,508元/平"}
{"location": "dongcheng", "name": "广渠门内大街 户型方正三居室 采光好", "area": "79.4平米", "totalPrice": "790万", "unitPrice": "99,497元/平"}
{"location": "dongcheng", "name": "东花市北里中区 3室2厅 南 北", "area": "100.27平米", "totalPrice": "1038万", "unitPrice": "103,521元/平"}
{"location": "dongcheng", "name": "新景家园东区 全凸南向一居室 满五年唯一 随时看", "area": "59.65平米", "totalPrice": "765万", "unitPrice": "128,249元/平"}
{"location": "xicheng", "name": "格调小区 精装大一居，满五唯一", "area": "87.44平米", "totalPrice": "855万", "unitPrice": "97,782元/平"}
{"location": "dongcheng", "name": "东城和平里五区一居室  值得选择", "area": "40.57平米", "totalPrice": "555万", "unitPrice": "136,801元/平"}
{"location": "xicheng", "name": "满五年 成本价 诚心出售 小两居 复兴门外大街", "area": "51.7平米", "totalPrice": "730万", "unitPrice": "141,200元/平"}
{"location": "xicheng", "name": "汽北小区小区 南北通透两居室 诚心出售", "area": "52.8平米", "totalPrice": "650万", "unitPrice": "123,107元/平"}
{"location": "dongcheng", "name": "板厂南里  低楼层 南北通透 满五年唯一 不临街", "area": "50.04平米", "totalPrice": "590万", "unitPrice": "117,906元/平"}
{"location": "dongcheng", "name": "广渠门内大街两居室满五年唯一诚心出售", "area": "60.38平米", "totalPrice": "623万", "unitPrice": "103,180元/平"}
{"location": "dongcheng", "name": "东直门 东城区 东方银座 西南向两居室", "area": "113.17平米", "totalPrice": "870万", "unitPrice": "76,876元/平"}
{"location": "xicheng", "name": "西城区 南向一居 低楼层 无遮挡 满五年央产房", "area": "40.37平米", "totalPrice": "460万", "unitPrice": "113,946元/平"}
{"location": "xicheng", "name": "红莲东南向阳光两居，满五唯一、电梯房，1995年建成", "area": "70.26平米", "totalPrice": "725万", "unitPrice": "103,189元/平"}
{"location": "dongcheng", "name": "国瑞城中区  高层 南向一居室", "area": "58.67平米", "totalPrice": "633万", "unitPrice": "107,892元/平"}
{"location": "dongcheng", "name": "全南向 无遮挡 精装修 周边配套齐全 诚心出售", "area": "58.45平米", "totalPrice": "688万", "unitPrice": "117,708元/平"}
{"location": "dongcheng", "name": "小黄庄1区  高楼层双朝南精装两居", "area": "72.44平米", "totalPrice": "784万", "unitPrice": "108,228元/平"}
{"location": "xicheng", "name": "广安门外南街67号院 2室1厅 南 北", "area": "54.01平米", "totalPrice": "545万", "unitPrice": "100,908元/平"}
{"location": "xicheng", "name": "西城两居，南北无遮挡，视野好，小区管理好，湾子站。", "area": "58.86平米", "totalPrice": "609万", "unitPrice": "103,466元/平"}
{"location": "xicheng", "name": "马甸南村  南北通透两居  把边户型  临近公园", "area": "65.11平米", "totalPrice": "990万", "unitPrice": "152,051元/平"}
{"location": "xicheng", "name": "西直门南大街四居室业主诚心出售，看房方便", "area": "94.2平米", "totalPrice": "1300万", "unitPrice": "138,005元/平"}
{"location": "dongcheng", "name": "天天家园 3室1厅 南", "area": "125.11平米", "totalPrice": "850万", "unitPrice": "67,941元/平"}
{"location": "xicheng", "name": "信和嘉园 南北通透 精装修 户型方正 看房方便 诚心卖", "area": "308.5平米", "totalPrice": "2688万", "unitPrice": "87,132元/平"}
{"location": "xicheng", "name": "红居南街 2室1厅 西北", "area": "45.77平米", "totalPrice": "469万", "unitPrice": "102,469元/平"}
{"location": "xicheng", "name": "侨办大院  三室一厅  有电梯  满五年唯一", "area": "93.9平米", "totalPrice": "1400万", "unitPrice": "149,095元/平"}
{"location": "xicheng", "name": "红莲晴园 三居双卫 阳台大 中间楼层 采光好 无遮挡", "area": "117.67平米", "totalPrice": "1200万", "unitPrice": "101,981元/平"}
{"location": "dongcheng", "name": "东直门外大街(东城）双南向两居室", "area": "80.1平米", "totalPrice": "780万", "unitPrice": "97,379元/平"}
{"location": "dongcheng", "name": "东南三居室 全天采光 封闭式管理 人车分流 距地铁50米", "area": "97.45平米", "totalPrice": "1130万", "unitPrice": "115,957元/平"}
{"location": "dongcheng", "name": "东城区 次新小区 一梯四户 使用面积大 东南向高层", "area": "67.53平米", "totalPrice": "698万", "unitPrice": "103,362元/平"}
{"location": "dongcheng", "name": "京城仁合 不临二环不临火车 2018年装修 无遮挡采光好", "area": "114.51平米", "totalPrice": "1050万", "unitPrice": "91,696元/平"}
{"location": "dongcheng", "name": "东交民巷 满五唯一 中高层 独立小区 可免费停车", "area": "49.38平米", "totalPrice": "620万", "unitPrice": "125,557元/平"}
{"location": "dongcheng", "name": "70年产权商品房 精装修 有燃气 满五年唯一 朝南", "area": "63.35平米", "totalPrice": "619万", "unitPrice": "97,712元/平"}
{"location": "dongcheng", "name": "海晟名苑北区西向开间，视野无遮挡，精装修拎包入住", "area": "46平米", "totalPrice": "530万", "unitPrice": "115,218元/平"}
{"location": "dongcheng", "name": "东二环内中间楼层，东南两居满五年，电梯楼。", "area": "59.87平米", "totalPrice": "628万", "unitPrice": "104,894元/平"}
{"location": "dongcheng", "name": "安定门外大街一居室带电梯，三环内，正对花园。", "area": "46.83平米", "totalPrice": "540万", "unitPrice": "115,311元/平"}
{"location": "xicheng", "name": "满五唯一  东西向两居室    户型方正   诚心出售", "area": "48.5平米", "totalPrice": "499万", "unitPrice": "102,887元/平"}
{"location": "xicheng", "name": "西便门内大街97号院 二环里 满五年央产 中间楼层", "area": "57.51平米", "totalPrice": "591万", "unitPrice": "102,765元/平"}
{"location": "xicheng", "name": "西四北大街160号西四北大街160号西四北大街160号", "area": "49.5平米", "totalPrice": "750万", "unitPrice": "151,516元/平"}
{"location": "dongcheng", "name": "东城 西革新里110号院 满五年唯一", "area": "44.44平米", "totalPrice": "376万", "unitPrice": "84,609元/平"}
{"location": "dongcheng", "name": "东单 金宝街 东堂子 中间楼层 户型好 诚意出售", "area": "44.32平米", "totalPrice": "525万", "unitPrice": "118,457元/平"}
{"location": "dongcheng", "name": "海运仓小区朝南向采光好   满五唯一   楼层好视野宽阔", "area": "47.87平米", "totalPrice": "650万", "unitPrice": "135,785元/平"}
{"location": "dongcheng", "name": "二环内新上东南两居室 诚心出售", "area": "51.17平米", "totalPrice": "660万", "unitPrice": "128,982元/平"}
{"location": "xicheng", "name": "裕中东里南北三居 全明格局 可签约", "area": "77.8平米", "totalPrice": "998万", "unitPrice": "128,278元/平"}
{"location": "xicheng", "name": "双南向，电梯房，采光好, 满五年住房, 随时看房", "area": "50.7平米", "totalPrice": "730万", "unitPrice": "143,985元/平"}
{"location": "xicheng", "name": "信建里小区 1室1厅 南", "area": "36.41平米", "totalPrice": "519万", "unitPrice": "142,544元/平"}
{"location": "xicheng", "name": "马相西巷中间楼层，无遮挡，随时签约，采光好", "area": "39.61平米", "totalPrice": "595万", "unitPrice": "150,215元/平"}
{"location": "dongcheng", "name": "东城区 悠胜美苑 03年新楼 商品房 视野好", "area": "70.17平米", "totalPrice": "545万", "unitPrice": "77,669元/平"}
{"location": "dongcheng", "name": "龙潭湖 龙潭北里小区 规整社区 配套齐全全南向三居室", "area": "65.37平米", "totalPrice": "630万", "unitPrice": "96,375元/平"}
{"location": "dongcheng", "name": "忠实里东区 中间层 带电梯 商品房", "area": "57.71平米", "totalPrice": "632万", "unitPrice": "109,514元/平"}
{"location": "dongcheng", "name": "北河沿大街 中间楼层东向两居室", "area": "53.03平米", "totalPrice": "666万", "unitPrice": "125,590元/平"}
{"location": "xicheng", "name": "三里河南二巷双南两居，采光好，无遮挡", "area": "54.9平米", "totalPrice": "789万", "unitPrice": "143,716元/平"}
```

### 源程序

#### begin.py

```python
from scrapy import cmdline
cmdline.execute("scrapy crawl lianjia".split())
# lianjia 为爬虫的名字，在 spider.py 中定义
```

#### spider.py

```
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
```

#### items.py

```
import scrapy

class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    location = scrapy.Field()
    name = scrapy.Field()
    totalPrice = scrapy.Field()
    area = scrapy.Field()
    unitPrice = scrapy.Field()
    pass

```

#### pipelines.py

```
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

```

#### settings.py

```
BOT_NAME = 'lianjia'

SPIDER_MODULES = ['lianjia.spiders']
NEWSPIDER_MODULE = 'lianjia.spiders'

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'lianjia.pipelines.MyPipeline': 300,
}
```

## 结语

​		使用 Python 语言的 scrapy 库可以比较容易地从互联网上爬取我们需要的数据，爬取的过程中使用 xpath 对 html 标签进行定位和提取，最后将爬取到的数据保存在 CSV 或者 JSON 文件中。对于静态的页面我们可以在 http 响应中直接提取数据，对于动态的页面我们可以通过 api 获取数据，这时需要设置 headers 和 cookies 形成 request 并发送才能通过响应来获取数据。当我们需要爬取多个页面时，可以生成多个 url 并添加到起始 url 列表中，也可以发送多个请求来爬取多个页面。通过本次实验，初步掌握了多种页面数据爬取的方法。
