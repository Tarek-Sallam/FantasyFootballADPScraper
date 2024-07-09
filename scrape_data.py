from fantasy_pros_scrape import scrape_adp_data
import os

path1 = os.path.join(os.getcwd(), 'raw_data')
scrape_adp_data(path1)