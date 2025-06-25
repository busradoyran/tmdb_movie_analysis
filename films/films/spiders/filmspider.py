import random
import scrapy
from scrapy import Request
from films.items import TMDBMovieItem

class TMDBSpider(scrapy.Spider):
    name = 'tmdb'
    allowed_domains = ['themoviedb.org']
    start_urls = ['https://www.themoviedb.org/movie?language=tr&page=1']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'FEED_FORMAT': 'csv',
        'FEED_URI': '../../data/tmdb_movies.csv'
    }

    def parse(self, response):
        movies = response.css('div.card.style_1')
        for movie in movies:
            detail_url = response.urljoin(movie.css('h2 a::attr(href)').get())
            yield scrapy.Request(detail_url, callback=self.parse_movie_details)

        current_page = int(response.url.split('page=')[-1])
        next_page = current_page + 1
        next_page_url = f'https://www.themoviedb.org/movie?language=tr&page={next_page}'

        if next_page <= 500:
            yield response.follow(next_page_url, callback=self.parse)

    def parse_movie_details(self, response):
        facts = response.css('section.split_column p')

        has_original_title = 'Orijinal Başlık' in facts[0].css('::text').extract_first()

        if has_original_title:
            original_language_index = 2
            budget_index = 3
            revenue_index = 4
        else:
            original_language_index = 1
            budget_index = 2
            revenue_index = 3

        original_language = facts[original_language_index].css('::text').extract()
        original_language = original_language[1].strip() if len(original_language) > 1 else None

        budget_and_revenue = facts[budget_index].css('::text').extract()
        budget = budget_and_revenue[1].strip() if len(budget_and_revenue) > 1 else None

        revenue_and_revenue = facts[revenue_index].css('::text').extract()
        revenue = revenue_and_revenue[1].strip() if len(revenue_and_revenue) > 1 else None

        # Corrected title selector
        title = response.css('div.title h2 a::text').get()
        if not title:
            self.logger.warning(f"Missing title for URL: {response.url}")

        item = TMDBMovieItem(
            title=title,
            release_date=response.css('div.facts span.release::text').get().strip(),
            rating=response.css('.user_score_chart::attr(data-percent)').get(),
            director=response.css('ol.people.no_image li.profile:contains("Director") a::text').get(),
            writer=response.css('ol.people.no_image li.profile:contains("Writer") a::text').get(),
            genres=response.css('span.genres a::text').getall(),
            runtime=response.css('span.runtime::text').get().strip(),
            original_language=original_language,
            budget=budget,
            revenue=revenue
        )
        yield item
