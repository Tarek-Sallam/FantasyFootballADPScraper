from fantasy_pros_scrape import scrape_adp_data, scrape_proj_data
import os

path1 = os.path.join(os.getcwd(), 'raw_data', 'adp')
path2 = os.path.join(os.getcwd(), 'raw_data', 'total_pts')

scrape_adp_data(path1)
scrape_proj_data(path2)