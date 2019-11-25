import pandas as pd
import glob
import os

filenames = []
for val in glob.glob('*full_clones_preprocess.txt'):
    file = os.path.splitext(val)[0]
    filenames.append(file)

for filename in filenames:
    data = pd.read_csv(filename + '.txt', delimiter = '\t')
    heavy = data.loc[data['allVHitsWithScore'].str.contains('IGHV')]
    name = filename.split('_full')
    
    nona_data = heavy.fillna('')
    f = open(filename + '_heavy_chain_AA.txt', 'w')
    for index, row in nona_data.iterrows():
        f.write('>' + name[0] + '_' + str(row['cloneId']) + ' | ' + str(row['cloneCount']) + ' | ' + row['allVHitsWithScore'] + ' | ' + row['allDHitsWithScore'] + ' | ' + row['allJHitsWithScore'] + ' | ' + row['allCHitsWithScore'] + '\n' + row['full ig'] + '\n')
    f.close()
