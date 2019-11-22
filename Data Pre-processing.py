import pandas as pd
import numpy as np

brca_19 = pd.read_csv('BRCA_19_full_clones.txt', delimiter = '\t')

#erase stop codon sign(_) from the last character in FR4 sequence
# start stop and step variables 
start, stop, step = 0, -1, 1
  
# slicing till last element 
brca_19['aaSeqImputedFR4seq']= brca_19['aaSeqImputedFR4'].str.slice(start, stop, step)

#merge character from all amino acid seq then make uppercase letter
brca_19['full ig'] = brca_19['aaSeqImputedFR1'].fillna('').str.cat(brca_19[['aaSeqImputedCDR1','aaSeqImputedFR2', 'aaSeqImputedCDR2', 'aaSeqImputedFR3', 'aaSeqImputedCDR3', 'aaSeqImputedFR4seq']].fillna(''),sep="").str.upper()

#drop row containing NA in amino acid seq
brca_19.dropna(subset = ['aaSeqImputedFR1', 'aaSeqImputedCDR1', 'aaSeqImputedFR2', 'aaSeqImputedCDR2', 'aaSeqImputedFR3', 'aaSeqImputedFR4'], inplace = True)

#nonfunctioning IG name list
nonfunc_ig = ['IGHV1-12', 'IGHV1-14', 'IGHV1-17', 'IGHV1-67', 'IGHV1-68', 'IGHV2-10', 'IGHV3-19', 
          'IGHV3-22', 'IGHV3-25', 'IGHV3-29', 'IGHV3-30-2', 'IGHV3-30-22', 'IGHV3-30-33', 'IGHV3-30-42', 
           'IGHV3-30-52', 'IGHV3-32', 'IGHV3-33-2', 'IGHV3-36', 'IGHV3-37', 'IGHV3-41', 'IGHV3-42', 'IGHV3-42D', 
             'IGHV3-47', 'IGHV3-50', 'IGHV3-52', 'IGHV3-54', 'IGHV3-57', 'IGHV3-6', 'IGHV3-60', 'IGHV3-62', 'IGHV3-63', 
             'IGHV3-65', 'IGHV3-69-1', 'IGHV3-71', 'IGHV3-75', 'IGHV3-76', 'IGHV3-79', 'IGHV4-55', 'IGHV4-80', 'IGHV5-78', 
             'IGHV7-27', 'IGHV7-34-1', 'IGHV7-40', 'IGHV7-40D', 'IGHV7-56', 'IGHV8-51-1', 
             'IGKV1-13', 'IGKV1-22', 'IGKV1-32', 'IGKV1-35', 'IGKV2-10', 'IGKV2-14', 'IGKV2-18', 'IGKV2-19', 'IGKV2-23', 
             'IGKV2-26', 'IGKV2-29', 'IGKV2-36', 'IGKV2-38', 'IGKV2-4', 'IGKV3-25', 'IGKV3-31', 'IGKV3-34', 'IGKV7-3', 
             'IGLV1-41', 'IGLV1-62', 'IGLV1-67', 'IGLV2-28', 'IGLV2-34', 'IGLV2-5', 'IGLV3-13', 'IGLV3-15', 'IGLV3-17', 
              'IGLV3-2', 'IGLV3-24', 'IGLV3-26', 'IGLV3-29', 'IGLV3-30', 'IGLV3-31', 'IGLV3-4', 'IGLV3-6', 'IGLV3-7', 
              'IGLV5-48', 'IGLV7-35',
             'IGHV1-38-4', 'IGHV3-16', 'IGHV3-25', 'IGHV3-35', 'IGHV3-38', 'IGHV3-38-3', 'IGHV7-81', 'IGKV1-37', 
             'IGKV1D-37', 'IGKV1D-42', 'IGKV2D-24', 'IGKV3-7', 'IGKV3D-20', 'IGKV6D-41', 'IGLC1', 'IGLJ4', 'IGLJ5',
              'IGLV1-50', 'IGLV11-55', 'IGLV2-33', 'IGLV3-32']

#erase IG seq which nonfunctioning
test_list = nonfunc_ig

#empty list for appending value
lis = []

# checking if string contains list element 
for test_string in brca_19['allVHitsWithScore']:
    res = any(ele in test_string[0:11] for ele in test_list)
    lis.append(res)

#invert value
flipped_lis = np.invert(lis)

#erase nonfunctioning IG from data
clear_brca_19 = brca_19[flipped_lis]
