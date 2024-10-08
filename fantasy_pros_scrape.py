from bs4 import BeautifulSoup
import requests
import os
import pandas as pd

def scrape_adp_data(path) -> None:
    url1 = 'https://www.fantasypros.com/nfl/adp/ppr-overall.php?year='
    for i in range(9):
        url = url1 + '20' + (str)(i+15)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, features='html.parser')
        table = soup.find('table').find('tbody')
        all_players = table.find_all('tr', recursive=False)
        pos = []
        avg = []

        for player in all_players:
            pos.append(''.join([j for j in (player.find_all('td')[2].text) if not j.isdigit()]))
            avg.append(float(player.find_all('td')[-1].text.replace(',', '')))
        df = pd.DataFrame({'position': pos, 'adp': avg})
        df.to_csv(os.path.join(path, 'adp_raw_' + '20' + (str)(i+15) + '.csv'), index=False)
