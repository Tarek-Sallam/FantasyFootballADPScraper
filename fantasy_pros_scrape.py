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
        names = []
        pos = []
        avg = []

        for player in all_players:
            names.append(player.find_all('td')[1].find('a').text)
            pos.append(player.find_all('td')[2].text)
            avg.append(float(player.find_all('td')[-1].text.replace(',', '')))
            
        df = pd.DataFrame({'name': names, 'position': pos, 'adp': avg})
        df.to_csv(os.path.join(path, 'adp_raw_' + '20' + (str)(i+15) + '.csv'), index=False)

def scrape_proj_data(path) -> None:
    url1 = "https://www.fantasypros.com/nfl/reports/leaders/ppr.php?year="
    for i in range(9):
        url = url1 + '20' + (str)(i+15)
        weeks = 17 if i < 8 else 18
        page = requests.get(url)
        soup = BeautifulSoup(page.text, features='html.parser')
        table = soup.find('table').find('tbody')
        all_players = table.find_all('tr', recursive=False)
        names = []
        pos = []
        pts = []

        for player in all_players:
            items = player.find_all('td')
            names.append(items[1].find('a').text)
            pos.append(items[2].text)
            weeks_played = weeks
            sum = 0
            for j in range(4, weeks + 4):
                if items[j].text == 'BYE' or items[j].text == '-':
                    weeks_played-=1
                    sum+=0
                else:
                    sum+= float((items[j].text))
            sum/=weeks_played if weeks_played !=0 else 1
            pts.append(sum)

        df = pd.DataFrame({'name': names, 'position': pos, 'points': pts})
        df.to_csv(os.path.join(path, 'adp_raw_' + '20' + (str)(i+15) + '.csv'), index=False)
            


     