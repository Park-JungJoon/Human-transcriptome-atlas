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
#### 5.2.1 Heatmap Distribution
+ 데이터 베이스 간의 bias를 확인하기 위해, 샘플 채취 조직, 성별, 나이가 같은 샘플의 유전자 발현 heatmap을 확인하였다.
+ Lung, Male, 60-69인 샘플을 각 데이터 베이스 별 3개씩 추출하였고 heatmap을 그림.
![2102_NOZERO_HEATMAP_LUNG](https://user-images.githubusercontent.com/97942772/211442630-ae50fb83-b3d4-4bf5-a74f-393d91c2b5b1.png)

+ Lung과 비교하기 위해 Liver, Male인 샘플을 각 데이터 베이스 별 3개씩 추출하였고 heatmap을 그림.
![image](https://user-images.githubusercontent.com/97942772/211445927-bede13fa-6298-4c50-9d4a-ad6b78155fe9.png)

+ 데이터 베이스 내 tissue는 clustering이 이뤄지나, 일부 분류군 (GTEx Lung / GTEx Liver)의 경우 데이터 베이스 간 차이가 조직 간 발현차이보다 큰 경향이 있다.


#### 5.2.2 UMAP dimensional reduction
+ 데이터 베이스, 성별, tissue 별 bias를 확인하기 위해, 차원 축소 그래프를 UMAP(3D)을 통해 확인하였다. 
+ 데이터 베이스 별 분포는 아래와 같다. 

![image](https://user-images.githubusercontent.com/97942772/212582208-8b48c87c-4c4e-4f19-b91a-2c80e43c4c8b.png)

+ 세 데이터 베이스간 clustering이 확실시 됨

<br/>

+ 조직 별 분포는 아래와 같다. 
<img width="700" alt="제목 없음" src="https://user-images.githubusercontent.com/97942772/212582092-d16345a6-78d1-4566-b79d-6b5918f61641.png">

+  조직 별 clustering이 되나, Blood, Skin, Uterus에서 같은 tissue가 DB에 따라 2개로 나뉘어 분포하는 경향이 있다. 
+ 실험별 보정값이 다르기 때문으로 보이며, RNA-seq batch effect correction tool [ComBat-seq](https://academic.oup.com/nargab/article/2/3/lqaa078/5909519), 혹은 각 데이터 베이스 별 발현량을 조사하여 수기로 샘플 별 재보정을 고려함.

### 6. Batch Effect, Bias Correction
#### 6.1. Divide by Sample TPM Sum
+ 가장 naive한 방법으로, 각 발현량을 sample TPM의 총합으로 나눔. 
+ PCA 분석 결과, 같은 database내 분산이 줄긴 하나, db간 분산이 줄지 않음.
#### 6.2. ComBat-Seq [link](https://academic.oup.com/nargab/article/2/3/lqaa078/5909519)
+ 선행 연구 [Unifying cancer and normal RNA sequencing data from different sources](https://www.nature.com/articles/sdata201861)에서, GTEx와 TCGA의 database 간 bias를 ComBat-seq을 이용해 완화함.(Fig 2)
+ ComBat-seq의 input으로 TPM count table을 사용할 수 없음. 일관성이 없는 2가지 방법(ComBat-seq, TPM)으로 보정을 하기 때문에 ComBat-seq 논문에서 TPM을 input으로 사용하는 것을 권고하지 않음.
+ Sample 개수가 350개이고, raw count를 제공하지 않은 ENCODE를 데이터 병합 대상에서 제외함.
+ 이후, ComBat-seq으로 batch effect가 제거된 gene count table을 생성함. (/panpyro/alfa/jjpark/adjusted_merge/COMBATED_RAW_COUNT_TABLE.tsv)
![image](https://user-images.githubusercontent.com/97942772/215329772-029a9e91-8a16-4408-a66f-918cbbc38d2d.png)

  + Lung Sample 10개를 GTEx, TCGA 두 데이터 베이스에서 추출함. Raw count로 PCA 분석을 실시함. 

![image](https://user-images.githubusercontent.com/97942772/215329776-b67ab413-c62f-4714-9316-cd473bd522dc.png)

  + 같은 샘플에 대해 ComBat-seq이 보정한 PCA 결과; DB간 bias가 줄고 clustering됨.


#### 6.3. GeTMM
+ ComBat-seq을 통해 얻은 database 간 bias가 줄어든 raw count table의 normalizing이 요구됨.
+ Sample 간 비교를 위해 read depth (library size) 보정과, gene lenth 보정이 필요함. 
+ 두 보정법을 모두 차용한 [GeTMM] (https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2246-7)을 사용함.
+ GeTMM의 경우, RPK를 계산한 후 (Gene length 보정) 이후 edgeR 모듈의 TMM 계산 과정을 거침. 
+ TCGA의 경우, FPKM으로부터 Gene Length를 계산하였고, GTEx는 자체적으로 사용하는 Gene Length를 파싱하여 사용함.
+ RPK를 계산한 파일을 (/panpyro/alfa/jjpark/adjusted_merge/split_by_db/output_of_R)에 저장하였음.
+ GeTMM 변환 중에 있음.

#### 6.4. Batch Effect Correction & Global Normalization Validation
+ 데이터 베이스 bias가 줄고, tissue간 clustering이 되는 지 확인하기 위해, 차원 축소 그래프를 UMAP(3D)을 통해 확인하였다. 
+ 데이터 베이스 별 분포는 아래와 같다. 

<img width="700" alt="image" src="https://user-images.githubusercontent.com/97942772/215636833-eff439e5-b70d-4353-8989-f8d55b288153.png">

  + 5.2.2의 TPM UMAP (Non-Batch effect correction)과 비교했을 때, 데이터 베이스가 양극화 되어 나타나는 경향성이 적어짐

+ Tissue 별 분포는 아래와 같다.

<img width="700" alt="image" src="https://user-images.githubusercontent.com/97942772/215637752-c81f93ff-9331-4b4a-9ff3-214301ddbb5b.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/97942772/215638651-5a0ba393-dba0-4c1e-9283-d3a132535860.png">


+ 같은 tissue가 데이터 베이스에 따라 2개로 나뉘게 되는 경향성이 적어짐.
+ ComBat-Seq과, GeTMM을 통한 normalizing이 TCGA, GTEx 데이터 셋의 데이터간 bias를 줄이는 방법으로 효과적임.

### 7. Comparison Normalizing Methods
+ 앞서 진행한 normalizing method들과, 단순 library size로 보정하는 방법이 sample간 비교에 있어서 큰 차이를 갖는지 검토함.
+ Gene 3개에 대해, X축에 Raw count/Sample library size, Y축에 GeTMM, Combet-seq/Sample library size 값을 사용함.
+ Scatter Plot으로 표기하고 Y=x 에 대한 선형회귀, Multiple R-squared 값을 통해 차이를 갖는지 검토함.

![pictures](https://user-images.githubusercontent.com/97942772/216820951-03c902e5-fac2-40a0-8b09-d89aa52a6f95.jpg)

![pictures (1)](https://user-images.githubusercontent.com/97942772/216821100-f640a07c-4fb6-497d-b660-aabd0dc01fa5.jpg)

![pictures (2)](https://user-images.githubusercontent.com/97942772/216821222-16f878ba-087d-4495-8ae8-6a0b7fc4f6bb.jpg)

+ Raw-count - GeTMM간의 R-squared 값이 모두 0.75 이상으로, GeTMM이나, Combet-seq의 사용시 이점이 크지 않음.
+ ALB, CD9의 경우 3개의 선으로 나눠지는 경향이 관측되는데, GeTMM의 보정 시 input으로 Combet-seq으로 보정된 파일을 넣어주기 때문임.
+ Batch effect correction 과정은 DB간 bias 를 일정 계수를 곱하여 산출함.
+ 결론적으로, Running time과 Processing 과정에서 사용되는 시간 소모에 비해 Normalizing method의 성능 차이는 크게 없으므로, 이후 연구에서 가장 간단한 방법인 raw count/library size 방법을 사용하고자 함.

### 8. Gene Expression Level Check in My Data, by HKG(House Keeping Gene), TS(Tissue-Specific Gene)
+  이미 알려진 HKG, TS를 통해 technical validation을 진행함. HKG로 GAPDH, GUSB를 사용했고, Liver Specific Gene ALB, Adrenal Gland Specific Gene AS3MT를 사용함.

<img width="947" alt="KakaoTalk_20230205_010156804" src="https://user-images.githubusercontent.com/97942772/216821472-4040d06a-1e5e-4dbd-b7bd-a8348efd6b9e.png">
<img width="947" alt="KakaoTalk_20230205_010210426" src="https://user-images.githubusercontent.com/97942772/216821489-0059488c-cc1f-45ec-9c4d-b9e075e080e7.png">

+  X축은 tissue, Y축은 log(GeTMM)으로 boxplot을 사용함.(Raw Count/library size 보정 파일은 작업 중에 있어, 이미 만들어진 파일 사용)
+  두 유전자 모두 전체 45개 Tissue에서 고른 분포를 보이며, 보고된 House Keeping Gene에 적합함.

<img width="947" alt="KakaoTalk_20230205_010220587" src="https://user-images.githubusercontent.com/97942772/216821499-5cdd6221-2efe-4cf7-b266-5adb31f70166.png">

+  Adrenal Gland에서의 AS3MT 발현량 중간값이 다른 tissue들에 비해 최소 100배 이상의 차이가 관찰됨.

<img width="947" alt="KakaoTalk_20230205_010229982" src="https://user-images.githubusercontent.com/97942772/216821507-c84536ff-f454-4f66-bd86-40f1c8c7eba0.png">

+ Liver 에서의 ALB 발현량 중간값이 다른 tissue들에 비해 최소 1000배 이상의 차이가 관찰됨.
+ 데이터의  TS/HKG searching을 위해 충분한 clean-up이 됨.

### 9. Comparison HKG between known HKG gene set, made HKG gene set.

+ 표준 편차를 산술 평균으로 나눈 CV(coefficient of variation)값을 HKG 지표로서 사용함.
+ 대조군으로 [HRT Atlas](https://academic.oup.com/nar/article/49/D1/D947/5871367)에서 제공하는 2,177개의 유전자를 사용함.
+ HRT Atlas에서 제공하는 유전자는 모두 protein coding gene으로, 갖고 있는 데이터에서도 protein coding gene 19,183개를 대상으로 연구를 실시함.
+ 각 Gene에 대한 CV의 분포는 아래 히스토그램과 같음. (X,Y축 모두 log10 scale)

![image](https://user-images.githubusercontent.com/97942772/218311589-2025c3cb-dd20-48cd-900d-6bf635959915.png)

+ 각 Gene에 대한 발현량 분포는 아래 히스토그램과 같음. (X,Y축 모두 log10 scale) 뱔현량은 gene당 GeTMM값의 총합/샘플 수 로 계산함.

![image](https://user-images.githubusercontent.com/97942772/218311666-5a10a403-ef7c-43c4-a249-a59b3fa0618e.png)

+ CV값과 GeTMM 값의 평균에 대한 기본적인 통계치는 아래 표와 같음.

Value|Median|Mean|Minimum|Maximum
-|-|-|-|-
CV Value|1.4881|4.0097|0.2617|198.4968
Expression|11.90|53.83|0.00|43625.05

+ 각 gene들에 대해, Expression level을 3단계로 나눔. 전체 gene의 expression level의 상위 33%를 high, 하위 33%를 low, 중간을 mid로 나눔.
+ 각 gene들에 대해, CV level을 2단계로 나눔. 전체 gene의 CV 값의 상위 50%를 high, 하위 50%를 low로 나타냄. 
+ 아래 표는 분류된 기준에 따른 gene(19,183개)들의 분포.

Data|CV High|CV Low
-|-|-
Expression High|1,699|4,823
Expression Mid|2,435|3,895
Expression Low|5,457|873


+ 아래 표는 Public HKG gene set에 속한 gene(2,177개)들의 분포.

Data|CV High|CV Low
-|-|-
Expression High|49|1,864
Expression Mid|7|196
Expression Low|16|8

+ 알려진 [database](https://pubmed.ncbi.nlm.nih.gov/32663312/)와 CV cut으로 자체적으로 만은 HKG set을 비교했을 때, 교집합은 대부분 CV값이 낮고, 발현량이 높은 gene들이다. 그러나, false positive가 많아, 샘플간 발현량 fold change 등으로 추가 filtering을 통해 HKG gene set을 얻을 예정이다.

### 10. Predicting Tissue-Specific Gene Set.
#### 10-1 Specificity Scoring (Tau) 
+ [선행 연구](https://academic.oup.com/bib/article/18/2/205/2562739#119555200)를 참고해, 해당 논문에서 가장 성능이 우수하다고 하는 Tau scoring을 사용했다. 
+ Scoing equation은 아래와 같다.

<img width="288" alt="image" src="https://user-images.githubusercontent.com/97942772/219707084-a4b75272-dfdf-4108-b6b2-2ceedd576303.png">

Xi : expression of the gene in tissue i
N : Number of tissues

+ Tau scoring의 Xi는 해당 tissue에서의 발현량/모든 tissue에서 가장 발현량이 높은 tissue의 발현량이며, 모든 tissue에서 발현량이 비슷할 경우,  Xi 값이 커짐.
+ 1-Xi는 발현량이 일정할 경우, 값이 작아짐.
+ 따라서, Tau가 높다면, 발현량이 일정하지 않음을 시사함.
+ Tau값은 0-1로, 1에 가까울 수록 발현량이 일정하지 않고, 0에 가까울 수록 발현량이 일정함.
+ 모든 tissue의 gene expression mean을 구함. (/eevee/val/jjpark/TSgenefinding/means/TRANSPOSED_ALL_TISSUE_MeAN.tsv)
+ Tau 값을 구함. (/eevee/val/jjpark/TSgenefinding/means/answers/TAU_SORTED.txt)
+ Tau 값이 75% 이상인 gene들을 잠재적인 tissue-specific gene으로 분류함.
+ Gene 별 Tau 분포는 아래와 같음.

![image](https://user-images.githubusercontent.com/97942772/219711266-f5e3f8d5-0b2c-4e97-8cae-0206c4e52eea.png)

#### 10-2 Predicting Tissue-Specific Gene Set
+ 앞서 filtering된 gene set에 대해, TS gene set을 작성함.
+ TS의 기준은 해당 tissue에서의 발현량이 나머지 모든 조직보다 5배 이상 높은 경우 TS로 분류함(/eevee/val/jjpark/TSgenefinding/means/answers/TS_ENRICHED_GENE_SORTED.tsv). [선행 연구](https://www.science.org/doi/10.1126/science.1260419)를 참고.

![image](https://user-images.githubusercontent.com/97942772/219717074-5e374be8-7820-41f7-8c84-5a1f4227e02c.png)
  + 발현량 cutting 없이, 가장 높은 tissue의 발현량 평균이 다른 모든 tissue의 발현량 평균보다 높은 gene 개수의 분포.
  + anal tissue는 TCGA에서 3개의 sample을 갖고 있어, noise가 심함. 45개의 tissue를 30개로 재조정하는 과정 중에 있음.
  + 전체 개수는 1,374개로 발현량이 낮은 경우, 지나치게 고평가 되는 듯 하여, 다른 조건에서 분포를 확인함.

![image](https://user-images.githubusercontent.com/97942772/219717754-6e0ffd1f-2211-4e0d-9026-0e74476306ae.png)
  + 가장 높은 tissue의 발현량 평균 (GeTMM)이 1 이상이며, 다른 모든 tissue의 발현량 보다 8배 이상 높은 786개의 gene을 선별함.

### 11. Data Supplementary
+ GEO/SRA 데이터 사용을 위해 [ARCHS4](https://maayanlab.cloud/archs4/) database에서 gene level raw count를 다운로드 받음.
+ ARCHS4의 분류 기준은 description에 특정 organ/tissue가 언급되면 해당 tissue로 간주하는 기준임.
+ 따라서, Liver cancer patient의 whole blood인 경우, 두 tissue에서 모두 발견되는 경우가 관찰됨.
+ 정확한 tissue의 분류 기준에 따라, source name이 정확하게 tissue 명인 데이터만 사용함. (e.g. tissue : brain (사용), tissue : brain;thalamus(사용하지 않음.)))
+ 앞서 작성한 데이터와 교집합이며, 발현량이 높으며, major tissue 30개로 재조정함. 
+ 전체 8,747개의 sample을 추가함. 
+ defaultdict(<class 'int'>, {'Bladder': 8, 'Brain': 584, 'Kidney': 277, 'Spleen': 43, 'Liver': 1938, 'Blood': 3970, 'Uterus': 1, 'Lung': 382, 'Breast': 197, 'Thyroid': 59, 'Stomach': 29, 'Testis': 35, 'Skin': 236, 'Prostate': 105, 'Adipose Tissue': 402, 'Pancreas': 109, 'Heart': 157, 'Esophagus': 32, 'Ovary': 30, 'Thymus': 59, 'colon': 94})
