# Human Transcriptome Atlas
본 연구에서는 Public bulk-RNA seq database의 데이터를 취합하고, 종합적인 분석 결과를 웹 앱을 통해 공개하는 것을 목적으로함.

</br>

## 1. Data Collecting
+ Public Human Transcriptome Database는 대표적으로 GEO, GTEx, TCGA가 있음.
+ 위의 데이터 베이스 중, GEO는 각 연구 별 자료의 형식이 통일되어 있지 않아, [ARCHS4](https://maayanlab.cloud/archs4/)database에서 gene level raw count를 다운로드 받음.
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
