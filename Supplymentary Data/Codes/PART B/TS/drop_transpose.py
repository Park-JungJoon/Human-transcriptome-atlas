import pandas as pd
import os
dic = {'Gene':'Gene'}
#metadata reading
with open ('/eevee/val/jjpark/RNA_SEQ_ATLAS/three_TS_predicting/archs4_meta.txt') as f:
    lines =f.readlines()
    for line in lines:
        smp = line.split('\t')[1]
        tis = line.split('\t')[2]
        dic[smp] = tis
with open ('/eevee/val/jjpark/RNA_SEQ_ATLAS/three_TS_predicting/RENEWAL_META_MAJOR_TISSUE.tsv') as f:
    lines =f.readlines()
    for line in lines:
        smp = line.split('\t')[1]
        tis = line.split('\t')[2]
        dic[smp] = tis
#dic의 smp에는 정제된 tissue만 있음
rmv = []
with open ('/eevee/val/jjpark/RNA_SEQ_ATLAS/one_pklformat_divide/gtextcga_header.txt') as f:
    lines = f.readlines()
    samps = lines[0].rstrip().split('\t')
    for i in samps:
        if i not in dic.keys():
            rmv.append(i)

gtexrmv = []
tcgarmv = []
for i in rmv:
    if i.startswith('GTEX-'):
        gtexrmv.append(i)
    else:
        tcgarmv.append(i)

gtexdf = pd.read_csv('./INTER_GTEX_PTN_GCT.tsv', delimiter='\t', index_col=0)
gtexdf_drp = gtexdf.drop(gtexrmv, axis=1)
gtexdf_drp_t = gtexdf_drp.transpose()
gtexdf_drp_t.to_csv('./T_DROP_INTER_GTEX_PTN_GCT.tsv',index = True, header = True, sep = '\t')

tcgadf = pd.read_csv('./INTER_TCGA_PTN_GCT.tsv', delimiter='\t', index_col=0)
tcgadf_drp = tcgadf.drop(tcgarmv, axis=1)
tcgadf_drp_t = tcgadf_drp.transpose()
tcgadf_drp_t.to_csv('./T_DROP_INTER_TCGA_PTN_GCT.tsv',index = True, header = True, sep = '\t')

geodf = pd.read_csv('INTER_GEO_PTN_GCT.tsv', delimiter='\t', index_col=0)
geodf_t = geodf.transpose()
geodf_t.to_csv('./T_DROP_INTER_GEO_PTN_GCT.tsv',index = True, header = True, sep = '\t')
