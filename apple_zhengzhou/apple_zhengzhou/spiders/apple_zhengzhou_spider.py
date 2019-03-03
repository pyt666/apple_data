# -*- coding: utf-8 -*-
import scrapy


class AppleZhengzhouSpiderSpider(scrapy.Spider):
    name = 'apple_zhengzhou_spider'
    allowed_domains = ['czce.com.cn']
    start_urls = ['http://www.czce.com.cn/cn/sspz/pg/H770221index_1.htm']

    def parse(self, response):
        s = response.xpath("//div[@class='container']//script[1]/@src").extract_first()
        url = "http://app.czce.com.cn/cms/cmsface/czce/newcms/calendarnewOne.jsp?curpath="+ str(s)
        url +="&curpath1="
