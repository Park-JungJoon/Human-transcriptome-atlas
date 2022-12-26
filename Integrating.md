# Intergrating 
+ 이용 가능한 세 데이터 베이스, (GTEx, ENCODE, TCGA)의 데이터를 통합함을 목적으로 한다.

## 1. Distribution of three databases
### 1-1. GTEx
  + 17,382 Samples.
  + Tissue, Sex, Age 3가지의 정보를 meta data에 사용했다. 
  + Tissue는 포괄적인 Tissue 30개와, Specific tissue 45개로 나타난다.
  + Sex는 male, female, unknown으로 나뉜다.
  + Age는 10년을 기준으로 20대 - 70대까지의 분포를 나타낸다.
  + 데이터 베이스의 특성으로 사망자들에서 채취한 샘플만을 사용한다.
### 1-2. TCGA
  + 22,018 Samples.
  + Tissue, Sex, Age 3가지의 정보를 meta data에 사용했다.
  + Tissue는 56개로 나뉜다.
  + Sex는 male, female, unknown으로 나뉜다.
  + Age는 days를 기준으로 나타난다.
  + 데이터 베이스의 특성으로는, 샘플들이 암에 관련된 샘플이다.
### 1-3. ENCODE
  + 서버의 문제로, 약 15개의 샘플들마다 수기로 다운로드 받아야한다. 다운로드 중에 있다.
  + Meta data 생성과, gene count table을 생성할 수 있는 소스코드를 작성했다.
  + 186 Samples.
  + Tissue, Sex, Age 3가지의 정보를 meta data에 사용했다.
  + Tissue는 91개로 나뉜다.
  + Sex는 male, female, unknown으로 나뉜다.
  + Age는 1년을 기준으로 나타난다.

## 2. Intergrating
### 2-1. Age
  + 나이는 가장 큰 단위인 10년(GTEx)로 통일하였다. 
### 2-2. Tissue
  + 3개 database에서 organ을 기준으로 총 45개의 Tissue를 기준점으로 사용했다.[Supplementary data](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/Tissue%20intergrating.txt)
### 2-3. Sex
  + 3개의 데이터 베이스에서 sex를 표기하는 방법이 같아, male/female/unknown으로 사용했다.
### 2-4. Gene
  + 각 데이터 베이스에 사용한 ENCODE gene annotation version이 달라, Count table간의 통합이 어려운 점에 있다. 
  + ENCODE (V29), GTEx (V26), TCGA(V38)

+ 현재 ENCODE를 제외하고, TCGA와 GTEx의 데이터를 meta data를 통합했고, ENCODE는 다운로드가 완료되는 대로 통합이 가능한 소스코드를 작성했다.
## 3. Distribution
