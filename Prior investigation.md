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

## Data handling 
### GTEx 
+ [GTEx](https://gtexportal.org/home/)에서 open access인, 948명의 Homo sapiens 개체에서  17,382개 samples에 대한 RNA-seq 결과(raw count)를 다운로드 하였다. 
+ GTEx는 대부분 사망(사고 및 기저 질환)한 인간 sample에 대한 RNA-seq 분석 데이터이며, sample의 tissue, age, sex등의 meta data를 만들기 위한 충분한 자료를 제공한다. [Meta Data](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/public_sorted_meta.tsv)
+ 17,382개 samples에 대한 meta data를 만들었으며, 개체 당 sample의 개수, sample의 tissue, sample의 specific한 tissue에 대한 통계는 아래와 같다. 

#### 1. 개체당 샘플의 개수 
 + Mean : 18.34
 + Median : 19.0
 
  Range of sample per human| Counts
  -|-
  0-10 | 94
  10-20 | 440
  20-30 | 373
  30 over | 41
  Total | 948

#### 2. Sample Tissue 분포
  
  Tissue|Count
  -|-
  Brain|2,642
  Skin|1,809
  Esophagus|1,445
  Blood Vessel|1,335
  Adipose Tissue|1,204
  Blood|929
  Heart|861
  Muscle|803
  Colon| 779
  Thyroid|653
  Nerve|619
  Lung|578
  Breast|459
  Testis|361
  Stomach|359
  Pancreas|328
  Pituitary|283
  Adrenal Gland|258
  Prostate|245
  Spleen|241
  Liver|226
  Small Intestine|187
  Ovary|180
  Salivary Gland|162
  Vagina|156
  Uterus|142
  Kidney|89
  Bladder|21
  Cervix Uteri|19
  Fallopian Tube|9
  Total|17,382
  
#### 3. Specific tissue 분포

  Specific tissue|Count
  -|-
  Muscle - Skeletal|803
  Whole Blood|755
  Skin - Sun Exposed (Lower leg)|701
  Adipose - Subcutaneous|663
  Artery - Tibial|663
  Thyroid|653
  Nerve - Tibial|619
  Skin - Not Sun Exposed (Suprapubic)|604
  Lung|578
  Esophagus - Mucosa|555
  Adipose - Visceral (Omentum)|541
  Esophagus - Muscularis|515
  Cells - Cultured fibroblasts|504
  Breast - Mammary Tissue|459
  Artery - Aorta|432
  Heart - Left Ventricle|432
  Heart - Atrial Appendage|429
  Colon - Transverse|406
  Esophagus - Gastroesophageal Junction|375
  Colon - Sigmoid|373
  Testis|361
  Stomach|359
  Pancreas|328
  Pituitary|283
  Adrenal Gland|258
  Brain - Cortex|255
  Brain - Caudate (basal ganglia)|246
  Brain - Nucleus accumbens (basal ganglia)|246
  Prostate|245
  Brain - Cerebellum|241
  Spleen|241
  Artery - Coronary|240
  Liver|226
  Brain - Cerebellar Hemisphere|215
  Brain - Frontal Cortex (BA9)|209
  Brain - Putamen (basal ganglia)|205
  Brain - Hypothalamus|202
  Brain - Hippocampus|197
  Small Intestine - Terminal Ileum|187
  Ovary|180
  Brain - Anterior cingulate cortex (BA24)|176
  Cells - EBV-transformed lymphocytes|174
  Minor Salivary Gland|162
  Brain - Spinal cord (cervical c-1)|159
  Vagina|156
  Brain - Amygdala|152
  Uterus|142
  Brain - Substantia nigra|139
  Kidney - Cortex|85
  Bladder|21
  Cervix - Endocervix|10
  Cervix - Ectocervix|9
  Fallopian Tube|9
  Kidney - Medulla|4    
  Total|17,382

#### 5. Age & Sex
+ Raw data의 나이는 20-29, 30-39 식으로 10년 기준으로 표기함.
##### 5.1 Age
+ Median : 50-59
+ Mean : 53.68 (75,65,55,45,35,25로 계산함.)
+ 
|Age|Count|
|-|-|
70-79|602
60-69|5,822
50-59|5,612
40-49|2,701
30-39|1,324
20-29|1,321
Total|17,382

|Sex|Count|
|-|-|
|Male|11,583|
|Female|5,798|
|Total|17,382|

#### 4. Analysis & Clustering GTEx Data
+ GTEx에서 보정한 TPM 파일을 input으로 사용함.[data](https://storage.googleapis.com/gtex_analysis_v8/rna_seq_data/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_tpm.gct.gz)
+ Meta data의 attribute에 따라 mds plot, heat map을 통해 attribute가 데이터의 어떤 영향을 끼치는지 연구함.

##### 4-1. Human Bias
+ 개체간 유전자 발현의 차이가 Expression level에 차이가 있는지 알아보기 위해, 인당 17개의 Sample을 갖는 4명의 사람을 대상으로, 총 68개 Sample에 대한 MDS plot, Heatmap을 그렸다.
+ GTEX-1F57B, GTEX-139TT, GTEX-1C4CL, GTEX-1GN1V 4명의 샘플을 사용했고, 성별은 GTEX-1F57B 여성, 나머지 3명은 남성이다.
![2022_gtex_human_1210_github_mds](https://user-images.githubusercontent.com/97942772/206842430-2315cf35-3a06-49f0-8a9c-1752f651091d.png)
+ MDS Plot
  개체간 bias는 낮다. 좌측 아래 clustring된 3개의 sample은 모두 각기 다른 사람의 testis tissue이다.
<img width="848" alt="image" src="https://user-images.githubusercontent.com/97942772/206842578-006ea9b6-87c5-4c93-b4bc-4fcb32b8f337.png">
+ Heatmap
  Heatmap의 일부분을 나타냈다.[원본](https://github.com/Park-JungJoon/Human-transcriptome-atlas/tree/main/Supplementary%20data)
  성별, 개인간의 clustering이 이뤄지지 않았다.

##### 4-2. Tissue 
+ Sample의 tissue 차이가 expression level에 차이가 있는지 알아보기 위해, 성별 특이적인 tissue(Testis, Ovary) 2개와 Lung, Liver 총 4개의 tissue 각각 10개의 sample을 연구에 사용했다. 총 40개 sample
+ 성별간의 차이를 보기 위해, Lung과 Liver tissue 모두 남여 5개씩의 sample을 사용했다. 
![2022_gtex_tissue_toy1210_mds](https://user-images.githubusercontent.com/97942772/206842919-cc8795ee-b7c8-4db6-84d2-4dfc8163bb96.png)
+ MDS Plot
  Tissue간 clustering이 매우 뚜렷하다. 같은 tissue의 다른 성별을 가진 경우 발현의 차이는 크게 없다. 
  성별간 발현차이는 적고, tissue간 발현차이는 매우 뚜렷하다.
<img width="850" alt="image" src="https://user-images.githubusercontent.com/97942772/206842960-2713f250-4ddb-49e4-8d42-c900fc98f0c1.png">
+ Heatmap 
  MDS plot과 마찬가지로, tissue간 clustering이 매우 뚜렷하다. MDS plot과 마찬가지로, 같은 tissue의 다른 성별인 샘플간의 차이는 없으며, 전체적인 mapping pattern이 tissue에 따라서 보인다. 

  
