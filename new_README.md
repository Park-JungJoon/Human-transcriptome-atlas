# Human Transcriptome Atlas
본 연구에서는 Public bulk-RNA seq database의 데이터를 취합하고, 종합적인 분석 결과를 웹 앱을 통해 공개하는 것을 목적으로함.

</br>
# PART A. Data Collecting / Merging 
## 1. Data Collecting
+ Public Human Transcriptome Database는 대표적으로 GEO, GTEx, TCGA가 있음.
+ 위의 데이터 베이스 중, GEO는 각 연구 별 자료의 형식이 통일되어 있지 않아, [ARCHS4](https://maayanlab.cloud/archs4/) database에서 gene level raw count를 다운로드 받음.
+ 본 연구에서는 먼저 통합 가능한 GTEx, TCGA, GEO의 데이터를 통합하고, 부족한 조직의 보충을 SRA에서 하고자함.

</br>

## 2. Feature of three public human transcriptome databases
### 2-1 GTEx
  + 17,382 Samples.
  + Meta data로서 제공하는 정보로 Sample donor, tissue, specific tissue, submitted date, experiment method, sex, age, hardy scale 등의 정보를 제공한다.
  + Tissue는 포괄적인 Tissue 30개와, Specific tissue 45개로 나타난다.
  + Sex는 male, female으로 나뉜다.
  + Age는 10년을 기준으로 20대 - 70대까지의 분포를 나타낸다.
  + GTEx는 사망자에서 채취한 샘플만을 사용한다.
### 2-2 TCGA
  + 22,018 Samples.
  + Meta data로서 제공하는 정보로 age at diagnosis, race, sex, ethinicity, vital status, primary diagnosis, disease type 등을 제공한다. 
  + Tissue는 56개로 나뉜다.
  + Sex는 male, female, unknown으로 나뉜다.
  + Age는 days를 기준으로 나타난다. Age는 샘플 채취일이 아닌, 진단시 날짜(age at diagnosis)이다. 채취일 기준 나이 데이터를 제공하지 않아, Age를 사용했다.
  + TCGA는 모든 샘플이 암 환자에서 채취한 조직 샘플이며, 암세포와 정상세포가 혼재한다.
### 2-3 GEO
  + 12,393 Samples.
  + Meta data로서 제공하는 정보로 tissue 정보만 제공한다.
  + Tissue 21개로 나뉜다.
### 2-4 Merging Metadata
  + Sample 개수가 충분한 major tissue 30개만을 연구 대상으로 삼았다. 

## 3. Intergrating Meta Data
+ TCGA, GTEx  데이터 베이스에서 공통적으로 존재하는 meta data(age, tissue, sex)으로 통합 [meta data](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/META_MERGED_COMPLETE.tsv) (/panpyro/alfa/jjpark/run_umap/new_meta_merged.tsv) 를 만들었다.
### 3.1 Age
  + 나이는 가장 큰 단위인 10년(GTEx)로 통일하였다. 
### 3.2 Tissue
  + GTEx의 tissue 분류를 기반으로 ENCODE, TCGA의 tissue를 추가하여 30개의 tissue로 재분류하였다. [분류군](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/Tissue%20intergrating.txt) 
### 3.3 Sex
  + 3개의 데이터 베이스에서 sex를 공통적으로 표기하는, male/female/unknown을 사용했다.

</br>

## 4. Distribution of Intergrated Data

</br>

## 5. Gene Count Table Intergrating 
### 5.1 Gene Annotation Version Intergrating
  + 각 데이터 베이스 별 gencode annotation version이 다름.

  Feature|TCGA|GTEx|ENCODE
  -|-|-|-
  Version|36|26|41
  Gene|60,661|56,201|62,381
  
 + Ensemble annotation accession ID (e.g. ENSG00000001630.16)의 . 뒤의 숫자인 버젼을 제외하고, accession ID를 기준으로 공통되는 유전자를 파악함.

###  5.2 The bias between databases
  + DB와 Tissue에 따른 bias, distribution 파악 하기 위해, 차원 축소 그래프 UMAP (3D)를 통해 확인하였다.

</br>
</br>

# PART B. Data Handling
## 6. Global Normalization
  + Sample 간 비교를 위해 read depth (library size) 보정과, gene lenth 보정이 필요함. 
  + 두 보정법을 모두 차용한 [GeTMM] (https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2246-7)을 사용함.
  + GeTMM의 경우, RPK를 계산한 후 (Gene length 보정) 이후 edgeR 모듈의 TMM 계산 과정을 거침. 
  + TCGA의 경우, FPKM으로부터 Gene Length를 계산하였고, GTEx는 자체적으로 사용하는 Gene Length를 파싱하여 사용함.
+ RPK를 계산한 파일을 (/panpyro/alfa/jjpark/adjusted_merge/split_by_db/output_of_R)에 저장하였음.
