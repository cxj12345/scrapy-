# import scrapy
# from scrapy.http import Request

# # 解决引入DIngdianItem报错
# import sys
# sys.path.append(r"E:\桌面\py\scrapy\dingdian")
# from dingdian.items import DingdianItem

# class Myspider(scrapy.Spider):
# 	name = 'dingdian'
# 	allowed_domains = ['x23us.com']
# 	bash_url = 'https://www.x23us.com/class/'
# 	bashurl = '.html'

# 	def start_requests(self):
# 		for i in range(1, 11):
# 			url = self.bash_url + str(i) +'_1' + self.bashurl
# 			yield Request(url, self.parse)

# 	def parse(self, response):
# 		response.encodeing = 'gbk'
# 		max_num = response.xpath('//div[@class="bdsub"]//div[@class="pagelink"]/a[@class="last"]')
# 		bashurl = str(response.url)[:-7]
# 		for num in range(1, int(max_num) + 1):
# 			url = bashurl + '_' + str(num) + self.bashurl
# 			yield Request(url, callback = self.get_name)

# 	def get_name(self, response):
# 		tds = response.xpath('//div[@class="blockcontent"]/ul/li/a[@target]')
# 		for td in tds:
# 			novelname = td.text
# 			novelurl = td.xpath('./@href')
# 			yield Request(novelurl, callback = self.get_chapterurl, meta={'name': novelname, 'url': novelurl})

# 	def get_chapterurl(self, response):
# 		item = DingdianItem()
# 		item['name'] = str(response.meta['name'])
# 		item['url'] = response.meta['url']
# 		return item


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

	start_urls = ['https://www.x23us.com/class/9_1.html']
	# for i in range(1 ,2):
	# 	url = bash_url + str(i) + '_1' + bashurl
	# 	start_urls.append(url)

	def parse(self, response):
		for td in response.xpath('//div[@class="bdsub"]//tbody/tr[@bgcolor="#FFFFFF"]'):
			yield{
				'name': n.xpath('./td[@class="L"]/a[@title]/@title')[0][:-2],
				'author': n.xpath('./td[@class="C"]/text()')[0],
				'noveurl': n.xpath('./td/a/@href')[0],
				'serialstatus': n.xpath('./td[@class="C"]/text()')[2],
				'serialnumber': n.xpath('./td[@class="R"]/text()')[0],
				'category': tree.xpath('//div[@class="bdsub"]//dt/h2/text()')[0][:-6],
				'name_id': noveurl[27:],
			}

		next_page_url = response.xpath('//div[@class="pagelink"]/a[@class="next"]/@href').extract_first() 
		if next_page_url is not None:
			yield scrapy.Request(response.urljoin(next_page_url))

