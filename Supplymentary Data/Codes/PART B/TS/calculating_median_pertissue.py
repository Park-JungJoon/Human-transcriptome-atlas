import pandas as pd
import numpy as np
# calculating medians of tissue/gene expression
gtex = pd.read_csv('./TIS_T_DROP_INTER_GTEX_PTN_GCT.tsv', index_col = 0 , sep = '\t')
tcga = pd.read_csv('./TIS_T_DROP_INTER_TCGA_PTN_GCT.tsv', index_col = 0 , sep = '\t')
geo = pd.read_csv('./TIS_T_DROP_INTER_GEO_PTN_GCT.tsv', index_col = 0 , sep = '\t')

mean_gtex = gtex.groupby(gtex.index).mean()
mean_tcga = tcga.groupby(tcga.index).mean()
mean_geo = geo.groupby(geo.index).mean()

mean_gtex.to_csv('./MEAN_GTEX_TISSUE_GCT.tsv', sep = '\t', header = True, index = True)
mean_tcga.to_csv('./MEAN_TCGA_TISSUE_GCT.tsv', sep = '\t', header = True, index = True)
mean_geo.to_csv('./MEAN_GEO_TISSUE_GCT.tsv', sep = '\t', header = True, index = True)

#median_gtex = gtex.groupby(gtex.index).median()
#median_tcga = tcga.groupby(tcga.index).median()
#median_geo = geo.groupby(geo.index).median()

#median_gtex.to_csv('/eevee/val/jjpark/RNA_SEQ_ATLAS/three_TS_predicting/gtex/MEDIAN_GTEX_TISSUE_GCT.tsv', sep = '\t', header = True, index = True)
#median_tcga.to_csv('/eevee/val/jjpark/RNA_SEQ_ATLAS/three_TS_predicting/tcga/MEDIAN_TCGA_TISSUE_GCT.tsv', sep = '\t', header = True, index = True)
#median_geo.to_csv('/eevee/val/jjpark/RNA_SEQ_ATLAS/three_TS_predicting/geo/MEDIAN_GEO_TISSUE_GCT.tsv', sep = '\t', header = True, index = True)
