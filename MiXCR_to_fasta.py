import pandas as pd
import os
import sys
import time
import argparse
import logging

nonfunc_ig_human = ['IGHV1-12', 'IGHV1-14', 'IGHV1-17', 'IGHV1-67', 'IGHV1-68', 'IGHV2-10', 'IGHV3-19', 
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

nonfunc_ig_mouse = ['IGHD5-1', 'IGHD5-2', 'IGHD5-3', 'IGHD5-4', 'IGHD5-5', 'IGHD5-6', 'IGHJ3', 'IGHV1-1', 'IGHV1-10',
            'IGHV1-13', 'IGHV1-16', 'IGHV1-17', 'IGHV1-17-1', 'IGHV1-19-1', 'IGHV1-2', 'IGHV1-21', 'IGHV1-21-1', 'IGHV1-23',
            'IGHV1-24', 'IGHV1-25', 'IGHV1-27', 'IGHV1-28', 'IGHV1-29', 'IGHV1-3', 'IGHV1-30', 'IGHV1-32', 'IGHV1-33', 'IGHV1-35',
            'IGHV1-38', 'IGHV1-40', 'IGHV1-41', 'IGHV1-44', 'IGHV1-45', 'IGHV1-46', 'IGHV1-48', 'IGHV1-51', 'IGHV1-57', 'IGHV1-6', 
            'IGHV1-60', 'IGHV1-62', 'IGHV1-62-3', 'IGHV1-65', 'IGHV1-67', 'IGHV1-68', 'IGHV1-70', 'IGHV1-73', 'IGHV1-79', 'IGHV1-8',
            'IGHV1-83', 'IGHV1-86', 'IGHV10-2', 'IGHV10-4', 'IGHV12-1', 'IGHV12-1-2', 'IGHV12-2', 'IGHV12-2-1', 'IGHV13-1', 'IGHV15-1',
            'IGHV16-1', 'IGHV2-1', 'IGHV2-2-1', 'IGHV3-7', 'IGHV5-1', 'IGHV5-10', 'IGHV5-10-1', 'IGHV5-10-2', 'IGHV5-11', 'IGHV5-11-1',
            'IGHV5-11-2', 'IGHV5-12-3', 'IGHV5-13', 'IGHV5-13-1', 'IGHV5-18', 'IGHV5-19', 'IGHV5-21', 'IGHV5-3', 'IGHV5-5', 'IGHV5-5-1',
            'IGHV5-7', 'IGHV5-7-1', 'IGHV5-7-2', 'IGHV5-7-3', 'IGHV5-7-4', 'IGHV5-7-5', 'IGHV5-7-6', 'IGHV5-8', 'IGHV5-8-1', 'IGHV5-8-2',
            'IGHV5-8-3', 'IGHV6-1', 'IGHV6-1-1', 'IGHV6-2', 'IGHV6-5', 'IGHV7-2', 'IGHV8-1', 'IGHV8-10', 'IGHV8-13', 'IGHV8-14', 'IGHV8-15',
            'IGHV8-16', 'IGHV8-2', 'IGHV8-3', 'IGHV8-4', 'IGHV8-5', 'IGHV8-7', 'IGHV8-8-1', 'IGHV8-9', 'IGKJ3', 'IGKV1-108', 'IGKV1-115', 
            'IGKV1-131', 'IGKV1-136', 'IGKV1-35', 'IGKV11-106', 'IGKV11-114', 'IGKV11-118', 'IGKV12-40', 'IGKV12-42', 'IGKV12-47',
            'IGKV12-49', 'IGKV12-66', 'IGKV12-67', 'IGKV13-64', 'IGKV13-76', 'IGKV13-82', 'IGKV13-87', 'IGKV14-130', 'IGKV15-101', 'IGKV15-102', 
            'IGKV15-103', 'IGKV15-97', 'IGKV17-134', 'IGKV2-105', 'IGKV2-107', 'IGKV2-113', 'IGKV2-116', 'IGKV3-11', 'IGKV3-6', 'IGKV3-8', 'IGKV4-52',
            'IGKV4-54', 'IGKV4-56', 'IGKV4-60', 'IGKV4-62', 'IGKV4-65', 'IGKV4-75', 'IGKV4-77', 'IGKV4-83', 'IGKV6-13', 'IGKV8-18', 'IGKV8-22', 
            'IGKV8-31', 'IGKV9-119', 'IGKV9-128', 'IGKV9-129', 'IGLC4', 'IGLJ4', 'IGLV4', 'IGLV5', 'IGLV6', 'IGLV7', 'IGLV8']

def preprocess_nt(data, database):

    #merge character from all amino acid seq then make uppercase letter
    data['full ig'] = data['nSeqImputedFR1'].fillna('').str.cat(data[['nSeqImputedCDR1','nSeqImputedFR2', 
                                                                            'nSeqImputedCDR2', 'nSeqImputedFR3', 
                                                                            'nSeqImputedCDR3', 'nSeqImputedFR4']].fillna('')).str.upper()
    
    #drop row containing NA in nucleotide seq
    data.dropna(subset = ['nSeqImputedFR1', 'nSeqImputedCDR1', 
                         'nSeqImputedFR2', 'nSeqImputedCDR2', 'nSeqImputedFR3', 'nSeqImputedFR4'], inplace = True)
    
    #erase IG seq which nonfunctioning
    test_list = database
    
    #empty list for appending value
    lis = []
    
    # checking if string contains list element
    for test_string in data['allVHitsWithScore']:
        res = any(ele in test_string[0:11] for ele in test_list)
        lis.append(not res)
        
    #erase nonfunctioning IG from data
    N_clear = data[lis]
    
    #erase full ig containing out-of-frame indels (* and _)
    clear_data = N_clear[~N_clear['full ig'].str.contains('\*|_')]

    
    return clear_data

def preprocess_aa(data, database):

    #erase stop codon sign(_) from the last character in FR4 sequence
    # start stop and step variables
    start, stop, step = 0, -1, 1
    
    # slicing till last element
    data['aaSeqImputedFR4']= data['aaSeqImputedFR4'].str.slice(start, stop, step)
    
    #merge character from all amino acid seq then make uppercase letter
    data['full ig'] = data['aaSeqImputedFR1'].fillna('').str.cat(data[['aaSeqImputedCDR1','aaSeqImputedFR2', 
                                                                            'aaSeqImputedCDR2', 'aaSeqImputedFR3', 
                                                                            'aaSeqImputedCDR3', 'aaSeqImputedFR4']].fillna('')).str.upper()
    
    #drop row containing NA in amino acid seq
    data.dropna(subset = ['aaSeqImputedFR1', 'aaSeqImputedCDR1', 
                         'aaSeqImputedFR2', 'aaSeqImputedCDR2', 'aaSeqImputedFR3', 'aaSeqImputedFR4'], inplace = True)
    
    #erase IG seq which nonfunctioning
    test_list = database
    
    #empty list for appending value
    lis = []
    
    # checking if string contains list element
    for test_string in data['allVHitsWithScore']:
        res = any(ele in test_string[0:11] for ele in test_list)
        lis.append(not res)
        
    #erase nonfunctioning IG from data
    N_clear = data[lis]
    
    #erase full ig containing out-of-frame indels (* and _)
    clear_data = N_clear[~N_clear['full ig'].str.contains('\*|_')]

    
    return clear_data

def preprocess_pseudo_aa(data, database):
    
    #merge character from all amino acid seq then make uppercase letter
    data['full ig'] = data['aaSeqImputedCDR1'].fillna('').str.cat(data[['aaSeqImputedCDR2', 'aaSeqImputedCDR3']].fillna('')).str.upper()
    
    #drop row containing NA in amino acid seq
    data.dropna(subset = ['aaSeqImputedFR1', 'aaSeqImputedCDR1', 
                         'aaSeqImputedFR2', 'aaSeqImputedCDR2', 'aaSeqImputedFR3', 'aaSeqImputedFR4'], inplace = True)
    
    #erase IG seq which nonfunctioning
    test_list = database
    
    #empty list for appending value
    lis = []
    
    # checking if string contains list element
    for test_string in data['allVHitsWithScore']:
        res = any(ele in test_string[0:11] for ele in test_list)
        lis.append(not res)
        
    #erase nonfunctioning IG from data
    N_clear = data[lis]
    
    #erase full ig containing out-of-frame indels (* and _)
    clear_data = N_clear[~N_clear['full ig'].str.contains('\*|_')]

    return clear_data

def data_exporter_heavy(data, filename_, filename_only, out_dir, suffix):
    heavy = data.loc[data['allVHitsWithScore'].str.contains('IGHV')]
    nona_data_h = heavy.fillna('')
                    
    if nona_data_h.empty:
        raise Exception('No heavy chain found!')
    else:
        f = open(os.path.join(out_dir, filename_only + suffix), 'w')
        for index, row in nona_data_h.iterrows():
            f.write('>' + filename_only + '_' + str(row['cloneId']) + '\n' + row['full ig'] + '\n')
        f.close()

def data_exporter_light(data, filename_, filename_only, out_dir, suffix):
    light = data.loc[data['allVHitsWithScore'].str.contains('IGKV |IGLV')]
    nona_data_l = light.fillna('')
                    
    if nona_data_l.empty:
        raise Exception('No light chain found!')
    else:
        f = open(os.path.join(out_dir, filename_only + suffix), 'w')
        for index, row in nona_data_l.iterrows():
            f.write('>' + filename_only + '_' + str(row['cloneId']) + '\n' + row['full ig'] + '\n')
        f.close()

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

    reader = pd.read_csv(filename, delimiter = '\t')

    if args.pseudo_aa == 'pseudo':
        if args.species == 'mouse':
            data = preprocess_pseudo_aa(reader, nonfunc_ig_mouse)
            print('processing mouse pseudo aa')
       
            data_exporter_heavy(data, filename_, filename_only, args.out_dir, '_heavy_chain_pseudo_aa.fa')

            data_exporter_light(data, filename_, filename_only, args.out_dir, '_light_chain_pseudo_aa.fa')

        else:
            data = preprocess_pseudo_aa(reader, nonfunc_ig_human)
            print('processing human pseudo aa')

            data_exporter_heavy(data, filename_, filename_only, args.out_dir, '_heavy_chain_pseudo_aa.fa')

            data_exporter_light(data, filename_, filename_only, args.out_dir, '_light_chain_pseudo_aa.fa')

    elif args.pseudo_aa == None:
        if reader.empty is False:
            if args.species == 'mouse':
                if args.type_job == 'aa':
                    data = preprocess_aa(reader, nonfunc_ig_mouse)
                    print('processing mouse aa...')
                    
                    data_exporter_heavy(data, filename_, filename_only, args.out_dir, '_heavy_chain_aa.fa')
                    
                    data_exporter_light(data, filename_, filename_only, args.out_dir, '_light_chain_aa.fa')

                elif args.type_job == 'nt':
                    data = preprocess_nt(reader, nonfunc_ig_mouse)
                    print('processing mouse nt...')
                    
                    data_exporter_heavy(data, filename_, filename_only, args.out_dir, '_heavy_chain_nt.fa')
                    
                    data_exporter_light(data, filename_, filename_only, args.out_dir, '_light_chain_nt.fa')
                
                else:
                    data = preprocess_aa(reader, nonfunc_ig_mouse)
                    print('processing mouse aa...')
                    
                    data_exporter_heavy(data, filename_, filename_only, args.out_dir, '_heavy_chain_aa.fa')
                    
                    data_exporter_light(data, filename_, filename_only, args.out_dir, '_light_chain_aa.fa')

                    data = preprocess_nt(reader, nonfunc_ig_mouse)
                    print('processing mouse nt...')

                    data_exporter_heavy(data, filename_, filename_only, args.out_dir, '_heavy_chain_nt.fa')
                    
                    data_exporter_light(data, filename_, filename_only, args.out_dir, '_light_chain_nt.fa')
                
            else:
                if args.type_job == 'aa':
                    data = preprocess_aa(reader, nonfunc_ig_human)
                    print('processing human aa...')
                    
                    data_exporter_heavy(data, filename_, filename_only, args.out_dir, '_heavy_chain_aa.fa')
                    
                    data_exporter_light(data, filename_, filename_only, args.out_dir, '_light_chain_aa.fa')

                elif args.type_job == 'nt':
                    data = preprocess_nt(reader, nonfunc_ig_human)
                    print('processing human nt...')
                    
                    data_exporter_heavy(data, filename_, filename_only, args.out_dir, '_heavy_chain_nt.fa')
                    
                    data_exporter_light(data, filename_, filename_only, args.out_dir, '_light_chain_nt.fa')

                else:
                    data = preprocess_aa(reader, nonfunc_ig_human)
                    print('processing human aa...')
                    
                    data_exporter_heavy(data, filename_, filename_only, args.out_dir, '_heavy_chain_aa.fa')
                    
                    data_exporter_light(data, filename_, filename_only, args.out_dir, '_light_chain_aa.fa')

                    data = preprocess_nt(reader, nonfunc_ig_human)
                    print('processing human nt...')
                    
                    data_exporter_heavy(data, filename_, filename_only, args.out_dir, '_heavy_chain_nt.fa')
                    
                    data_exporter_light(data, filename_, filename_only, args.out_dir, '_light_chain_nt.fa')
        else:
            print('file empty!!')
            sys.exit()
    else:
        print('you should write "pseudo" after -p argument')

if __name__ == '__main__':
    start_time = time.time()
    main()

    print(("Done. Total run time: %s seconds" %(time.time() - start_time)))

