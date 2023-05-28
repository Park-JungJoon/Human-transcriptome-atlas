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

------

# PART C. Web DB Constructure
## 11. Program Selection
+ [Django](https://docs.djangoproject.com/ko/4.2/intro/)를 통해 Web App 구축을 하고자함.
+ 아래와 같은 이유로 Django를 선정함
  + Gene별 URL 이동이 Shiny를 통한 구현이 어려움.
  + Django 사용시 어려운 점은 Model - View - HTML templates - User 등의 복잡한 구조를 통해 구축하는 점인데, Shiny R/Python을 통한 구축 시에도 참조한 사이트에서 Django와 비슷한 구조로 구축함. 
  + 이후 scRNA-seq 데이터 베이스를 구축할 때, 완성도 높은 사이트를 만드려면 필수적이라고 판단함. 
 
## 12. Dataset Making
<img width="502" alt="image" src="https://user-images.githubusercontent.com/97942772/236738938-24117b48-1392-4516-b6e2-e65479d1bf19.png">

+ 위의 [Human Protein Atlas](https://www.proteinatlas.org/ENSG00000131095-GFAP)를 참조하여 사이트를 구상중에 있음
+ Gene-Centric page에서는 HKG/TS 분류 및 Promoter information, Expression box plot을 포함하는 정보를 제공하고자 함.
+ 검색 창을 통해 원하는 ENSG number을 통해 넘어가고자함. 

+ '/eevee/val/jjpark/webservice/data_back/boxplots/' 디렉토리에 아래와 같은 gene 1개에 대한 box plot을 3개 DB를 대상으로 총 57,454개 저장함.

![GEO_ENSG00000121410](https://user-images.githubusercontent.com/97942772/236739619-770f0af5-4fe3-4952-bacd-baf3d5973f58.png)

+ 위와 같이 구성한 이유는, 유저의 request마다 plot을 계산해야하는 메모리 부담을 덜고자 함. 
+ 이외에도, web DB에 필수적인 meta data, tissue mean expression table등의 backend data를 /eevee/val/jjpark/webservice/data_back/에 저장함.

## 13. Web DB Coding
+ Leafeon 서버에서 작업중에 있음.(/leafeon/analysis1/jjpark/atlas_webapp)
+ Shiny for Python을 이용해 작업중에 있음.
+ 크게 3 페이지로 나누고, 첫번째 페이지에서는 Gene-Centric analysis 결과를 보고하고자함. 
+ Gene의 TS/HKG 여부, Promoter information 등의 정보를 제공함. 
+ 이외에도, 3 database의 boxplot의 정보를 공개함. 
+ 아래 이미지와 같게 기능 구현함. 

<img width="849" alt="image" src="https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/ab6b5e52-772d-4422-954e-37620f189138">

+ UI 개선 및 이미지 해상도 조절 등의 세부 조정 사항이 필요함.

<img width="467" alt="image" src="https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/615ba59c-dfd3-48c5-89fe-74b90d0d3c18">
<img width="311" alt="image" src="https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/698b6233-4b67-488c-9a47-524ad2399403">

## Next Week Goal
+ UI 개선
+ 두번째 Data Download page 개선


# PART D. Highlight
## 14. Tissue Specific Gene from Non-major Tissue
+ 연구가 많이되지 않은 minor tissue에 대한 TS gene에 대한 종합적인 분석을 연구의 첫 번째 Highlight로 삼고자 합니다.
+ 먼저, 현 사용되고 있는 TS score에 대한 조사를 진행함. 

![venn_result8525](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/51731c22-77f5-4157-85da-407d823559ba)

  + [Human Protein Atlas](https://www.proteinatlas.org/)에서 조직 특이적인 10,987개의 유전자 전체에 대한 벤다이어그램
  + Enriched는 모든 조직에 비해 5배 이상의 발현량을 갖는 경우, Group Enriched는 2-5개의 tissue가 5배 이상의 발현량을 갖는 경우, Enchanced는 2-5배의 발현량을 갖는 경우이다.
  + 현재 TS cut (TS score 1 이상, 1개 이상의 DB에서 tissue specific gene일 경우)는 과도하게 strict함. 
  + 이에 따라 Tau Value를 조정해 점수를 보완할 필요성이 있음.
+ 현재 데이터에서 TS 로 분류하나, Human Protein Atlas에서는 Specificity가 보고되지 않은 9개의 유전자에 대해 자세히 조사함. 
+ 크게 원인은 3가지로
  + Expression level이 낮은 gene이라, 우리 데이터 셋에서 filtering 되지 않았으나, Human Protein Atlas에서는 filtering된 경우
  + GTEx, TCGA에서 TS gene으로 분류된 경우, 사용된 DB가 다르기 때문에 다르게 지정된 경우
  + Human Protein Atlas에 없는 gene일 경우가 있음.
+ Tau value, Decision Tree를 이용한 Scoring 기준을 보완한 후 TS gene finding을 진행하고자 함.

## 15. SEG / MEG 
+ 다른 highlight의 대상으로, SEG/MEG에 따른 expression pattern을 대상으로 삼고자 함.



## Next Week Goal
+ TS scoring funciton 확립, TS gene에 관련한 Highlight 연구
