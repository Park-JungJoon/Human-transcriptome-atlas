[This Week Weekly Report](#my-anchor)


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
[ENSG00000042832](https://www.genecards.org/cgi-bin/carddisp.pl?gene=TG&keywords=ENSG00000042832)  | Tyroid | [Paper](https://link.springer.com/article/10.1007/s12022-018-9532-9)
[ENSG00000117601](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SERPINC1&keywords=ENSG00000117601)    | Liver |[Paper](https://www.liebertpub.com/doi/full/10.1089/omi.2015.0088)
[ENSG00000055957](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ITIH1&keywords=ENSG00000055957)    |Liver|[Paper](https://www.nature.com/articles/s41467-021-25546-y)
[ENSG00000167751](https://www.genecards.org/cgi-bin/carddisp.pl?gene=KLK2&keywords=ENSG00000167751) | Prostate | [Paper](https://www.degruyter.com/document/doi/10.1515/BC.2001.002/html)
[ENSG00000110243](https://www.genecards.org/cgi-bin/carddisp.pl?gene=APOA5&keywords=ENSG00000110243)|Liver| Funtionally Tissue Specific
[ENSG00000134389](https://www.genecards.org/cgi-bin/carddisp.pl?gene=CFHR5&keywords=ENSG00000134389)   | Liver | Reported in nephropathy; *
[ENSG00000091583](https://www.genecards.org/cgi-bin/carddisp.pl?gene=APOH&keywords=ENSG00000091583) | Liver | Funtionally Tissue Specific
[ENSG00000122304](https://www.genecards.org/cgi-bin/carddisp.pl?gene=PRM2&keywords=ENSG00000122304)   |Testis|[Paper](https://www.jbc.org/article/S0021-9258(20)65481-3/abstract)

+ 위의 표와 같이, TS scoring function이 단순 TS-gene 분류 뿐만이 아니라, 연속적인 값으로서 매우 높은 값을 갖을 때, biomarker 발굴에 직접적으로 사용가능함을 시사함.

## 3. TS score Problems
+ 3개의 database를 사용하며, 특정 db에만 존재하는 tissue들이 있음. 
+ 예를 들어, Muscle의 경우에 GTEx에만 존재하는데, 기본적인 Tissue distribution 계산값이 0으로, (나머지 두 DB에선 없으므로) TS scoring에서 매우 불리한 위치에 있음.
+ Expression이 3개 DB중 하나라도 1이 안되면 사용하지 않음. 약 2,000개 가량의 gene에 대한 추가적인 연구의 진행이 없음. 


****** 
연구 중 사용된 raw 및 merged table 디렉토리입니다.
<br/>
```
/eevee/val/jjpark/atlas_report/final : 현재 연구의 최종 결과본으로, 해당 디렉토리 내 README.txt에 column 설명을 했습니다.
/eevee/val/jjpark/atlas_report/normalized : raw gene count table을 normalized한 결과입니다.
/eevee/val/jjpark/atlas_report/raw : raw gene count table(read)입니다.
/eevee/val/jjpark/atlas_report/RENEWAL_META_MAJOR_TISSUE.tsv :  메타데이터입니다.
```

# 23/07/02
## Summarize of Last Report
+ TS score을 통해 연속적인 tissue-specificity 파악 및 분포, 검증
## This week goal
+ Multi Nomial Classifier in python

## 1. Using Dataset

+ Normalization method가 다를 경우, 학습된 데이터와 다르게 판별함.
+ 현재 사용하는 normalization method([GeTMM](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2246-7))을 사용할 경우, Input data를 raw로 받을 때, 계산량이 너무 많음.
+ Library size로만 보정한 CPM 을 normalization method로 사용함.
+ 3개 DB의 Gene count matrix를 CPM으로 새로 보정함.

## 2. Classifier Model Selection
+ Classifier로 적합한 Model을 선정함에 있어 주요하게 생각한 기능.
 - Multinomial classification의 코딩이 python 환경에서 자유로울 것. (Web DB 공개가 Shiny for python으로 진행되기 때문.)
 - Multithread 기능을 자유롭게 사용할 수 있을 것.
 - Predicted class를 차등적으로 predicted probability와 함께 제공가능할 것.
 - 계산 시간이 느리지 않을 것.
 - Determining gene (feature)의 확인이 가능할 것. 
+ 위의 기준에 적함한 sklearn의 Randomforest를 사용함.

## 3. Hyperparameter Optimization
+ Input 데이터로는 3개 DB의 Gene expression matrix(CPM normalized)를 사용하고, 첫 column은 tissue임.
+ TS 연구에 사용된 17,231개의 Gene (used as X), 30개의 tissue (used as Y)로 나뉘어진 46831개의 sample로 구성되어 있음.
+ test size 0.4, train size 0.6으로 진행함.
+ Optimization에 활용된 코드는 아래와 같음.

```
from sklearn.model_selection import GridSearchCV
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import multiprocessing
import time
start = time.time()
df = pd.read_csv('MERGED_cpm_gene_count_table.tsv',sep = '\t')
print("Reading : ", time.time() - start)
X = df.iloc[:, 1:]  # Exclude the first column (assumed to be the "Gene" column)
y = df.iloc[:, 0]   # Select the first column as the target variable
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
# Set the number of threads to use
num_threads = 28
n_jobs = multiprocessing.cpu_count() if num_threads == -1 else num_threads
# Optimize the number of trees
params = { 'n_estimators' : [i for i in range(10,101,10)],
           'max_depth' : [i for i in range(2,11,2)],
           'min_samples_leaf' : [i for i in range(2,19, 6)],
           'min_samples_split' : [i for i in range(4,25,4)]
            }
rf_clf = RandomForestClassifier(random_state = 0, n_jobs = 6)
grid_cv = GridSearchCV(rf_clf, param_grid = params, cv = 3, n_jobs = 4)
grid_cv.fit(X_train, y_train)
print('최적 하이퍼 파라미터: ', grid_cv.best_params_)
print('최고 예측 정확도: {:.4f}'.format(grid_cv.best_score_))
print("Finishing : ", time.time() - start)
```

+ n_estimator 은 10 - 100을 10간격으로 10개, max_depth는 2-10을 2 간격으로 5개, min_samples_leaf는 2-18을 6간격으로 3개, min_samples_split은 4-24를 4 간격으로 6개 확인함.
+ 최적화된 Parameter는 아래와 같음.
+ 'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 12, 'n_estimators': 80
+ 위 Parameter로 accuracy는 0.9382 임.
+ 위 코드를 실행하는데 15,473초 (4시간 30분) 가량 소요됨. (eevee, thread 28)
+ Optimized option으로 model 구축을 했을 때, 19분 소요됨.
+ 위 Option으로 구축한 model은 pkl으로 "/eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/tissue_classifier/0702_random_forest_model.pkl" 에 저장함.
+ Paramter중 max_depth는 지정한 범위의 최대, min_samples_leaf는 최소이지만 default로, 최적화를 위해 depth를 변경하여 다시 작업하는 과정 중에 있음.
+ 추후 연구에 모델을 저장하고, input으로 raw gene matrix를 받을 때, normalization과 함께 tissue predictor를 제공하는 기능을 자동화하여 web에서 구현하고자 합니다.

# Nest Week Goal
+ Web DB construction
+ 논문 작성 (Introduction, Method)


# 23/07/15
## Summarize of Last Report
+ Tissue Classifier, paper draft.

## This week goal
+ Re-working HKG
+ Re-working Gene Info Page (Web App)

## Re-working HKG
+ 기존의 HKG에서 사용한 method는 Coefficient Variants 하위 50%, Expression Percentile 상위 33%인 gene을 각 DB 별로 조사함. 이후에 3 DB에서 모두 존재하는 gene을 HKG로서 정의함
+ 위의 기준이 과학적이고, 별도의 기준이 없어, TS scoring에서 사용된 GeTMM 1이상의 gene을 사용하고자함.

### 1. CV distribution

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/cfd76ef9-72d3-4360-a0e3-d1c062b2a5c3)

+ CV distribution. Peak 값은 0.23 - 0.3의 값을 갖고 있다. Peak 이하의 값을 갖는 유전자를 HKG 로 정의하고자함.
+ 각 DB 마다 peak 이하로 정의 할 경우에, DB bias가 생기기 때문에, 모든 DB의 CV 하위 25%로 상정함. 
+ Expression level pre-filtering은 TS scoring에 사용된 gene과 마찬가지로, 17,150개의 유전자를 사용함.
+ 3 DB에서 모두 HKG로 정의했을 때, 그 값을 consensus HKG로서 지정함.

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/6eca90ea-daaf-4085-85fa-4a0a7e1584c3)

+ 변경된 HKG와 기존 연구에 대한 비교.

* 변경된 HKG 정보를 포함한 데이터는 "/eevee/val/jjpark/atlas_report/HKGs_25percentile.txt"에 저장했습니다.

### 2.  Re-working Gene Info Page 
+ 새로운 Tissue-specific data와, HKG 연구로 인해, 다시 web app을 구축함.
+ 웹앱의 구성은 Home,Gene info page, data download page, tissue classifier page로 나누고자함.
+ 가장 중요한 기능인 Gene info Page를 구축함.

<img width="888" alt="image" src="https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/c98c2d0f-868f-4d91-bd5c-2d4c436ff7ea">



+ 위의 사진과 같은 형태로, 기능만을 구현한 Gene info page의 구축을 완료함. 이후 추가적인 UI 개선 및 디테일 보정이 필요함. 

* "http://leafeon.korea.ac.kr:8001/" 주말동안 위의 링크에서 웹앱 구동하고 있습니다.


# 23/07/23
## Summarize of Last Report
+ HKG reworking, Web app construction.

## This week goal
+ Constitive Expression Gene
+ Up/Down Regulated gene
+ Re-working TS score

### 1. Constitive Expression Gene
+ Constitive Expression Gene을 파악하기 위한 기준은 아래와 같음.
 - DB별 Sample내의 상위 75% 발현을 보이는 Gene은 1로, 그렇지 못하는 Gene은 0으로 표기함.
 - DB별 Gene의 binary table을 합산하여, Gene의 consititive expression score을 나타내고, Z-score 보정을 통해, 각 DB의 weight를 일괄적으로 조정함. 

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/0f7e50fa-0d33-41bf-988d-7a6d2b017abc)
+ Consititive Score

+ Constitive Score 2 이상의 expression level percentile은 95.94%. (DB당 expression read count sum의 percentile 평균)
+ Constitive Score 1 이상의 expression level percentile은 81.45%
+ Constitive Score 0 이상의 expression level percentile은 62.51%

### 2. Up / Down Regulated Gene
+ 앞선 Tissue-specific gene은 배타적으로 specific하게 high-expression되는 gene만을 규정하며, down-regulated 되는 gene에 대한 연구는 진행되지 않음.
+ 포괄적이고, less harsh한 기준으로 Up/Down regulated gene을 정의함.
+ 기준은 해당 tissue의 발현량이 평균 발현량의 5배 이상/이하를 up/down regulated gene으로서 정의함.
+ 위의 기준에 따라, 여러개의 tissue에서 up-regulated 되는경우와, down regulated gene의 경우 기존의 TS와 다른 분석을 제시 가능함.
+ '/eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/h_constitive/ALL_GENE_INFOS.json'에 TS, HKG, Consititive, Up/Down Regulated gene에 대한 정보를 개제함.

### 3. TS score re-working
+ 기존의 모든 DB에 존재하지 않는 tissue의 경우 분석에 noise가 생기는 문제가 있었음.
+ Most-expressed tissue의 Z-tau, Z-LogFC를 계산한 새로운 Gene TS Score를 계산하고, Consensus를 별도로 표시할 예정임.
+ 본 연구에서 지정하는 Tissue-specific gene은 조직을 보유하고 있는 모든 조직에서 가장 높은 발현량을 갖는 유전자만 TS gene으로 규정함.
+ '/eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/ts_scoring_new/0722_new/new_score.tsv'에 새로 계산된 TS score가 있음.

## Next week goal.
+ 금주로서 계획한 모든 gene centric 연구가 완료됨에 따라, web app construction을 빠른 시일 내에 해결하고자 합니다. 

# 23/10/02
## 1. Constitutive score revise

+ Constitutive Expression Gene의 파악을 위한 기준은 아래와 같음.
   - DB 별 1개 sample 내의 상위 25%, 50%, 75% 각 criteria로 binary 파일을 만듦 (GEO 1st quantile binary, GEO 2nd quantile binary, GEO 3rd quantile binary; GTEx, TCGA 동일)
   - 만들어진 binary 파일 (criteria up or down으로 분류하여 1,0으로 표기함.)을 합한뒤, z-score normalization을 진행하고 한 gene당 총 9개 normalized expression값(3개 DB * 3개 critera)의 평균을 constitutive score으로 정의함.

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/e57ee613-e007-4be2-8389-a3b80653db82)

+ 3rd quantile을 사용해서 만든 constitutive score plot
![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/08c698fe-ed45-4e24-b305-27f42a0089e3)

파일 계산 코드 및 결과물 : /eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/h_constitive/subs


# 23/10/15
## House keeping gene functional analysis.
+ House keeping gene 2,420개를 대상으로 [Panter](https://www.pantherdb.org/) 데이터 베이스에서 gene function annotation을 다운로드 받고, 기능별로 HKG function marking을 진행함.
+ Panter는 13,687개의 human protein coding gene에 대하여 24개의 class로 분류함.
+ HKG 2,420개는 1,582개 유전자에 대한 function annotation이 이뤄졌으며, 24개 class 중 22개의 class로 나뉜다.


HKG Function | Count
-|-
RNA_metabolism_ptn|291
gene_specific_transcriptional_regulator|249     
protein_modifying_enzyme|216
metabolite_interconversion_enzyme|148
membrane_traffic_protein|94
protein_binding_activity_modulator|86
chromatin_chromatin_binding_regulatory_ptn|81
transporter|78
translational_ptn|77
scaffold_adaptor_ptn|75
DNA_metabolism_ptn|67
cytoskeletal_ptn|45
chaperone|38
transmembrane_signal_receptor|7
structural_ptn|5       
transfer_carrier_ptn|5
viral_transposable_element_ptn|5   
extracellular_matrix_ptn|4
calcium-binding_ptn|3
cell_junction_protein|2
defense_immunity_ptn|3
intercellular_signal_molecule|3

Panter Function | Count
-|-
metabolite_interconversion_enzyme|1930
protein_modifying_enzyme|1615
gene_specific_transcriptional_regulator|1504    
transmembrane_signal_receptor|1138
transporter|1029
RNA_metabolism_ptn|819
protein_binding_activity_modulator|785
scaffold_adaptor_ptn|742
cytoskeletal_ptn|620
defense_immunity_ptn|611
membrane_traffic_protein|430
intercellular_signal_molecule|397
chromatin_chromatin_binding_regulatory_ptn|337
translational_ptn|332
cell_adhesion_molecule|325     
DNA_metabolism_ptn|225
chaperone|216
extracellular_matrix_ptn|142
transfer_carrier_ptn|136
structural_ptn|136    
calcium-binding_ptn|114
cell_junction_protein|60
viral_transposable_element_ptn|36 
storage_ptn|8 

+ Top 10 Function of HKG, Panther overview.

  ![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/83c6a82f-147a-40f3-9cc4-f593e6b08558)
  ![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/6b674d00-fea7-4274-9b29-dceaf43b7651)

+ House keeping gene의 function 구성 비율이 panther가 기본 제공하는 비율과 상이하며, 특히 RNA-metabolism 관련된 유전자들의 구성이 많은 만큼, 생존에 필수적인 유전자의 구성이 많고, immunity와 같은 특이적인 유전적 형질을 요하는 function은 줄었다. 


# TS score criteria 

+ [HPA](https://www.proteinatlas.org/)에서 tissue enriched (FC >4, Expression level pre-filtered) 3,106개 gene을 대상으로 TS score 5%,10%,15%,20%,25%,30% geneset을 만들어 confusion matrix를 통해 가장 신뢰도 높은 TS score criteria를 설정함.

Percentile|	Accuracy|	Precision|	Recall|	F1-Score
-|-|-|-|-
0.95	|0.8989|	0.2964|	0.7427|	0.4238
0.9	|0.891768115942029	|0.4671|	0.5855|	0.5196
0.85|	0.8750	|0.5999|	0.5011	|0.5461
0.8|0.84669|	0.6859|	0.42984|	0.5285
0.75|	0.8130	|0.7516	|0.376744	|0.5019
0.7|	0.77733	|0.80853|	0.33778|	0.4764

![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/c2726774-ba5f-45bf-8f2d-d1455fc43d76)
![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/e17e43e5-4a71-4d3e-972f-c413dcf5c9f1)

+ 가장 F1 score가 높은 15%의 1.286218 TS score를 Tissue specific gene criteria 으로 지정함.

# Environmental metarial DEG analysis
+ 한국 환경부 위해성평가 실시 등의 대상이 되는 환경유해인자의 종류 및 유해성 목록 고시 [자료](https://www.me.go.kr/home/web/public_info/read.do?pagerOffset=0&maxPageItems=10&maxIndexPages=10&searchKey=&searchValue=&menuId=10123&orgCd=&condition.publicInfoMasterId=7&condition.deleteYn=N&publicInfoId=1167&menuId=10123)에 등재된 263개의 environmental toxicity metrials 중 CAS 번호가 있는 물질에 대해 분석을 진행하고자함. 
+ GEO 의 rnaseq-count 옵션을 통해서 NCBI측에서 일괄적으로 align한 table을 분석대상으로 이용하고자함. Toy dataset download / distribution 파악 중에 있음. 

# 1217 weekly report 
## This week goal
+ T-score validation
+ 배준식 학생 연구 도움
+ coding work

## T-score validation
+ TS score (T-score) 개선을 위해 기존에 공개된 [TigerDB](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-9-271)와 비교 분석을 목적으로 함.
+ 2008년에 공개된 논문으로 gene annotation version, 제공하는 tissue의 차이에 따라 HUPTA에 존재하는 tissue와 일치하는 gene annotation version이 같은 1,960개의 gene으로 거름.
+ 1,960개의 gene 중 520개의 gene만이 HUPTA와 intersection함.
+ HUPTA의 T-score (85%) 이상의 gene과 공통된 데이터 셋이 다른 이유는 10년 이상의 gene annotation version 차이와 사용하는 tissue가 다르기 때문일 것으로 추정됨.
+ 데이터의 차이가 상이하여 연구 및 논문에 기재하기 어려움.
+ 다음 주 연구로 HUPTA와 HPA의 다른 연구를 Enrichment 분석으로 validation part를 검증하고자함.

## 배준식 학생 연구 도움
+ 같은 종의 소똥구리의 gut-microbiome의 조성을 k-mean clustering을 통해 labeling하는 과정 중에 있음.

## Coding work
+ 지난 연구 토의에서 지적하신 web DB coding work;  consititutive score, 누락된 정보 기입, download data 등의 coding work 마무리함. 

<a id="my-anchor"></a>
# 0101 Weekly Report
+ T-score 5% 대상으로 HPA와 비교
+ 배준식 학생 연구 도움

## T-score 1% 대상으로 HPA와 비교
+ 5%의 T-score를 갖는 gene 863개 대상으로 HPA와 비교하여 HUPTA에서만 TS 로 지정되는 222개의 gene을 분석 중에 있습니다.
+ Gene 별로 manually searching을 하고 있어 시간이 오래 걸리고 있습니다.

## 배준식 학생 연구 도움
+ "/panpyro/alfa/jjpark/jsbae" 디렉토리에 배준식 학생 연구 관련 작업물이 저장되어있습니다.
+ Clustering은 구성되는 OTU를 기반으로 Hierarchical Clustering을 진행했고, 4종의 소똥구리에 대해 구성하는 genus level / family level / OTU level 로 각각 진행했습니다.
+ Clustering 결과를 desert / grass land로 놓고 봤을 때, OTU level은 genus level과 비슷하게 분류되고, family level보다 genus level이 나은 것 같아, genus level로 소똥구리 4종에 대한 clustering 을 진행했습니다.
+ 클러스터링 된 샘플들을 labeling 하고, 먼저 bodilus 종에 대한 random forest 분류를 진행했습니다. parameter는 환경 변수, y값은 cluster label입니다. 
+ accuracy가 51%으로 모델 성능이 매우 좋지 못해 다른 종 / 다른 기법 등 다른 방법을 찾고 있습니다. 
