[This Week Weekly Report](#23/06/18)


# 23/06/11
## Topics
1. Human tissue specific genes/expression - biomarker/profiles

2. new discovery? comparing to known/previous results

3. Predictor

4. Environmental disease transcriptome

## Progress
### 1. Human tissue specific genes/expression - biomarker/profiles

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/a0c9f820-1f72-4213-b187-7813ac92c361)

+ Human Protein Atlas와 현재 TS 데이터셋 간 비교 
+ HPA 에서 Tissue enriched로 정의하였으나, TS gene으로 detected 되지 않은 1,638개 gene의 이유에 대한 분포. (원인 중복 포함 count)

Standard|GTEx|TCGA|GEO|Sum
-|-|-|-|-
FC|1,207|1,385|1,303|3,895
Tau|550|680|712|1,942
Expression|147|152|161|460
Sum|1,904|2,217|2,176|6,297

+ Tau pre-filtering의 기준점을 현재 상위 25%에서 50%로 하향 조정할 예정. 
+ Expression pre-filtering의 기준점은 현상 유지(상위 90%)하도록 함. 
+ Fold Change에 의해 TS로 분류되지 못함. 현재 FC 4로 고정하고, Tau등의 추가적인 parameter으로 detecting rate을 높이고자함. 

#### 1-1. Foldchange
![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/550163ad-801f-4827-aaa1-7b1dbba9bf87) 

+ y축을 로그 스케일로 정의해, 분포가 역으로 이뤄져있음. 
+ log(FC+10)의 슈도카운트를 적용했을 때 density plot (FC는 가장 많이 발현된 조직의 평균 발현량 / 두번째로 많이 발현된 조직의 평균 발현량)으로 정의함. 
+ TCGA가 FC가 높은 경우가 많이 관측되나, 위의 표에서 제시된 바, 특정 DB가 TS의 정의에 영향을 크게 주지 않는 것으로 파악됨. 

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/c302decb-4352-40cc-b5d8-f1e893eac5b5)

+ HPA에서 정의한 Tissue enriched / Tissue enhanced / Group enriched gene의 FC의 percentile 분포.


#### 1-1. Tau
+ DB별 Tau 분포. 


![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/8eb18485-06bf-4c4d-b167-97f21bc966fa)

+ HPA에서 정의한 Tissue enriched / Tissue enhanced / Group enriched gene의 Tau 분포. 

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/dd937994-2321-4bb9-8c67-bf5209379489)
 
+ HPA에서 정의한  Tissue enriched / Tissue enhanced / Group enriched gene의 Tau의 percentile 분포.

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/ae600a61-73fd-466f-94e4-a5f5a74936e5)


#### Result
+ FC의 percentile과 Tau  두 값 모두, HPA의 Tissue enriched gene의 경우, Tissue specificity가 없는 그룹(Else)간의 차이가 명확함. 
+ FC percentile, Tau를 고려하여 TS scoring function을 재조정하고, 개수를 약 1,100개에서 3,000개 이상으로 재조정하고, HPA 이외의 DB와 비교할 예정임.
+ Parameter들을 적용해서 사용할 수 있는 새로운 gene profile을 코드와 함께 '/eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/ts_scoring_new'에 저장함. 이를 적용해 다음 주에 기준을 적용 / biomarker 발굴을 할 예정임.


</br>

****



# 23/06/18
## Summarize of Last Report
+ Tau, Fold Change 등의 데이터 분포 시각적 확인
+ [Human Protein Atlas](https://www.proteinatlas.org/)의 데이터 셋을 비교군으로 삼고, DB 2개 이상에서 같은 Tissue Specific이라고 지정한 gene을 TS gene이라고 정함. 
+ 총 1,110개의 gene 중에, HPA에서 Tissue specificity를 가지지 않는 유전자라고 정의한 유전자는 총 9개임.
+ 9개 유전자에 대한 분석 결과, HPA에서 분석 대상으로 삼지 않는 Blood tissue이거나, 발현량이 너무 낮아 HPA에서 pre-filtering된 것으로 추정됨.
+ 기존의 TS score 기준이 너무 harsh해서, Tissue specity 관련 highlight를 찾기 어려워, TS scoring function의 재조정이 필요함. 

## 1. TS score Definition 
- Gene 마다 3개의 DB에서 Most expressed tissue가 다른 경우가 있고, 이 경우에 단순 Foldchange를 사용하는 경우, Tissue specificity가 왜곡되므로, Tissue distribution을 1개의 기준으로 삼음.
  + 3개 DB에서 모두 같은 경우 1점, 2개 DB에서 모두 같은 경우 0.5점, 3개 DB에서 모두 다른 경우 0점을 사용함. 
- Tau값을 사용함. Tau 의 경우, Tissue Specificity를 전반적으로 파악하는데 매우 유용하나, 특정 2개 tissue에서 매우 높은 발현량을 가지고, 나머지 Tissue에서 매우 낮은 발현량을 가질 때에도 높은 값을 가지기 때문에, 특정 1가지의 Tissue Specificity를 포함하는 정보를 제공할 수 없음.
  + Mean Tau (3 DB)를 Score function으로 사용 
- 이에 Foldchange Percentile을 사용함. (Raw foldchange를 사용했을 경우, Tau와 같은 weight으로 반영되지 않음.)
  + Mean FC Percentile (3 DB)를 Score function으로 사용


![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/c5bde3f9-09d2-4b7c-a9de-a209c3dae9a8)

+ TS score의 분포, 2.5 이상의 gene을 TS score 으로 분류하고, 1,521개의 분포를 보임. 지난 주 연구의 1,100개 보다 많은 양의 Gene을 detecting함. 

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/ddb565bb-43bb-41df-a782-14f817c5514f)

+ HPA(enriched , enhanced, group enriched 와, 기존의 standard (FC >4, Tau percentile > 0.75, Expression percentile > 0.2)를 한개의 DB에서라도 넘긴 gene set에 대한 벤다이어그램. 
 - HPA에서 3단계로 나뉘는데, (Enriched > Group Enriched > Enhanced) 순이며, 너무 넓은 범위 (10,000개 이상을 TS gene으로 분류함)를 포함함. 

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/479fd2a4-e70d-4a8f-bb5f-991020a4bac5)

+ HPA에서 가장 높은 Tissue Specificity를 보이는 3,361개의 Tissue Enriched 데이터 set과, 앞선 2개의 데이터 set 벤다이어그램.
 - TS score > 2.5이며, 기존의 TS finding 기준에도 부합하는 389개의 gene에 대한 mannually gene annotation analysis를 진행함. 
 - ENSG00000125618와 같이 Thyroid Specific gene이며, 이전의 다른 Paper에서 그 기능과 tissue specificity가 보고된 유전자이나,  HPA에서 분류하지 못한 gene이 있음 (ENSG00000160781,ENSG00000176894)
 - 그러나, 아직도 Blood Brain과 같이 data set의 차이에 기인한 유전자들이 여집합이 대부분을 차지하고, TS score의 문제점을 파악함. 

## 2. TS score supplementary
+ 이전에 고안한 TS score에 대한 문제점
 - 1. Expression Pre-filtering 이 충분히 이뤄지지 않음. 
 - Expression이 낮은 gene의 경우, psuedo count (0.001)의 영향으로 fc가 200,000이 나오는 경우가 있음.
 - 이런 경우, HPA, gencard, archs4 등의 선행연구에서도 tissue specific하지 않은 발현 패턴을 보이는데 TS 로 분류되는 경우가 빈번함. Noise로 판단함.
 - Expression Level Pre-filtering 기준을 가장 높은 tissue의 평균 발현량이 1 (GeTMM)  이상으로 상향 조정하고, GEO, GTEx, TCGA 3 database 중 어느 하나의 DB에서라도 위 조건에 맞지 않으면 filtered함. 
 - 2. FC Percentile은 분산을 반영하지 못함.
 - 3. DB간 mean fold change에 차이가 있어, 단순 평균으로 계산할 경우 특정 DB의 발현 패턴이 TS scoring에 편향되어질 것으로 예상함. 
 
 ![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/556e8bf7-7ed7-42b7-a416-6f6edc97fcb2)
 
 - 위와 같이, GTEx의 평균 Foldchange가 높게 책정되어있음. 
 - 2,3 번 문제점의 해결으로, fold change의 z-score를 만들어 scoring function에 사용하고자함. 
 - 추가적으로, raw foldchange를 사용할 경우, 정규분포화에 어려움이 있어 Log FC를 사용함. 

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/78ed487b-ea4a-4cb1-9c0b-b2f232ac20d8)

+ 위와 같은 분포의 TS score를 얻음.

Total Gene | 17,249
-|-
TS score > 1 | 3,643
TS score > 1.5 | 1,996
TS score > 2 | 1,077

+ 앞선  TS score가 5 이상인 15개의 gene 중 10개 gene에 대한 tissue-specific과 관련된 문헌은 아래와 같음.

Ensembl Gene ID | Tissue | Paper
-|-|-
ENSG00000042832  | Tyroid | [Paper](https://link.springer.com/article/10.1007/s12022-018-9532-9)
ENSG00000080910   | Liver | -
ENSG00000117601    | Liver |[Paper](https://www.liebertpub.com/doi/full/10.1089/omi.2015.0088)
ENSG00000055957    |Liver|[Paper](https://www.nature.com/articles/s41467-021-25546-y)
ENSG00000167751 | Prostate | [Paper](https://www.degruyter.com/document/doi/10.1515/BC.2001.002/html)
ENSG00000110243|Liver| Funtionally Tissue Specific
ENSG00000134389   | Liver | Reported in nephropathy; *
ENSG00000091583 | Liver | Funtionally Tissue Specific
ENSG00000122304   |Testis|[Paper](https://www.jbc.org/article/S0021-9258(20)65481-3/abstract)

+ 위의 표와 같이, TS scoring function이 단순 TS-gene 분류 뿐만이 아니라, 연속적인 값으로서 매우 높은 값을 갖을 때, biomarker 발굴에 직접적으로 사용가능함을 시사함.

## 3. TS score Problems
+ 3개의 database를 사용하며, 특정 db에만 존재하는 tissue들이 있음. 
+ 예를 들어, Muscle의 경우에 GTEx에만 존재하는데, 기본적인 Tissue distribution 계산값이 0으로, (나머지 두 DB에선 없으므로) TS scoring에서 매우 불리한 위치에 있음.
+ Expression이 3개 DB중 하나라도 1이 안되면 사용하지 않음. 약 2,000개 가량의 gene에 대한 추가적인 연구의 진행이 없음. 


****** 
지난 주 말씀하신 huge table directory 입니다. 연구 중 수정을 거듭해, 이번 주에 보고드립니다.
All intersection protein gene :/eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/ts_scoring_new/ALL_INFOS_TABLE.tsv  
Highly Expressing Gene : /eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/ts_scoring_new/ESSENTIAL_17000_INFOS.tsv,  /eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/ts_scoring_new/Z_scored_17000_ALL_INFOS.tsv
