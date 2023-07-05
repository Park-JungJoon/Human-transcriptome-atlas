# Semi Report

****

# A. Data Collecting, Handling
## A-1. Raw data distribution
  + Total Sample : 46,813
  + Data Source : GEO, GTEX, TCGA gene raw matrix (GEO from ARCHS4)
  + Meta Data 
    - GTEx, TCGA : Tissue, Age, Sex
    - GEO : Tissue
## A-2. Data Handling
  + Gene 
    - Gene symbol substituted as ensembl gene id. Ignore ensembl id version (ENSG000001234.4 > ENSG000001234)
    - Using only intersection protein coding gene (19,151 gene)
  + Tissue
    - Major 30 tissues (all tissues have more than 100 samples in total across the three databases)
## A-3. Normalization
  + [GeTMM](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2246-7) used.
  + Considering gene length, library size.

# B. House Keeping Gene
+ Criteria : Coefficient Variants(CV), Expression percentile (ignoring low expression genes.)
+ CV top 50%, expression top 33%.

</br>

+ 추가 하고자 하는 기능 : 현재 CV와 expression level 만 고려하는 것이 설득력이 적어보여, 가장 높게 발현하는 조직의 발현량 / 가장 낮게 발현하는 조직의 발현량 Foldchange 4 (4는 현재 Tissue specificity에서 사용하고 있습니다.)을 넘지 않는 gene.

# C. Tissue Specificity [More info 06/18](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Weekly%20Report.md)
+ Criteria
  - [Tau](https://academic.oup.com/bib/article/18/2/205/2562739) : 0-1 scale. 1 is tissue-specific. 

<img width="300" alt="image" src="https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/8b7f2cfb-4a47-4c59-bef4-b2aaec2ea9ee">

<img width="300" alt="image" src="https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/83938eaa-20a3-42f6-9994-5bc6724c172e">

  - Foldchange : 조직의 평균 발현량을 기준으로 제일 높은 평균 발현량을 갖는 조직 / 두번째로 높은 평균 발현량을 갖는 조직.
  - TS score : [z-score normalized(Tau) + z-score normalized(FC)] : 3 database 평균
  - Tau 는 2 조직에서 과발현 되는 경우와, 1 조직에서 과발현되는 경우에 대한 뚜렷한 차이가 없음. (조직이 많기때문)
  - FC는 3번째 이후로 과발현 되는 조직의 발현이 조절되지 않음.
  - 위와 같은 이유에서 두 값의 합으로 사용하며, Z-score normalization은 DB별 weight를 맞추기 위해서 사용함. (일반적으로 GTEx의 FC, Tau값이 높음.)

</br>

+ 개선점 : 3 DB에서 모두 존재하지 않고, 2개 DB에 존재하거나, 1개 DB에 존재하는 경우 TS score가 보정받지 못함.
+ 고안하고 있는 해결책 : 2개 DB의 경우 2개 DB의 값만 계산하고, web app serving시 2개 조직에만 있다고 표기함. (low consensus)


# D. Promoter
+ [EPD](https://epd.expasy.org/epd)에서 human protein coding gene 데이터 다운로드.
+ 전체 gene (19,251) 중, 16,000 정도 promoter information이 있음.
+ EPD에서 제공하는 Promoter type, Motif infos, Promoter sequence 등이 있음.

# E. Single Exon Gene, Multi Exon Gene
 + SinEx2에서 1,793개의 gene을 Inronless gene (Single exon gene)으로 정함.
 + 우리 데이터셋에 기재함.

# F. Tissue Classifier
+ Python sklearn module 내에 있는 multinomial classifier 통해서 구축함.
+ Hyper paramter optimization 완료 [More info. 07/02](https://github.com/Park-JungJoon/Human-transcriptome-atlas/blob/main/Weekly%20Report.md)

# G. Paper Work
+ 논문 abstract, introduction, method 작성 중에 있음. 
