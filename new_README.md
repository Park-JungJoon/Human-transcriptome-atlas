# Human Transcriptome Atlas
본 연구에서는 Public bulk-RNA seq database의 데이터를 취합하고, 종합적인 분석 결과를 웹 앱을 통해 공개하는 것을 목적으로함.

----

</br>

# PART A. Data Collecting / Merging 
## 1. Data Collecting
+ Public Human Transcriptome Database는 대표적으로 GEO, GTEx, TCGA가 있음.
+ 위의 데이터 베이스 중, GEO는 각 연구 별 자료의 형식이 통일되어 있지 않아, [ARCHS4](https://maayanlab.cloud/archs4) database에서 gene level raw count를 다운로드 받음.
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

+ 새로운 데이터로 통합중에 있습니다. Visualization 끝나는대로 업데이트 하겠습니다.

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

+ 현재 Panpyro Rstudio의 문제로, plotting만 못했습니다. [Supplementary data](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplymentary%20Data/R_data_april_embedding_nn_10_mindis_0_1.csv)에 csv coordinate 파일을 업로드하였습니다. 월요일 오전중에 업데이트 하겠습니다.

</br>
</br>

------

# PART B. Data Handling
## 6. Global Normalization
  + Sample 간 비교를 위해 read depth (library size) 보정과, gene lenth 보정이 필요함. 
  + 두 보정법을 모두 차용한 [GeTMM](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2246-7) 을 사용함.
  + GeTMM의 경우, RPK를 계산한 후 (Gene length 보정) 이후 edgeR 모듈의 TMM 계산 과정을 거침. 
  + TCGA의 경우, FPKM으로부터 Gene Length를 계산하였고, GTEx는 자체적으로 사용하는 Gene Length를 파싱하여 사용함.
+ RPK를 계산한 파일을 (/panpyro/alfa/jjpark/adjusted_merge/split_by_db/output_of_R)에 저장하였음.

## 7. House Keeping Gene Searching 
  + 표준 편차를 산술 평균으로 나눈 CV(coefficient of variation)값을 HKG 지표로서 사용함.
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
  + 알려진 [database](https://pubmed.ncbi.nlm.nih.gov/32663312/)와 CV cut으로 자체적으로 만은 HKG set을 비교했을 때, 교집합은 대부분 CV값이 낮고, 발현량이 높은 gene들이다. 그러나, false positive가 많아, 샘플간 발현량 fold change 등으로 추가 filtering을 통해 HKG gene set을 얻을 예정이다.

## 8. Tissue Specific Gene Searching
### 8-1. Tau pre-filtering
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
### 8-2. TS Gene Searching by expression level, fold change
  +  Tau percentile 25%, expression > 500, Foldchange 5의 기준으로 세 데이터 베이스 각각 tissue specific gene을 조사함. 각 데이터 베이스에서 TS gene 개수가 상위 5개인 조직과, TS gene 개수 분포는 아래와 같음.
  
  + GEO : 1979 TS genes

Tissue|Count
-|-
Liver|344
Pituitary|269
Blood|213
Testis|164
Kidney|145



  + GTEX : 3022 TS genes

Tissue|Count
-|-
Testis|1597
Liver|245
Brain|167
Muscle|131
Skin|131

  + TCGA : 1559 TS genes

Tissue|Count
-|-
Brain|301
Liver|262
Testis|179
Adrenal_Gland|97
Thymus|95

  + Intersection : 390 TS genes

Tissue|Count
-|-
Liver|167
Brain|61
Testis|61
Pancreas|21
Blood|20

### 8-3. Group Enriched Genes
  + Group Enriched Gene은 2-6개의 tissue에서 나머지 tissue에 비해 5배이상 발현된 gene을 뜻함. [선행연구 참조](https://www.science.org/doi/10.1126/science.1260419) 각 DB 별 GE (Group Enriched)의 분포는 아래와 같음. Tissue 별 count는 중복되게 셈.

  + GEO : 745 GE genes

Tissue|Count
-|-
Kidney|713
Liver|379
Blood|310
Spleen|259
Esophagus|211

  + TCGA : 479 GE genes

Tissue|Count
-|-
Liver|265
Lymph_Nodes|249
Blood|228
Large_Intestine|194
Adrenal_Gland|174

  + GTEX : 326

Tissue|Count
-|-
Blood|196
Muscle|151
Liver|139
Heart|131
Blood_Vessel|83

  + 세 데이터 베이스에서 tissue 조합이 같으며, GE인 gene은 없다. 

## 9. Single Exon/ Multi Exon Genes
  + Human Single Exon Gene Database [SinEx2](https://v2.sinex.cl/)에서 1,793개의 gene을 Inronless gene (Single exon gene)으로 정함.
  + 1,9151개의 Protein coding gene에 대해, DB별 TS/HKG/exon type을 기재한 파일을 "/eevee/val/jjpark/RNA_SEQ_ATLAS/four_intron/GENE_ALL_INFO_TS_HKG_INTRON.tsv"에 저장함.

  + 먼저, 각 DB 별 MEG(Multi Exon Gene) 대비 각 조직 별 평균 SEG 발현량 box plot은 아래와 같음
  + x축은 tissue, 각 box의 component는 해당 tissue에서 발현되는 gene의 평균 발현량이다. SEG와 MEG를 따로 표기하고, y축은 로그 스케일.

  + GTEX

![gtex_boxplot](https://user-images.githubusercontent.com/97942772/224544705-77081eed-2b17-47e1-949a-39d5e0a4813c.png)

  + GEO

![geo_boxplot](https://user-images.githubusercontent.com/97942772/224544730-98340fb3-0437-4b59-9ac5-62c522e656da.png)


  + TCGA

![tcga_boxplot](https://user-images.githubusercontent.com/97942772/224544763-d894fd03-6aa6-4d8a-a621-40a9f7088ca1.png)

  + 세 데이터베이스에서 모두 SEG는 MEG에 비해 현저히 낮은 발현량을 보임. Intron이 Expression level regulation을 하기에, 그 영향을 받지 않는 것으로 사료됨.
  + 앞서 언급한, DB별 TS/HKG/exon type을 기재한 파일을 토대로, TS와 HKG에서 SEG가 차지하는 비중을 확인함.
  + SEG는 1,793개로, MEG의 약 10%임.
  + 2개 이상의 DB에서 TS/HKG로 분류된 gene을 TS/HKG로 규정하고, TS의 MEG/SEG 비율 분포를 확인함.

TS score 0.6 이상, HKG score 1.5 이상을 각각 TS, HKG로 규정함.

Type|TS|HKG
-|-|-
MEG|3,631|4,821
SEG|464|90


+ TS의 경우, MEG/SEG의 비율이 대략 10배로 전체 gene pattern과 비슷하나, HKG의 경우 50배 이상이 차이남.

## 10. Promoter anlaysis
  + [EPDnew](https://epd.epfl.ch/human/human_database.php?db=human) 데이터 베이스에서 human promoter sequence를 모두 얻음.
  +  16,246개의 gene에 대해 promoter sequence (-50 ~ 10 bp from transcription start site.), major motif  (TATA box, Initiatie region, CCAAT box, GC box), promoter type ([Dreos et al., 2016](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005144)) 정보를 다운로드 받음.
  +  앞선 7-9 까지의 연구 내용;각 DB 별 TS / HKG prediction, TS score, SEG/MEG 와 Promoter comprehensive information을 포함한 Gene-centric data table을 만듦. (/eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/new_d_ts/FINAL_ver1.tsv) [link](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Supplymentary%20Data/GEECENTRIC_TABLE_FINAL.tsv)
