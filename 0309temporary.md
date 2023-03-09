+ 기존에 연구는 세 데이터베이스를 하나의 gene count table로 만들고, HKG, Tissue specific gene을 여러 parameter를 통해 조정함. 
+ 현재 세 데이터 베이스 별 HKG, TS를 조사하고, 그 교집합을 HKG, TS로 규정하고자함. 
+ HKG의 분포는 아래 벤 다이어그램과 같고, intersection HKG를 사용 가능하며, 선행연구와 유의함. 

<img width="210" alt="image" src="https://user-images.githubusercontent.com/97942772/223963648-7227df2c-c3db-4803-a0d8-3bd6b397fb62.png">

+ TS의 각 DB별 분포, 상위 5개 Tissue는 아래와 같음. 

GEO total : 1,979
Tissue|TS gene 
-|-
Liver|344
Pituitary|269
Blood|213
Testis|164
Kidney|145

TCGA total : 1,559
Tissue | TS gene
-|-
Brain|301
Liver|262
Testis|179
Adrenal_Gland|97
Thymus|95

GTEX total : 3022
Tissue | TS gene
-|-
Testis|1597
Liver|245
Brain|167
Muscle|131


+ 아래 벤다이어 그램은 가장 intersection TS의 분포.
<img width="270" alt="image" src="https://user-images.githubusercontent.com/97942772/223967682-dbe0a9b7-7130-4c0e-97a5-25e0b6d7b415.png">
<img width="270" alt="image" src="https://user-images.githubusercontent.com/97942772/223967743-e0d12536-d8d0-40f6-ae4f-37881b2ec324.png">
<img width="270" alt="image" src="https://user-images.githubusercontent.com/97942772/223967810-62d62d1a-a625-414a-b25f-f13491a1df7c.png">
<img width="270" alt="image" src="https://user-images.githubusercontent.com/97942772/223967837-b10c37dc-5672-45a8-a466-d54031c5a64a.png">


+ Liver를 제외한 나머지 tissue에서 Intersection TS를 사용하기 어려움. 교집합의 절대적인량이 부족함. 

+ TS는 해당 tissue 이외의 모든 tissue의 median expression의 5배 이상의 발현량을 가질 때 TS로 정의함. (추가적인 parameter로 Tau, expression level 사용.)
+ Tissue간 비교가 있어, 데이터 베이스 별 tissue 구성이 다르며, sample 수의 차이가 있음. 
+ Sample이 적은 tissue를 가진 db는 noise가 심함.
+ Tissue component가 다를 경우, tissue expression / tissue expression 비교시, db 별로 다른 결과가 나옴. (Liver/Pancreas highly express gene의 경우, pancreas가 없는 db에선 liver TS로 분류됨.)



## 현재 진행 상황 보고 
+ TS에 있어, 앞서 말씀드린 사항에 문제가 있습니다. 
+ Single exon gene 데이터셋을 다운로드 받고, single exon gene의 expression pattern을 확인하는 중에 있습니다.
  + Single exon gene 중, HKG와 겹치는 gene set을 확보하고, functional analysis를 진행했습니다.
  + TS에도 HKG와 비슷한 연구를 진행하고자하는데, TS의 정의가 명확하지 않아 난항에 말씀드립니다.





