# this code is parsing for gff3 file of human genome, and get exon count of gene 
from collections import defaultdict
exon_countdic = defaultdict(int)
with open ('gencode.v43.annotation.gff3') as f:
    lines = f.readlines()
    gene = ''
    for line in lines:
        if line.startswith('#'):
            continue
        source = line.split('\t')[2]
        metadata = line.split('\t')[8]
        if '_PAR_Y' in  metadata.split(';')[1]:
            continue
        ensg = metadata.split(';')[1].split('.')[0].replace('gene_id=','')
        gtype = metadata.split(';')[2].replace('gene_type=','')
        print(ensg,gtype)
        if gtype != 'protein_coding':
            continue
        if source == 'gene':
            gene = ensg
        if source == 'exon':
            exon_countdic[gene] += 1

for k,v in exon_countdic.items():
    print(k + '\t' + str(v))
