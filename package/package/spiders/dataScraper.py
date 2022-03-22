import scrapy
import re

def clean(string):
    result = list()
    for i in string:
        result.append(re.sub(" +|\n|\r|\t|\0|\x0b|\xa0", ' ', i).strip())
    return result

class DatascraperSpider(scrapy.Spider):
    name = 'dataScraper'
    
    def __init__(self, category='', **kwargs):
        self.start_urls = ['https://natashaskitchen.com/recipes/']
        self.count = 0
        super().__init__(**kwargs)

    def parse(self, response):
        link = response.css('.ingcol-a a').css('::attr(href)').extract()
        for i in link:
            yield response.follow(i, callback=self.get_recipe)
        print(self.count)
    
    def get_recipe(self, response):
        link = response.css('#main-a a').css('::attr(href)').extract()
        # self.count = self.count + len(link)
        print(self.count)
        # print(link)
        for j in link:
            self.count = self.count + 1
            yield response.follow(j, callback=self.get_details)
        yield
            
    def get_details(self, response):
        # name = clean(response.css('.wprm-recipe-name::text').extract())
        # time = clean(response.css('.wprm-recipe-cook_timeunit-hours , .wprm-recipe-cook_time-hours').css('::text').extract())
        # course = clean(response.css('.wprm-recipe-newcourse::text').extract())
        # cuisine = clean(response.css('.wprm-recipe-newcuisine::text').extract())
        # serves = clean(response.css('.wprm-recipe-servings-75112::text').extract())
        # calorie = clean(response.css('.wprm-recipe-calories::text').extract())
        # ingridients_amount = clean(response.css('.wprm-recipe-ingredient-amount').css('::text').extract())
        # ingridients_unit = clean(response.css('.wprm-recipe-ingredient-unit').css('::text').extract())
        # ingridients_name = clean(response.css('.wprm-recipe-ingredient-namet').css('::text').extract())
        # # ingridients = ingridients_amount + ' ' + ingridients_unit + ' '+ ingridients_name + '.'
        # instruction = clean(response.css('.wprm-recipe-instruction-text , .wprm-recipe-instruction-text p').css('::text').extract())
        # print(name, time, course, cuisine, serves, calorie, ingridients_name, instruction)

        yield
