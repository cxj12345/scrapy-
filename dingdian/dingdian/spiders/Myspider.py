import scrapy

# 解决引入DIngdianItem报错
import sys
sys.path.append(r"E:\桌面\py\scrapy\dingdian")
from dingdian.items import DingdianItem

class Myspider(scrapy.Spider):
	name = 'dingdian'
	allowed_domains = ['x23us.com']
	bash_url = 'https://www.x23us.com/class/'
	bashurl = '.html'

	start_urls = []
	for i in range(1 ,11):
		url = bash_url + str(i) + '_1' + bashurl
		start_urls.append(url)

	def parse(self, response):
		for td in response.xpath('//div[@class="main"]/div[@id="centerm"]/div[@class="bdsub"]/dl[@id="content"]//tr[@bgcolor="#FFFFFF"]'):
			yield{
				'name': td.xpath('./td[@class="L"]/a[@title]/@title').extract_first()[:-2],
				'author': td.xpath('./td[@class="C"]/text()').extract_first(),
				'noveurl': td.xpath('./td/a/@href').extract_first(),
				'serialstatus': td.xpath('./td[@class="C"]/text()').extract()[2],
				'serialnumber': td.xpath('./td[@class="R"]/text()').extract_first(),
				'category': response.xpath('//div[@class="bdsub"]//dt/h2/text()').extract_first()[:-6],
				'name_id': td.xpath('./td/a/@href').extract_first()[27:],
			}

		next_page_url = response.xpath('//div[@class="pagelink"]/a[@class="next"]/@href').extract_first() 
		if next_page_url is not None:
			yield scrapy.Request(response.urljoin(next_page_url))

