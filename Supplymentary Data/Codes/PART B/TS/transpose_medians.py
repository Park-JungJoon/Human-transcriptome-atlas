import pandas as pd
# transpose median file for calculating TAU
gtex = pd.read_csv('./MEAN_GTEX_TISSUE_GCT.tsv', delimiter = '\t', index_col = 0)
tcga = pd.read_csv('./MEAN_TCGA_TISSUE_GCT.tsv', delimiter = '\t', index_col = 0)
geo = pd.read_csv('./MEAN_GEO_TISSUE_GCT.tsv', delimiter = '\t', index_col = 0)
gtex_t = gtex.transpose()
tcga_t = tcga.transpose()
geo_t = geo.transpose()

gtex_t.to_csv('./T_MEAN_GTEX_TISSUE_GCT.tsv', index = True, header = True, sep = '\t')
tcga_t.to_csv('./T_MEAN_TCGA_TISSUE_GCT.tsv', index = True, header = True, sep = '\t')
geo_t.to_csv('./T_MEAN_GEO_TISSUE_GCT.tsv', index = True, header = True, sep = '\t')

