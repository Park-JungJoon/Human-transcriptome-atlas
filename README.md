# Human-transcriptome-atlas
## 1. Data Collecting
+ High throughput seqeuncing, Homo sapiens에 해당하며, sample 개수가 6-100개, Gene count table이 담긴 supplementary에 파일이 있는 모든 데이터를 [GEO datasets](https://www.ncbi.nlm.nih.gov/gds) 연구대상으로함.(18,676개)
+ 앞선 18,676개의 데이터 중, 사람과 다른 동물간의 발현차이를 보이는 연구 결과는 제외함.
### 1-1. Data filtering
+ GEO dataset 중, 이용하고자 하는 발현량을 나타내는 표는 GSE, GSM 두가지 포맷을 사용할 수 있음.
  + GSE의 경우, 해당 연구의 전체 샘플을 요약하여 나타내는 포맷임.
  + GSM의 경우, 각 샘플을 요약하여 나타내는 포맷임.
  + 일부 연구는 GSE로 통합하지 않고, 각 GSM파일을 묶어서 업로드 되어있음.
  + 위와 같은 경우에서, BAM과 같은 raw data가 포함되어 있으며, 파일의 용량이 30기가 이상이므로, 연구 대상에서 제외함. 
  + 위의 경우, 확장자는 tar 확장자를 사용함. 

+ GSE에 포함되는 데이터 중, 유전자 발현량을 나타내는 표를 사용하고자함. 각 연구 별 gene count table의 양식과 포함하는 정보가 상이함.
  + 대부분의 데이터는 csv,tsv,txt와 같은 확장자를 가진 gene count table 이외의 부가적인 정보를 담고 있음. 
  + 일부 데이터는 raw count없이 보정값(RPKM,CPM,FPKM 등)만을 포함함.
  + 일부 데이터는 단순한 count 이외의 유전자 서열 등의 추가적인 정보를 포함함.
  + 일부 데이터는 샘플 별로 나눠, 전체 분포를 한 파일로 읽을 수 없음.
  
### 1-2. Toy set counting
+ 1-1의 데이터들의 경우, 0.1version의 데이터에 포함시키기 기술적인 어려움이 있음.
+ 1-1에 포함되는 데이터와, 사용가능한 데이터의 분포를 알아보기 위해 250개의 GEO dataset을 다운로드 받고, 1-1의 기준에 따른 일차적인 filtering을 거침.
  + GSE를 제외한 나머지 데이터는 제외함. 
  + txt, csv, tsv 포맷의 데이터만 포함함.
  
+ 초기 연구 대상으로 사용가능한 데이터는 아래와 같은 성질을 띔.
  + 보정값이 아닌, raw count만을 포함함.
  + Table 안에 샘플, 유전자, 발현량의 정보 외의 다른 정보를 포함하지 않음.
  + 여러 샘플이 한 파일 내에 묶여있음.

+ 250개 data에 대한 분포는 아래 표와 같다.
  |Total|Available|Normalized data|Non available|
  |-|-|-|-|
  |239|59|74|111|
 + 연구 데이터 기준으로, 250개의 연구 중, 52개의 연구가 바로 사용가능한 형식이다. 

## GEO 이외의 다른 플랫폼에서 제공하는 RNA-seq 데이터
+ GTEx : 11,688 samples (53 tissues, over 250 individuals)
+ TCGA : 11,077 samples (tumor only)
+ 위 두 플랫폼에서 제공하는 RNA-seq 데이터는 별도의 가공이 불필요함.

