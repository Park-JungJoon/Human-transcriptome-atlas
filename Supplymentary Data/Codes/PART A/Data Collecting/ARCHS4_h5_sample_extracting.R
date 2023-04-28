# This code is written for selecting samples which needed for research
# Output of code is "merged_archs4_infos"

library("rhdf5")    # can be installed using Bioconductor


destination_file = "/eevee/val/jjpark/archs4/beta_Ver/archs4_gene_human_v2.1.2.h5"
extracted_expression_file = "ARCHS4_GENE_COUNT_TABLE_RAW.tsv"

# Check if gene expression file was already downloaded, if not in current directory download file form repository
setwd("/eevee/val/jjpark/archs4/beta_Ver")

usg = read.csv('/eevee/val/jjpark/archs4/beta_Ver/archs4_meta.txt',sep = '\t',header = FALSE) 
# Selected samples to be extracted
samp = usg$V2
# Retrieve information from compressed data
samples = h5read(destination_file, "meta/samples/geo_accession")
genes = h5read(destination_file, "meta/genes/gene_symbol")

# Identify columns to be extracted
sample_locations = which(samples %in% samp)

# extract gene expression from compressed data
expression = t(h5read(destination_file, "data/expression", index=list(sample_locations, 1:length(genes))))
H5close()
rownames(expression) = genes
colnames(expression) = samples[sample_locations]

# Print file
write.table(expression, file=extracted_expression_file, sep="\t", quote=FALSE, col.names=NA)
print(paste0("Expression file was created at ", getwd(), "/", extracted_expression_file))
