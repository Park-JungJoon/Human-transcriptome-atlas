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



</br>

***

금주에 학기 기말 과제가 겹쳐 연구 Progress가 많지 못했습니다. 죄송합니다. 
