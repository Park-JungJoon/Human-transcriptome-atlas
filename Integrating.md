# Intergrating Human Transcriptome Database 
+ Public human transcriptome Database (GTEx, ENCODE, TCGA)의 gene count table(TPM), meta data를 통합함을 목적으로 한다.

## 1. Feature of three public human transcriptome databases
### 1-1. GTEx
  + 17,382 Samples.
  + Meta data로서 제공하는 정보로 Sample donor, tissue, specific tissue, submitted date, experiment method, sex, age, hardy scale 등의 정보를 제공한다.
  + Tissue는 포괄적인 Tissue 30개와, Specific tissue 45개로 나타난다.
  + Sex는 male, female으로 나뉜다.
  + Age는 10년을 기준으로 20대 - 70대까지의 분포를 나타낸다.
  + GTEx는 사망자에서 채취한 샘플만을 사용한다.
### 1-2. TCGA
  + 22,018 Samples.
  + Meta data로서 제공하는 정보로 age at diagnosis, race, sex, ethinicity, vital status, primary diagnosis, disease type 등을 제공한다. 
  + Tissue는 56개로 나뉜다.
  + Sex는 male, female, unknown으로 나뉜다.
  + Age는 days를 기준으로 나타난다. Age는 샘플 채취일이 아닌, 진단시 날짜(age at diagnosis)이다. 채취일 기준 나이 데이터를 제공하지 않아, Age를 사용했다.
  + TCGA는 모든 샘플이 암 환자에서 채취한 조직 샘플이며, 암세포와 정상세포가 혼재한다.
### 1-3. ENCODE
  + Meta data로서 제공하는 정보로 tissue, age, sex, sample donor 등의 meta data를 제공한다.
  + 350 Samples.(Total RNA-seq 186, polyA plus RNA-seq 164.)
  + Tissue는 91개로 나뉜다.
  + Sex는 male, female, unknown, male,female으로 나뉜다.
  + Age는 1년을 기준으로 나타난다.

## 2. Intergrating Meta Data
+ 세 데이터 베이스에서 공통적으로 존재하는 meta data(age, tissue, sex)으로 통합 [meta data](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/integrated_tcga_gtex.tsv)를 만들었다.
### 2-1. Age
  + 나이는 가장 큰 단위인 10년(GTEx)로 통일하였다. 
### 2-2. Tissue
  + GTEx의 tissue 분류를 기반으로 ENCODE, TCGA의 tissue를 추가하여 45개의 tissue로 재분류하였다. [분류군](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/Tissue%20intergrating.txt) 
### 2-3. Sex
  + 3개의 데이터 베이스에서 sex를 공통적으로 표기하는, male/female/unknown을 사용하고, ENCODE에서 2가지 sample에서 나온 데이터의 경우 male,female로 표기 되는 경우는 unknown에 통합했다.
### 2-4. Gene
  + 각 데이터 베이스에 사용한 ENCODE gene annotation version이 달라, Count table간의 통합이 어려운 점에 있다. 
  + ENCODE (V29), GTEx (V26), TCGA(V38)

## 3. Distribution of Intergrated Data
### 3-1. Intergrated Data
#### 3-1-a. Tissue
+ 통합 데이터의 sample 개수 상위 20개 tissue의 sample 개수 분포는 아래와 같다. [Total Tissue Distribution](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/Integrated_data.md)
![image](https://user-images.githubusercontent.com/97942772/210167153-6c432dc0-a8d4-43b8-bedb-5467df12b7d0.png)


Tissue|Blood|Brain|Lung|Skin|Thyroid|Breast|Kidney|Large intestine|Esophagus|Uterus|Blood Vessel|Adipose Tissue|Prostate|Heart|Muscle|Pancreas|Stomach|Liver|Ovary|Nerve|Adrenal Gland|Lymphoid organ|Testis|Bladder|ETC|Pituitary|Spleen|Mouth|Small Intestine|Tongue|Salivary Gland|Vagina|Retroperitoneum and peritoneum|Connective, subcutaneous and other soft tissues|Unknown|Larynx|Heart,mediastinum,and pleura|Thymus|Bone&joint|Eye|Tonsil|Gallbladder|Placenta|Fallopian Tube|Anal|Umbilical cord|
-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-
Count|6683|3523|2478|2320|2060|2049|1888|1684|1676|1533|1344|1215|938|895|852|850|845|707|692|642|577|523|522|456|318|283|255|220|204|170|163|157|146|135|129|128|124|99|97|81|45|17|12|9|3|1|


#### 3-1-b. Age
+ 통합 데이터의 Age 분포는 아래와 같다.
![image](https://user-images.githubusercontent.com/97942772/209555837-e34a3066-35af-4e0d-a4b3-a71c4ea5fa8c.png)

Age|90-99|80-89|70-79|60-69|50-59|40-49|30-39|20-29|10-19|00-09|Unknown|
-|-|-|-|-|-|-|-|-|-|-|
Count|228|1049|3894|10617|9485|4898|2571|2142|2129|761|1974|

#### 3-1-c. Sex
Sex | Count
-|-
Male|22,311
Female|16,584
NA|504

### 3-2. GTEx Data
#### 3-2-a. Tissue
+ GTEx 데이터의 sample 개수 상위 20개 tissue의 sample 개수 분포는 아래와 같다. [Total Tissue Distribution](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/Integrated_data.md)

![image](https://user-images.githubusercontent.com/97942772/209605328-6820d488-6eb8-4d97-9ac3-da10c32dccb8.png)


Tissue|Brain|Skin|Esophagus|Blood Vessel|Adipose Tissue|Blood|Heart|Muscle|Large intestine|Thyroid|Nerve|Lung|Breast|Testis|Stomach|Pancreas|Pituitary|Adrenal Gland|Prostate|Spleen|
-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
Count|2,642|1,809|1,445|1,335|1,203|929|861|803|779|653|619|578|459|361|359|328|283|258|245|241


#### 3-2-b. Age
![image](https://user-images.githubusercontent.com/97942772/209559451-1de7ac4e-4af3-4103-8ff6-60bf902a76b8.png)

Age|20-29|30-39|40-49|50-59|60-69|70-79
-|-|-|-|-|-|-
Count|1,320|1,323|2,702|5,614|5,821|601

#### 3-2-c. Sex
Sex|Count
-|-
male|11,584
female|5,797

### 3-3. TCGA Data
#### 3-3-a. Tissue
+ TCGA 데이터의 sample 개수 상위 20개 tissue의 sample 개수 분포는 아래와 같다. [Total Tissue Distribution](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplementary%20data/Integrated_data.md)

![image](https://user-images.githubusercontent.com/97942772/209605291-a261c877-cce4-4bfb-8714-cae4f5218bf2.png)


Tissue|Blood|Lung|Kidney|Breast|Thyroid|Uterus|Large intestine|Brain|Prostate|Lymphoid organ|Pancreas|Ovary|Skin|Stomach|Liver|Bladder|ETC|Adrenal Gland|Tongue|Testis|
-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
Count|5,755|1,872|1,779|1,587|1,402|1,370|880|874|691|519|512|503|502|471|470|433|318|298|221|169|157|


#### 3-3-b. Age
![image](https://user-images.githubusercontent.com/97942772/209559228-047add7b-e153-4805-ab54-a83e4bc1d1fa.png)

Age|90-99|80-89|70-79|60-69|50-59|40-49|30-39|20-29|10-19|00-09|NA|
-|-|-|-|-|-|-|-|-|-|-|-|
Count|228|1,049|3,293|4,797|3,871|2,196|1,249|822|2,129|412|1,972


#### 3-3-c. Sex
Sex|Count
-|-
Female|10,787
Male|10,727
NA|504

## Discussion
+ GTEx & TCGA data's attribute is cancer and dead people. Removing batch effect might be required.
+ Tissue re-naming needed, by DEGs. 
+ Data supplement from GEO/SRA, tissue with insufficient number of samples. 
