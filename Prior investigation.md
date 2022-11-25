## 추출 가능한 데이터 베이스 

- GEO/SRA (NCBI) 
- ENCODE
- TCGA (NIH)
- GTEx (NIH)
- Array Express

### ENCODE

  - Samples : 58
  - File format : FASTQ, BAM, TSV
  - Data format : FPKM/TPM 
  - Feature : Tissue/Cell line/Primary cell
  - Platform : total RNA-seq/Poly A plus RNA-seq/Poly A minus RNA-seq

### TCGA 

  - Samples : 21,781 (Only open access, controlled )
  - File format : TSV
  - Data format : TPM/FPKM
  - Feature : Cancer cell / Normal cell / Tissue
  - Platform : RNA-seq/scRNA-seq/miRNA-seq

### GEO/SRA

  - Samples : 18,676 (sample 6-100 limited, for filtering scRNA-seq)
  - File format : Not Unifed. TSV, tar.gz, FASTQ, BAM
  - Data format : Not Unifed. 
  - Feature : Not Unifed. Tissue/Treatment/etc ...
  - Platform : micro array/RNA-seq/scRNA-seq/miRNA-seq/etc ...

### Arrary Express

  - Samples : 3,091(protein coding), 500(non protein coding)
  - File format : FASTQ
  - Data format : NA
  - Feature : age/developmental stage/sex/disease/organism part/cell type/immunophenotype/etc...
  - Platform : RNA-seq/chip-seq/chip-array/micro array/methylation-profiling by highthroughput sequencing/etc..

### GTEx

  - Samples : 11,688
  - File format : FASTQ/BAM/VCF/gtc/cel/etc ...
  - Data format : raw count, TPM, median TPM
  - Feature : Tissue/Sex/Age/Pathology Categories/Pathology Notes
