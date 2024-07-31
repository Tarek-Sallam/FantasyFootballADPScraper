import pandas as pd
import numpy as np
import os

raw_data = []
path = os.path.join(os.getcwd(), 'raw_data');

for i in range(9):
    raw_data.append(pd.read_csv(os.path.join(path, 'adp_raw_' + str(2015+i) + '.csv')))

## concatenate all the year data
all_adps = pd.concat(raw_data).sort_values('adp')

## seperate all the data by each position
adp_by_pos = {'QB': all_adps[all_adps['position'] == 'QB'].reset_index(drop=True), 
              'RB': all_adps[all_adps['position'] == 'RB'].reset_index(drop=True), 
              'WR': all_adps[all_adps['position'] == 'WR'].reset_index(drop=True), 
              'TE': all_adps[all_adps['position'] == 'TE'].reset_index(drop=True),
              'K': all_adps[all_adps['position'] == 'K'].reset_index(drop=True),
              'DEF': all_adps[all_adps['position'] == 'DST'].reset_index(drop=True)}

all_adp = {}
normalized_adp = {}

## drop the positon column, convert to np array and normalize each position
for pos, value in adp_by_pos.items():
    all_adp[pos] = value['adp'].to_numpy()
    normalized_adp[pos] = all_adp[pos] / all_adp[pos].size
    
np.save(os.path.join(os.getcwd(), 'cleaned_data', 'adp_data.npy'), normalized_adp)