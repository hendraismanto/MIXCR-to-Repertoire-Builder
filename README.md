# MIXCR-to-FASTA
make MiXCR output into FASTA that used in model building of Repertoire Builder and clustering in CD-HIT

Dependencies:
Pyhton 3.7 and above
Pandas (0.25.3)

usage:
MiXCR_to_fasta.py [-h] [-i INPUT_FILE] [-s SPECIES] [-t TYPE_JOB] [-o OUT_DIR] [-p PSEUDO_AA]

optional arguments:
  -h, --help  show this help message and exit
  -i INPUT_FILE Inputfile (in tsv format, either in tsv, csv, or txt extension)
  -s SPECIES    Species (human or mouse) default = human
  -t TYPE_JOB   Type of job (aa+nt, aa-only, or nt-only) default = aa&nt
  -o OUT_DIR    Output Directory
  -p PSEUDO_AA  Generate Pseudo aa seq-only (CDR1 + CDR2 + CDR3) you must input pseudo as argument
  
  
