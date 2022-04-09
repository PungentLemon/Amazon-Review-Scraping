import scrapy
from datetime import datetime

reviews_url = 'https://www.amazon.in/product-review/B07PFFMP9P/{}'
asin_list = ['B07PFFMP9P']

#Creating custom function
def bool_check(txt):
    if txt=='Verified Purchase':
        return True
    else:
        return False

def helpful(txt):
    num=''
    if txt==None:
        num='0'
    elif txt=='One person found this helpful':
        num='1'
    else:
        for x in txt:
            if x.isdigit()==True:
                num=num+x
    return int(num)

def date(txt):
    a=datetime.strptime(txt,'%d %B %Y').strftime('%d/%m/%Y')
    return a


class ScrapeSpider(scrapy.Spider):
    name = 'scrape'

    def start_requests(self):
        for asin in asin_list:
            url = reviews_url.format(asin)
            yield scrapy.Request(url)

    def parse(self, response):
        for review in response.css('[data-hook="review"]'):
            item = {
                'Name': review.css('.a-profile-name ::text').get(),
                'Stars': int(review.css('[data-hook="review-star-rating"] ::text').get()[0:1]),
                'Reviewed_Country': review.css('[data-hook="review-date"] ::text').get()[12:17],
                'Date': date(review.css('[data-hook="review-date"] ::text').get()[21:]),
                'Verified': bool_check(review.css('[data-hook="avp-badge"] ::text').get()),
                'HelpfulVotes': helpful(review.css('[data-hook="helpful-vote-statement"] ::text').get()),
                'Title': review.css('[data-hook="review-title"] span ::text').get(),
                'Review': review.xpath('normalize-space(.//*[@data-hook="review-body"])').get()
            }
            yield item
        next_page= response.xpath('//a[text()="Next page"]/@href').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
