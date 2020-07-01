import pandas as pd

def import_to_fasta(cohort, filename):
    data = pd.read_csv(filename + '.txt', delimiter='\t')
    #erase stop codon sign(_) from the last character in FR4 sequence
    # start stop and step variables
    start, stop, step = 0, -1, 1
    
    # slicing last element
    data['aaSeqImputedFR4']= data['aaSeqImputedFR4'].str.slice(start, stop, step)
    
    #merge character from all amino acid seq then make uppercase letter
    data['full ig'] = data['aaSeqImputedFR1'].fillna('').str.cat(data[['aaSeqImputedCDR1','aaSeqImputedFR2', 
                                                                       'aaSeqImputedCDR2', 'aaSeqImputedFR3', 
                                                                       'aaSeqImputedCDR3', 'aaSeqImputedFR4']].fillna('')).str.upper()
    
    #drop row containing NA in amino acid seq
    data.dropna(subset = ['aaSeqImputedFR1', 'aaSeqImputedCDR1', 
                          'aaSeqImputedFR2', 'aaSeqImputedCDR2', 
                          'aaSeqImputedFR3', 'aaSeqImputedFR4'], inplace = True)
    
    with open(filename + '.fasta', 'w') as f:
        for index, row in data.iterrows():
            f.write('>' + cohort + '_' + filename + '_' + str(row['cloneId']) + '\n' + row['full ig'] + '\n')
            

def import_pseudo_to_fasta(cohort, filename):
    data = pd.read_csv(filename + '.txt', delimiter='\t')
    
    #merge character from all amino acid seq then make uppercase letter
    data['pseudo ig'] = data['aaSeqImputedCDR1'].fillna('').str.cat(data[['aaSeqImputedCDR2', 'aaSeqImputedCDR3']].fillna('')).str.upper()
    
    #drop row containing NA in amino acid seq
    data.dropna(subset = ['aaSeqImputedFR1', 'aaSeqImputedCDR1', 
                         'aaSeqImputedFR2', 'aaSeqImputedCDR2', 'aaSeqImputedFR3', 'aaSeqImputedFR4'], inplace = True)
    with open(filename + '.fasta', 'w') as f:
        for index, row in data.iterrows():
            f.write('>' + cohort + '_' + filename + '_' + str(row['cloneId']) + '\n' + row['pseudo ig'] + '\n')
            
