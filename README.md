# biblio-bot
A Slack bot that notifies me when newly-released books are available for request at my library


## Scraper 
book_scrapy.py searches for each book in the Wishlist Template that isn't available for request yet. It scrapes the library website using Selenium by automated clicks. 
Runs every 30 minutes. 
