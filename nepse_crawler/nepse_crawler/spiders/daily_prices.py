import scrapy
import re


class DailyPricesSpider(scrapy.Spider):
    name = 'daily_prices'
    allowed_domains = ['www.nepalstock.com']
    start_urls = ['http://www.nepalstock.com/todaysprice']
    names = ['SN', 'Name', 'No. Of Transaction','Max Price', 'Min Price', 'Closing Price' , 'Traded Shares',
             'Amount',	'Previous Closing']

    def parse(self, response):
        companies_all = response.xpath("//div[@id='home-contents']/table/tr").getall()[2:-4]
        for each in companies_all:
            yield dict(zip(self.names, [data for data in re.findall(r'<td.*>(.*)</td>', each.strip())]))

        next_page = response.xpath('//a[@title="Next Page"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)