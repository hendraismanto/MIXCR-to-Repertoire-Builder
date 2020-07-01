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
            
def main():

    parser = argparse.ArgumentParser(description = 'change MiXCR output into fasta for human and mouse aa/nt')

    parser.add_argument('-i', dest = 'input_file', help = 'Input file (tsv)')
    parser.add_argument('-s', dest = 'species', default = 'human', help = 'Species (human or mouse) default = human')
    parser.add_argument('-t', dest = 'type_job', default = 'all', help = 'type of job (aa+nt or aa or nt), default = aa&nt')
    parser.add_argument('-o', dest = 'out_dir', help = 'directory of output')
    parser.add_argument('-p', dest = 'pseudo_aa', default = None, help = 'generate only pseudo aa seq (keyword = pseudo)')
    args = parser.parse_args()
    
    os.makedirs(args.out_dir, exist_ok=True)

    filename = os.path.abspath(args.input_file)
    filename_ = os.path.basename(filename)
    filename_only, file_extension = os.path.splitext(filename_)
    

    logging.basicConfig(filename=os.path.join(args.out_dir, "out.log"), level=logging.INFO)
    logger = logging.getLogger()
    sh = logging.StreamHandler()
    logger.addHandler(sh)
    
    logging.info("species: {}".format(args.species))
    logging.info('type of job: {}'.format(args.type_job))
    logging.info("out_dir: {}".format(os.path.abspath(args.out_dir)))
    
