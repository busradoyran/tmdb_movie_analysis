# TMDB Movie Data Analysis Project

This project consists of two main parts:
1. A Scrapy-based web scraper that collects movie information from The Movie Database (TMDB) website
2. Data analysis of the collected movie data using Google Colab

## Quick Start - Analysis Only

If you just want to run the analysis:

1. Open the analysis notebook in Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/busradoyran/tmdb_movie_analysis/blob/main/analysis/TMDB_Movie_Analysis.ipynb)
2. The notebook will automatically load the data from this repository
3. Run the cells to see the analysis

## Project Structure

```
TMDB_Scraping_Analysis-1.0/
├── films/                      # Scraping project
│   ├── films/
│   │   ├── spiders/
│   │   │   ├── filmspider.py  # Main spider for TMDB scraping
│   │   ├── items.py
│   │   └── middlewares.py
│   └── scrapy.cfg
├── data/                       # Data directory
│   └── tmdb_movies.csv        # Scraped movie data
├── analysis/                   # Analysis project
│   └── TMDB_Analysis.ipynb    # Colab notebook for data analysis
└── README.md
```

## Features

### Scraping
- Collects detailed movie information from TMDB including:
  - Title
  - Release date
  - User rating
  - Director
  - Writer
  - Genres
  - Runtime
  - Original language
  - Budget
  - Revenue

### Analysis
- Jupyter notebook with detailed analysis of the movie data
- Data preprocessing and cleaning
- Feature engineering
- Statistical analysis
- Visualizations of movie trends and patterns

## Running the Project

### Option 1: Use Pre-scraped Data (Recommended)
The `data/tmdb_movies.csv` file in this repository contains already scraped movie data. This is the recommended way to start with the analysis:

1. Open the analysis notebook in Google Colab using the badge above
2. The notebook will automatically load the data
3. Follow the analysis steps in the notebook

### Option 2: Run the Scraper Yourself

If you want to scrape fresh data:

1. Clone this repository:
```bash
git clone https://github.com/busradoyran/tmdb_movie_analysis.git
cd TMDB_Scraping_Analysis
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install scrapy
```

4. Run the spider:
```bash
cd films
scrapy crawl tmdb
```

The scraped data will be saved to `data/tmdb_movies.csv`.

## Data Description

The `tmdb_movies.csv` file contains the following columns:
- `title`: Movie title
- `release_date`: Release date of the movie
- `rating`: User rating on TMDB
- `director`: Movie director
- `writer`: Movie writer
- `genres`: Movie genres (comma-separated)
- `runtime`: Movie duration
- `original_language`: Original language of the movie
- `budget`: Movie budget
- `revenue`: Movie revenue

## Analysis Highlights

The analysis notebook (`analysis/TMDB_Analysis.ipynb`) includes:
- Data cleaning and preprocessing
- Feature engineering (including language encoding, genre processing, runtime conversion)
- Statistical analysis of movie trends
- Handling missing values
- Data normalization
- Movie clustering analysis
- Visualizations of key insights

## Notes

- The spider includes a delay between requests to respect TMDB's rate limits
- Currently set to scrape up to 500 pages of movie listings
- The provided dataset was scraped on March 25, 2024

## License

This project is open source and available under the MIT License. 