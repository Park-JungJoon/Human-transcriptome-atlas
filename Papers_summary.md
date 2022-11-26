# Papers Summary for Reasearch
### 1. Atlas of RNA sequencing profiles for normal human tissues [link](https://www.nature.com/articles/s41597-019-0043-4)
  - Data Source
    + 142 solid tissue samples representing 20 organs (post-mortem human healthy donors, who had dided in road accident, no later than 36 hours after death.)
    + Blood sample from 17 healthy donors.
    + TCGA(625 samples), ENCODE polyA RNA-seq, ENCODE-total RNA-seq (Sum of ENCODE data 38 samples) data for comparison.
  - Method
    + RNA extraction & sequencing 
    + Alignment with STAR
    + Hierachical clustering by tissue, using R ward.D2, making dendrogram
    + Validation of data by mix with other database's data, Whether clustering is subject to issue or database.
  - Review
    + 해당 연구는 data handling보다, raw sample의 채집부터, sequencing 전반을 상대적으로 작은 크기의 dataset을 만들었다.(142 samples)
    + 이에 따라, hierachical clustering을 통한 dendrogram의 사용법은 적용할만하나, 다른 점은 참고하기에 어려움이 있다.

<br>

### 2. Unifying cancer and normal RNA sequencing data from different sources [link](https://www.nature.com/articles/sdata201861)
  - Data Source 
    + GTEx (2,790 samples), TCGA normal (701 samples), TCGA tumor (6,875 samples), Total (10,366 samples)
    + GTEx samples was classified into organizations.
    + TCGA samples was classified into cancer type.
  - Method 
    + Data collecting from GTEx (SRA format), TCGA (tar.gz format). Using FASTQ raw data. 
    + Alignment by STAR
    + Quality Control by mRIN (filtering degradated RNA), RseQC. 831 samples filtered because of 5' degradation
    + Quantification by RSEM, FeatureCounts. (FPKM)
    + Batch effect correctiorn (ComBat;SVAseq)
  - Review
    + Processed Gene Count Table 사용하지 않음. FASTQ 부터 RNA-seq data analysis pipeline을 사용함.
    + GTEx와 TCGA를 사용. GEO 는 사용대상에서 벗어남. 
    + Batch effect를 computationally correcting하는 과정을 차용하기 좋아보임. 
  
### 3. Massive mining of publicly available RNA-seq data from human and mouse [link](https://www.nature.com/articles/s41467-018-03751-6) [ARCHS4](https://maayanlab.cloud/archs4/)
  - Data source
    + NCBI의 GEO/SRA data set. Human 84,863 samples. Mouse 103,083 samples. Total 187,946
    + Feauture from GEO (cell line, tissue), SRA format from SRA, using FASTQ files. 
  - Method
    + FASTQ file from SRA dataset.
    + Using AWS/Amazon cloud computer for bulk FASTQ align.
    + Kallisto (one-way reads) & STAR (paired reads) for alignment program
    + Data store as H5 data matrix (hierarchical data format, binary)
    + Data clustering by t-SNE embedding
    + Providing enrichment analysis based on co-expression gene 
  - Review
    + Processed Gene Count Table을 parsing해서 사용하지 않고, FASTQ부터 re-align을 통해 batch effect를 줄이고, 획일화된 format을 가진 파일 생성.
    + GEO dataset사용.
    + co-expression gene analysis는 크게 의미 있어보임.
    
### 고찰
1. RNA degradation filtering
2. Batch effect normalizing
3. Using cloud computing for re-align?
