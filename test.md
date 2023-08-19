##### Summarized Info
+ **Tissue** refers to the tissue with the highest expression level, based on two or more databases including GEO, GTEx, and TCGA. If the same tissue is identified as having the highest expression in two or more databases, it is labeled as that tissue. If different tissues are identified as having the highest expression levels across the three databases, the tissue that yields the highest value of (expression level of tissue with the highest expression) / (expression level of tissue with the second-highest expression) is selected and displayed, following the described rule.
+ **TS score** quantifies the degree of tissue-specific expression. We define genes with values equal to or greater than 1.5 as tissue-specific genes. The TS score is calculated by examining Normalized Foldchange (NFC) and Normalized Tau (NTau) across all three databases and then averaging the results. The TS score ranges from -1.5 to 5.2. NFC and Ntau values are explained in the TS Gene Info section below.Please refer to the image below for distribution visualization.
+ **Constitive score** is a measure of how consistently a gene is expressed. We assigned a score of 1 to genes with expression levels in the top 75% within samples out of a total of 46,813 samples, and a score of 0 otherwise. Subsequently, we combined the binary distribution of all genes and normalized it. The score ranges from -0.8 to 2.35. Please refer to the image below for distribution visualization.
+ **Up/Down Regulated Tissue** The criteria for "regulated" are based on the tissue with the highest or lowest expression level or the average expression across all tissues. Genes with expression levels more than 5-fold higher are categorized as Tissue-upregulated genes, while genes with expression levels more than 0.2-fold lower are categorized as downregulated genes. A gene can be associated with multiple regulated tissues.
+ **HKG** Please refer to the housekeeping INFO section for detailed explanations of the parameters. We conducted pre-filtering on genes that exhibit a difference of 4 or more in expression levels between the tissue with the highest expression and the tissue with the lowest expression. We classify genes with a coefficient of variation (CV) in the bottom 25% as housekeeping genes (HKG).

##### House Keeping Gene Info
+ **CV** is [Coefficient of variation](https://en.wikipedia.org/wiki/Coefficient_of_variation).The coefficient of variation (CV) is defined as the ratio of the standard deviation. We adopted CV instead of standard deviation, because library size of each sample are not equal. CV have values ranging from 0 to 1. A value closer to 0 suggests a more housekeeping-like pattern.
+ **Foldchange** in house keeping gene is the ratio of the average expression level in the tissue with the highest expression to the average expression level in the tissue with the lowest expression. We use foldchange as a pre-filtering criteria.
+ We pre-filtered genes with an average Fold Change (FC) of 4 or higher and defined genes with an average coefficient of variation (CV) in the lower 25% across the three databases as Housekeeping Genes (HKG). You can adjust the criteria on the Download page to customize your downloads.

##### Tissue Specific Gene Info
+ **NTau** is normalized [Tau](https://academic.oup.com/bib/article/18/2/205/2562739). Tau calculated in this equation :
  $$\tau = 1 - \frac{1}{n-1} \sum_{i=1}^{n} \hat{x}_i$$
  $$\hat{x_i} = x_i/max(x_i)$$
  $x_i$ is the expression of the gene in tissue $i$.
  $n$ is the number of tissues.
  From all genes, Tau values were investigated for each database, and Ntau was calculated by adjusting with Z-scores.
+ **NFC** is normalized foldchange, foldchange is the ration of the average expression level in the tissue with the highest expression to the average expression level in the tissue with the second highest expression. From all genes, FC wer investigated for each database, and NFC was calulated by adjusting with Z-scores.
+ **TS score** is mean of **NTau** and **NFC**

##### Promoter Info
+ All Promoter information obtained from [EPD new](https://epd.expasy.org/epd/EPDnew_database.php)
+ **Promoter type** Three categories of promoters are identified, indicating the diversity of transcription initiation patterns in Eukaryotes. [Dreos et al., 2016 ](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005144)
+ **Motifs** GC box, Inr region, TATA box, CCAAT box are defined.
+ **Promoter Sequence** A sequence spanning from -50bp to 10bp relative to the transcript region is displayed.


![image](https://github.com/Park-JungJoon/Human-transcriptome-atlas/assets/97942772/bf459c08-814b-40ec-8e1f-75c5213e29e6)
