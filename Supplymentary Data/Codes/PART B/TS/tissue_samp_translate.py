import pandas as pd
import os
# this code is for translate sample id to tissue
dic = {'Gene':'Gene'}
with open ('/eevee/val/jjpark/RNA_SEQ_ATLAS/three_TS_predicting/archs4_meta.txt') as f:
    lines =f.readlines()
    for line in lines:
        smp = line.split('\t')[1]
        tis = line.split('\t')[2].replace(' ','_')
        dic[smp] = tis
with open ('/eevee/val/jjpark/RNA_SEQ_ATLAS/three_TS_predicting/RENEWAL_META_MAJOR_TISSUE.tsv') as f:
    lines =f.readlines()
    for line in lines:
        smp = line.split('\t')[1]
        tis = line.split('\t')[2].replace(' ','_')
        dic[smp] = tis
with open ('./TIS_T_DROP_INTER_GTEX_PTN_GCT.tsv','w') as g:
    with open('./T_DROP_INTER_GTEX_PTN_GCT.tsv') as f:
        lines = f.readlines()
        g.write(lines[0])
        for line in lines[1:]:
            samp = line.split('\t')[0]
            etc = line.split('\t')[1:]
            g.write(dic[samp] + '\t' + '\t'.join(etc))

with open ('./TIS_T_DROP_INTER_TCGA_PTN_GCT.tsv','w') as g:
    with open('./T_DROP_INTER_TCGA_PTN_GCT.tsv') as f:
        lines = f.readlines()
        g.write(lines[0])
        for line in lines[1:]:
            samp = line.split('\t')[0]
            etc = line.split('\t')[1:]
            g.write(dic[samp] + '\t' + '\t'.join(etc))
with open ('./TIS_T_DROP_INTER_GEO_PTN_GCT.tsv','w') as g:
    with open('./T_DROP_INTER_GEO_PTN_GCT.tsv') as f:
        lines = f.readlines()
        g.write(lines[0])
        for line in lines[1:]:
            samp = line.split('\t')[0]
            etc = line.split('\t')[1:]
            g.write(dic[samp] + '\t' + '\t'.join(etc))
