import pandas as pd
import numpy as np
import os

raw_data = []
path = os.path.join(os.getcwd(), 'raw_data');

for i in range(9):
    raw_data.append(pd.read_csv(os.path.join(path, 'adp_raw_' + str(2015+i) + '.csv')))

all_data = pd.concat(raw_data).reset_index(drop=True).sort_values('adp')
adp = all_data['adp'].to_numpy()
adp = (adp - np.min(adp)) / (np.max(adp) - np.min(adp))
normalized_data = pd.DataFrame({'position': all_data['position'], 'adp': adp})
adp_by_pos = {'QB': normalized_data[normalized_data['position'] == 'QB'].reset_index(drop=True)['adp'].to_numpy(), 
              'RB': normalized_data[normalized_data['position'] == 'RB'].reset_index(drop=True)['adp'].to_numpy(), 
              'WR': normalized_data[normalized_data['position'] == 'WR'].reset_index(drop=True)['adp'].to_numpy(), 
              'TE': normalized_data[normalized_data['position'] == 'TE'].reset_index(drop=True)['adp'].to_numpy(),
              'K': normalized_data[normalized_data['position'] == 'K'].reset_index(drop=True)['adp'].to_numpy(),
              'DEF': normalized_data[normalized_data['position'] == 'DST'].reset_index(drop=True)['adp'].to_numpy()
}

np.save(os.path.join(os.getcwd(), 'cleaned_data', 'adp_data.npy'), adp_by_pos, allow_pickle=True)