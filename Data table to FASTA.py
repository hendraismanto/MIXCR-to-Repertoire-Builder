import pandas as pd

#import data table from Data Pre-processing.py

#convert data table to FASTA
nona_brca_19 = brca_19.fillna('')
f = open("brca_19_output.txt", "w")
for index, row in nona_brca_19.iterrows():
    f.write('>' + 'brca_19' + ' | ' + str(row['cloneId']) + ' | ' + str(row['cloneCount']) + ' | ' + row['allVHitsWithScore'] + ' | ' + row['allDHitsWithScore'] + ' | ' + row['allJHitsWithScore'] + ' | ' + row['allCHitsWithScore'] + '\n' + row['full ig'] + '\n')
f.close()
#these code still include all heavy and light chain
#need to seperate heavy from light chain
