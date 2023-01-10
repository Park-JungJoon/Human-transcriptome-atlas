# Human Transcriptome Atlas
## 1. Data Collecting
+ Public Human Transcriptome Database는 대표적으로 GEO, GTEx, TCGA, ENCODE가 있음.
+ 위의 데이터 베이스 중, GEO는 각 연구 별 자료의 형식이 통일되어있지 않고, 보정 방법 및 gencode annotation 버젼이 달라 선행 연구에서 GEO의 gene count table을 사용한 결과는 없으며, [ARCHS4](https://maayanlab.cloud/archs4/) 연구에서는 FASTQ 파일을 SRA로부터 받아 computational RNA-seq workflow를 cloud computing을 이용해 통일된 형식의 gene count table을 만들어 사용함.
+ 본 연구에서는 먼저 통합 가능한 GTEx, TCGA, ENCODE의 데이터를 통합하고, 부족한 조직의 보충을 SRA에서 하고자함.

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
### 2-3 ENCODE
  + Meta data로서 제공하는 정보로 tissue, age, sex, sample donor 등의 meta data를 제공한다.
  + 350 Samples.(Total RNA-seq 186, polyA plus RNA-seq 164.)
  + Tissue는 91개로 나뉜다.
  + Sex는 male, female, unknown, cell line인 경우, male&female으로 나뉜다.
  + Age는 성인 기준 1년으로 나타나며, weeks, days로도 표기된다.


## 3. Intergrating Meta Data
+ 세 데이터 베이스에서 공통적으로 존재하는 meta data(age, tissue, sex)으로 통합 [meta data](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/META_MERGED_COMPLETE.tsv)를 만들었다.
### 3.1 Age
  + 나이는 가장 큰 단위인 10년(GTEx)로 통일하였다. 
### 3.2 Tissue
  + GTEx의 tissue 분류를 기반으로 ENCODE, TCGA의 tissue를 추가하여 45개의 tissue로 재분류하였다. [분류군](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/Tissue%20intergrating.txt) 
### 3.3 Sex
  + 3개의 데이터 베이스에서 sex를 공통적으로 표기하는, male/female/unknown을 사용하고, ENCODE에서 cell line에서 나온 데이터의 경우 male,female로 표기 되는 경우는 unknown에 통합했다.

## 4. Distribution of Intergrated Data
### 4.1 Tissue Distribution
+ 통합 데이터의 sample 개수 상위 20개 tissue의 sample 개수 분포는 아래와 같다. [Total Tissue Distribution]
(https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/Integrated_data.md)
![image](https://user-images.githubusercontent.com/97942772/210997605-de682ee6-7083-47a9-8074-b8fd20a3c9bf.png)

Tissue|Blood|Brain|Lung|Skin|Thyroid|Breast|Kidney|Large intestine|Esophagus|Uterus|Blood Vessel|Adipose Tissue|Prostate|Heart|Muscle|Pancreas|Stomach|Liver|Ovary|Nerve|Adrenal Gland|Lymphoid organ|Testis|Bladder|ETC|Pituitary|Spleen|Mouth|Small Intestine|Tongue|Salivary Gland|Vagina|Retroperitoneum and peritoneum|Connective, subcutaneous and other soft tissues|Unknown|Larynx|Heart,mediastinum,and pleura|Thymus|Bone&joint|Eye|Tonsil|Gallbladder|Placenta|Fallopian Tube|Anal|Umbilical cord|
-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Count|6683|3523|2478|2320|2060|2049|1888|1684|1676|1533|1344|1215|938|895|852|850|845|707|692|642|577|523|522|456|318|283|255|220|204|170|163|157|146|135|129|128|124|99|97|81|45|17|12|9|3|1|

### 4.2 Age Distribution
+ 통합 데이터의 Age 분포는 아래와 같다.
![image](https://user-images.githubusercontent.com/97942772/210167767-94d0cd6a-1d1f-4803-920f-cf32a1536f93.png)

Age|90-99|80-89|70-79|60-69|50-59|40-49|30-39|20-29|10-19|00-09|Unknown|
-|-|-|-|-|-|-|-|-|-|-|-
Count|228|1049|3894|10617|9485|4898|2571|2142|2129|761|1974|

#### 4.3 Sex Distribution
Sex | Count
-|-
Male|22,472
Female|16,754
Unknown|522

## 5. Gene Count Table Intergrating 
### 5.1 Gene Annotation Version Intergrating
+ 각 데이터 베이스 별 gencode annotation version이 다름.

  Feature|TCGA|GTEx|ENCODE
  -|-|-|-
  Version|36|26|29
  Gene|60,661|56,201|55,617
 
 + Ensemble annotation accession ID (e.g. ENSG00000001630.16)의 . 뒤의 숫자인 버젼을 제외하고, accession ID를 기준으로 공통되는 유전자를 파악함.
 
    <img width="270" alt="image" src="https://user-images.githubusercontent.com/97942772/211015422-a598498e-1570-472e-902b-65328cc0d700.png">
    
+ 세 데이터 베이스에서 공유하는 gene의 개수는 55,617개이다. 전체 union gene은 61,730이다.

  V26|V29|V36|Protein Coding|Non Coding
  -|-|-|-|-
  O|O|O|19,200|36,417
  X|O|O|647|2,121
  X|x|O|97|2,134
  X|O|X|29|30
 
 + Protein Coding Gene의 96%가 공유됨. 
 + Gene name과 gene type등은 세 데이터 베이스 중 가장 최신 버젼인 36으로 통일하였다. 
 + 세 데이터 베이스의 integrating을 위한 gene은 공유되는 55,617개를 사용하였다.
 + 공유되는 유전자 55,617개를 이용해 Gene Count Table을 작성함. (/eevee/val/jjpark/atlas/integrate/V36_COUNT_TABLE_COMPLETE.tsv)
  
###  5.2 The bias between databases
+ 데이터 베이스 간의 bias를 확인하기 위해, 샘플 채취 조직, 성별, 나이가 같은 샘플의 유전자 발현 heatmap을 확인하였다.
+ Lung, Male, 60-69인 샘플을 각 데이터 베이스 별 3개씩 추출하였고 heatmap을 그렸다.
![2102_NOZERO_HEATMAP_LUNG](https://user-images.githubusercontent.com/97942772/211442630-ae50fb83-b3d4-4bf5-a74f-393d91c2b5b1.png)
+ 데이터 베이스 별 bias가 확실시되며, 615442.9 649715.42 648597.93 811693.97 776149.79 989849.54 998676.16 999194.0 999076.33
 
