# 
library(ggplot2)
library(dplyr)

# Load data
tcga = read.table("/eevee/val/jjpark/RNA_SEQ_ATLAS/three_TS_predicting/re_work_mean/T_MEAN_TCGA_TISSUE_GCT.tsv", header = TRUE, sep = '\t',row.names = 1)
gtex = read.table("/eevee/val/jjpark/RNA_SEQ_ATLAS/three_TS_predicting/re_work_mean/T_MEAN_GTEX_TISSUE_GCT.tsv", header = TRUE, sep = '\t',row.names = 1)
geo = read.table("/eevee/val/jjpark/RNA_SEQ_ATLAS/three_TS_predicting/re_work_mean/T_MEAN_GEO_TISSUE_GCT.tsv", header = TRUE, sep = '\t',row.names = 1)
genetype <-read.table("/eevee/val/jjpark/RNA_SEQ_ATLAS/four_intron/genesfor_R.txt", header = TRUE, sep = '\t',row.names = 1)
#merging
tcga <- merge(tcga, genetype, by="row.names")
tcga <- as.data.frame(tcga)
row.names(tcga) <- tcga$Row.names
tcga <- subset(tcga, select = -Row.names)
tcga.list <- tidyr::gather(tcga, "tissue", "value",-Type)

tcga_boxplot <- ggplot(tcga.list, aes(x=tissue, y=value, color=Type)) +
  geom_boxplot(outlier.shape=NA) + scale_y_log10() +
  xlab("TCGA_Tissue") + ylab("Expression") + ggtitle("TCGA SEG/MEG Expression Distribution") + theme_bw()+
  theme(axis.text.x=element_text(size = 18,angle=45, hjust=1)) + theme(axis.text.y=element_text(size = 18)) +
  theme(axis.title.x=element_text(size = 22)) + theme(axis.title.y=element_text(size = 22))+
  theme(plot.title=element_text(size=27))

tcga_jitter <- ggplot(tcga.list, aes(x=tissue, y=value, color=Type)) +
  geom_boxplot(outlier.shape=NA) +geom_point(alpha=0.1,position=position_jitterdodge())+ scale_y_log10()+
  xlab("TCGA_Tissue") + ylab("Expression") + ggtitle("TCGA SEG/MEG Expression Distribution") + theme_bw()+
  theme(axis.text.x=element_text(size = 18,angle=45, hjust=1)) + theme(axis.text.y=element_text(size = 18)) +
  theme(axis.title.x=element_text(size = 22)) + theme(axis.title.y=element_text(size = 22))+
  theme(plot.title=element_text(size=27))

ggsave(tcga_boxplot, filename = 'tcga_boxplot.png', path = '/eevee/val/jjpark/RNA_SEQ_ATLAS/four_intron/', width = 8000, height = 2200, units = "px")
ggsave(tcga_jitter, filename = 'tcga_jitter.png', path = '/eevee/val/jjpark/RNA_SEQ_ATLAS/four_intron/', width = 8000, height = 2200, units = "px")

#gtex
gtex <- merge(gtex, genetype, by="row.names")
gtex <- as.data.frame(gtex)
row.names(gtex) <- gtex$Row.names
gtex <- subset(gtex, select = -Row.names)
gtex.list <- tidyr::gather(gtex, "tissue", "value",-Type)

gtex_boxplot <- ggplot(gtex.list, aes(x=tissue, y=value, color=Type)) +
  geom_boxplot(outlier.shape=NA) + scale_y_log10()+
  xlab("GTEX_Tissue") + ylab("Expression") + ggtitle("GTEX SEG/MEG Expression Distribution") + theme_bw()+
  theme(axis.text.x=element_text(size = 18,angle=45, hjust=1)) + theme(axis.text.y=element_text(size = 18)) +
  theme(axis.title.x=element_text(size = 22)) + theme(axis.title.y=element_text(size = 22))+
  theme(plot.title=element_text(size=27))

gtex_jitter <- ggplot(gtex.list, aes(x=tissue, y=value, color=Type)) +
  geom_boxplot(outlier.shape=NA) +geom_point(alpha=0.1,position=position_jitterdodge())+ scale_y_log10()+
  xlab("GTEX_Tissue") + ylab("Expression") + ggtitle("GTEX SEG/MEG Expression Distribution") + theme_bw()+
  theme(axis.text.x=element_text(size = 18,angle=45, hjust=1)) + theme(axis.text.y=element_text(size = 18)) +
  theme(axis.title.x=element_text(size = 22)) + theme(axis.title.y=element_text(size = 22))+
  theme(plot.title=element_text(size=27))

ggsave(gtex_boxplot, filename = 'gtex_boxplot.png', path = '/eevee/val/jjpark/RNA_SEQ_ATLAS/four_intron/', width = 8000, height = 2200, units = "px")
ggsave(gtex_jitter, filename = 'gtex_jitter.png', path = '/eevee/val/jjpark/RNA_SEQ_ATLAS/four_intron/', width = 8000, height = 2200, units = "px")

#geo
geo <- merge(geo, genetype, by="row.names")
geo <- as.data.frame(geo)
row.names(geo) <- geo$Row.names
geo <- subset(geo, select = -Row.names)
geo.list <- tidyr::gather(geo, "tissue", "value",-Type)

geo_boxplot <- ggplot(geo.list, aes(x=tissue, y=value, color=Type)) +
  geom_boxplot(outlier.shape=NA) + scale_y_log10()+
  xlab("GEO_Tissue") + ylab("Expression") + ggtitle("GEO SEG/MEG Expression Distribution") + theme_bw()+
  theme(axis.text.x=element_text(size = 18,angle=45, hjust=1)) + theme(axis.text.y=element_text(size = 18)) +
  theme(axis.title.x=element_text(size = 22)) + theme(axis.title.y=element_text(size = 22))+
  theme(plot.title=element_text(size=27))

geo_jitter <- ggplot(geo.list, aes(x=tissue, y=value, color=Type)) +
  geom_boxplot(outlier.shape=NA) +geom_point(alpha=0.1,position=position_jitterdodge())+ scale_y_log10()+
  xlab("GEO_Tissue") + ylab("Expression") + ggtitle("GEO SEG/MEG Expression Distribution") + theme_bw()+
  theme(axis.text.x=element_text(size = 18,angle=45, hjust=1)) + theme(axis.text.y=element_text(size = 18)) +
  theme(axis.title.x=element_text(size = 22)) + theme(axis.title.y=element_text(size = 22))+
  theme(plot.title=element_text(size=27))

ggsave(geo_boxplot, filename = 'geo_boxplot.png', path = '/eevee/val/jjpark/RNA_SEQ_ATLAS/four_intron/', width = 8000, height = 2200, units = "px")
ggsave(geo_jitter, filename = 'geo_jitter.png', path = '/eevee/val/jjpark/RNA_SEQ_ATLAS/four_intron/', width = 8000, height = 2200, units = "px")

