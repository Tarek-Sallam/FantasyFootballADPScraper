from fantasy_pros_data_scrape import scrape_adp_data
import os

path = os.path.join(os.getcwd(), 'raw_data')
scrape_adp_data(path)