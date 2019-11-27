# Biblio Bot
A Slack bot that notifies me when newly-released books are available for request at my library

## Technologies
This project is created with:
-Python ver 3.6
-Selenium Webdriver
-Chromium browser automation 
-Slack

## Scraper 
book_scrapy.py searches for each book in the Wishlist Template that hasn't notified the user if it is available for request. It scrapes the library website using Selenium to see if the book can be requested. If a book can be requested, a link to request it will be posted on the specified Slack channel. 

Runs every 30 minutes. 
