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
### 3-1. Intergrated Data
#### 3-1-a. Tissue
+ 통합 데이터의 상위 20개 Tissue에 대한 분포는 아래와 같다.

![Rplot01](https://user-images.githubusercontent.com/97942772/209561224-471cc8c8-b267-4722-b362-40e7f8245e06.png)

Tissue|Blood|Brain|Lung|Skin|Thyroid|Breast|Kidney|Esophagus|Large Intestine|Uterus|Blood Vessel|Adipose Tissue|Prostate|Heart|Pancreas|Stomach|Muscle|Liver|Ovary|Nerve
-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
Count|6,684|3,516|2,450|2,311|2,055|2,046|1,868|1,666|1,659|1,531|1,335|1,203|936|861|840|830|803|696|683|630


#### 3-1-b. Age
+ 통합 데이터의 Age 분포는 아래와 같다.
![image](https://user-images.githubusercontent.com/97942772/209555837-e34a3066-35af-4e0d-a4b3-a71c4ea5fa8c.png)

Age|90-99|80-89|70-79|60-69|50-59|40-49|30-39|20-29|10-19|00-09|NA|
-|-|-|-|-|-|-|-|-|-|-|-|
Count|228|1,049|3,894|10,618|9,485|4,898|2,572|2,142|2,129|412|1,972


#### 3-1-c. Sex
Sex | Count
-|-
Male|22,311
Female|16,584
NA|504

### 3-2. GTEx Data
#### 3-2-a. Tissue
![image](https://user-images.githubusercontent.com/97942772/209560018-97aa846a-0e9e-4798-94bc-454179d5526d.png)


Tissue|Brain|Skin|Esophagus|Blood Vessel|Adipose Tissue|Blood|Heart|Muscle|Large intestine|Thyroid|Nerve|Lung|Breast|Testis|Stomach|Pancreas|Pituitary|Adrenal Gland|Prostate|Spleen|
-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
Count|2,642|1,809|1,445|1,335|1,203|929|861|803|779|653|619|578|459|361|359|328|283|258|245|241


#### 3-2-b. Age
![image](https://user-images.githubusercontent.com/97942772/209559451-1de7ac4e-4af3-4103-8ff6-60bf902a76b8.png)

Age|70-79|60-69|50-59|40-49|30-39|20-29
-|-|-|-|-|-|-
Count|601|5,821|5,614|2,702|1,323|1,320

#### 3-2-c. Sex
Sex|Count
-|-
male|11,584
female|5,797

### 3-3. TCGA Data
#### 3-3-a. Tissue
![Rplot](https://user-images.githubusercontent.com/97942772/209560856-d976b01c-b4c4-46c7-9640-c5992e133231.png)


Tissue|Blood|Lung|Kidney|Breast|Thyroid|Uterus|Large intestine|Brain|Prostate|Lymphoid organ|Pancreas|Ovary|Skin|Stomach|Liver|Bladder|ETC|Adrenal Gland|Tongue|Testis|
-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
Count|5755|1872|1779|1587|1402|1370|880|874|691|519|512|503|502|471|470|433|318|298|221|169|157|


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

