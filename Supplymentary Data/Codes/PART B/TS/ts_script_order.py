# this is order of codes for TS finding
import os 
os.system('python drop_transpose.py')
os.system('python tissue_samp_translate.py')
os.system('python calculating_median_pertissue.py')
os.system('python transpose_medians.py')
os.system('python tauwriting.py')
os.system('python ts_finding.py')
