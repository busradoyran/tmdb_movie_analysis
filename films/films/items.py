# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TMDBMovieItem(scrapy.Item):
    title = scrapy.Field()
    release_date = scrapy.Field()
    rating = scrapy.Field()
    director = scrapy.Field()
    writer = scrapy.Field()
    genres = scrapy.Field()
    runtime = scrapy.Field()
    original_language = scrapy.Field()
    budget = scrapy.Field()
    revenue = scrapy.Field()
