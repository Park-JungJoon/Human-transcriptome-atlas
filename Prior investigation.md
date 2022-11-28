## 추출 가능한 데이터 베이스 

- GEO/SRA (NCBI) 
- ENCODE
- TCGA (NIH)
- GTEx (NIH)
- Array Express

### ENCODE

  - Samples : 576
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

### Data selecting 
  + GEO/SRA dataset의 크기가 가장 크고, micro array를 비롯한 여러 platform을 사용할 수 있지만, 데이터 processing이 어렵다. 
  + GEO/SRA를 제외한 platform은 데이터의 형식이 통일되어있다. 
  + GEO/SRA dataset을 사용하려면, 가장 간단한 방법으로 STAR gene counting/GTEx form 등 특정 form인 데이터들을 선별적으로 사용하는 것이 가능하다. 그러나 이와 같은 방식을 채택할 때, Program에 따른 bias나, Platform bias(TCGA의 경우 cancer cell이 많으므로.)이 생길 수 있는 문제점이 있다. 
