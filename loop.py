from selenium import webdriver
import time
import sys
import traceback
from library_scraper import scraping_books

if __name__ == "__main__":
    while True:
        print("{}: Starting scrape cycle".format(time.ctime()))
        # scraping(driver)
        try:
            scraping_books()
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error with scraping:", sys.exc_info()[0])
            traceback.print_exc()
        else: 
            print("{}: End of scrape cycle".format(time.ctime()))
        time.sleep(60)