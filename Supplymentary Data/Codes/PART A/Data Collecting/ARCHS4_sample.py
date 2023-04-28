# 이전의 ARCHS4_h5_sample_extracting.R 에서 추출한 'archs4_meta.txt'에서 필요한 sample만 parsing함.
import pandas as pd
arc = {}
with open ('/eevee/val/jjpark/archs4/beta_Ver/archs4_meta.txt') as f:
    lines =f.readlines()
    for line in lines:
        smp = line.split('\t')[1]
        tis = line.split('\t')[2]
        arc[smp] = tis
using = ['Bladder','Brain','Kidney','Spleen','Liver','Blood','Uterus',
        'Lung','Breast','Small Intestine','Thyroid','Stomach','Testis','Skin','Prostate','Pituitary','Adipose Tissue',
        'Vagina','Blood Vessel','Adrenal Gland','Pancreas','Heart','Esophagus','Large intestine',
        'Ovary','Thymus','Muscle']
rmv = []

with open ('/eevee/val/jjpark/atlas_getmm/META_MERGED_COMPLETE.tsv') as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.rstrip()
        db = line.split('\t')[0]
        if db == 'ENCODE':
            continue
        samp = line.split('\t')[1]
        tiss = line.split('\t')[2]
        stiss = line.split('\t')[3]
        if tiss not in using:
            if stiss == 'Lymph nodes':
                continue
            elif stiss == 'Nerve - Tibial':
                continue
            rmv.append(samp)
df= pd.read_csv('MERGED_PTN_CODING_LIB_SIZE_NORMED_GCT.tsv', delimiter='\t', index_col=0)
df = df.drop(rmv, axis=1)
df.to_csv('DROP_MERGED_PTN_CODING_LIB_SIZE_NORMED_GCT.tsv', sep='\t')

