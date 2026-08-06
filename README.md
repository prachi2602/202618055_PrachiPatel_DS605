# Book Data Pipeline Using Python and Scrapy

## Student Information

- **Name:** Prachi Patel
- **Student ID:** 202618055
- **Course:** DS605 – Fundamentals of Machine Learning

## Assignment Objective

The objective of this project is to build a complete data pipeline by scraping book information using Python and Scrapy, cleaning and transforming the collected data, creating visualizations, and reporting meaningful data-driven insights.

## Website Used

Books to Scrape: https://books.toscrape.com/

## Dataset Scope

The Scrapy spider collected 100 books from the first five catalogue pages. Each individual book page was visited to extract the following fields:

- Title
- Category
- Price
- Rating
- Availability
- Product description
- UPC
- Number of reviews
- Product URL

## Project Files

- `book_scraper/spiders/books_spider.py` – Scrapy spider
- `book_data_pipeline.ipynb` – preprocessing, visualizations, analysis, and insights
- `books_raw.csv` – original scraped dataset
- `books_cleaned.csv` – cleaned and transformed dataset
- `price_distribution.png` – price distribution plot
- `rating_distribution.png` – rating distribution plot
- `average_price_by_category.png` – category price comparison
- `price_vs_rating.png` – relationship between price and rating
- `description_wordcloud.png` – word cloud from book descriptions

## Data Preprocessing

The preprocessing steps included:

- Cleaning extra spaces and inconsistent text
- Handling missing product descriptions
- Removing duplicate books using UPC
- Converting price into numeric format
- Mapping ratings from One–Five to 1–5
- Extracting the available stock count
- Converting review counts into integers

## Engineered Features

The following features were created:

- `description_word_count`
- `price_band`
- `affordability_score`
- `value_score`
- `recommended`

## Main Results

- Total scraped records: 100
- Missing values in the raw dataset: 0
- Duplicate UPC values: 0
- Average book price: £34.56
- Minimum book price: £10.16
- Maximum book price: £58.11
- Price-rating correlation: -0.122
- Most represented category: Sequential Art
- Number of recommended books: 21

The correlation value shows that book price and rating have almost no meaningful relationship.

## Limitations

Books to Scrape is a practice website and does not represent a real commercial bookstore. The ratings, stock levels, prices, and review counts may not reflect real customer behaviour. Only 100 books from five pages were analysed. Written reviews were unavailable, so product descriptions were used for the word cloud.

