import re
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]

    start_urls = [
        "https://books.toscrape.com/catalogue/page-1.html"
    ]

    max_pages = 5

    def parse(self, response):
        """
        Reads one catalogue page, visits every book page,
        and follows pagination until page 5.
        """

        book_links = response.css(
            "article.product_pod h3 a::attr(href)"
        ).getall()

        for book_link in book_links:
            yield response.follow(
                book_link,
                callback=self.parse_book
            )

        page_match = re.search(
            r"page-(\d+)\.html",
            response.url
        )

        if page_match:
            current_page = int(page_match.group(1))
        else:
            current_page = 1

        self.logger.info(
            "Processing catalogue page %s",
            current_page
        )

        if current_page < self.max_pages:
            next_page = response.css(
                "li.next a::attr(href)"
            ).get()

            if next_page:
                yield response.follow(
                    next_page,
                    callback=self.parse
                )

    def parse_book(self, response):
        """
        Extracts all required fields from one individual book page.
        """

        rating_class = response.css(
            "div.product_main p.star-rating::attr(class)"
        ).get()

        rating = None

        if rating_class:
            rating = rating_class.replace(
                "star-rating",
                ""
            ).strip()

        availability = " ".join(
            text.strip()
            for text in response.css(
                "div.product_main p.instock.availability::text"
            ).getall()
            if text.strip()
        )

        product_information = {}

        for row in response.css(
            "table.table.table-striped tr"
        ):
            heading = row.css("th::text").get()
            value = row.css("td::text").get()

            if heading:
                product_information[heading.strip()] = (
                    value.strip() if value else None
                )

        yield {
            "title": response.css(
                "div.product_main h1::text"
            ).get(),

            "category": response.css(
                "ul.breadcrumb li:nth-last-child(2) a::text"
            ).get(),

            "price": response.css(
                "div.product_main p.price_color::text"
            ).get(),

            "rating": rating,

            "availability": availability,

            "product_description": response.css(
                "#product_description + p::text"
            ).get(),

            "upc": product_information.get("UPC"),

            "number_of_reviews": product_information.get(
                "Number of reviews"
            ),

            "product_url": response.url,
        }