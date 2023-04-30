# GET HKG from cv, exp 
from matplotlib_venn import venn3
import matplotlib.pyplot as plt
import os
import math
gtex_cv_dic = {}
gtex_exp_dic = {}

tcga_cv_dic = {}
tcga_exp_dic = {}

geo_cv_dic = {}
geo_exp_dic = {}

with open ('GEO_CV_EXP.tsv') as f:
    lines = f.readlines()
    for line in lines[1:]:
        if line.split('\t')[1] == 'NA':
            continue
        line = line.rstrip()
        gene = line.split('\t')[0]
        cv = float(line.split('\t')[1])
        exp = float(line.split('\t')[2])
        geo_cv_dic[gene] = cv
        geo_exp_dic[gene] = exp

with open ('GTEX_CV_EXP.tsv') as f:
    lines = f.readlines()
    for line in lines[1:]:
        if line.split('\t')[1] == 'NA':
            continue
        line = line.rstrip()
        gene = line.split('\t')[0]
        cv = float(line.split('\t')[1])
        exp = float(line.split('\t')[2])
        gtex_cv_dic[gene] = cv
        gtex_exp_dic[gene] = exp

with open ('TCGA_CV_EXP.tsv') as f:
    lines = f.readlines()
    for line in lines[1:]:
        if line.split('\t')[1] == 'NA':
            continue
        line = line.rstrip()
        gene = line.split('\t')[0]
        cv = float(line.split('\t')[1])
        exp = float(line.split('\t')[2])
        tcga_cv_dic[gene] = cv
        tcga_exp_dic[gene] = exp

gtex_cv_sorted = sorted(gtex_cv_dic.items(), key=lambda x: x[1]) #small to large
gtex_cv_cut = round(len(gtex_cv_sorted) * 0.5)
gtex_cv_high = []
for tmplist in gtex_cv_sorted[:gtex_cv_cut+1]:
    gtex_cv_high.append(tmplist[0])

gtex_exp_sorted = sorted(gtex_exp_dic.items(), key=lambda x: x[1], reverse = True) # large to small
gtex_exp_cut = round(len(gtex_exp_sorted) * 0.33)
gtex_exp_high = []
for tmplist in gtex_exp_sorted[:gtex_exp_cut+1]:
    gtex_exp_high.append(tmplist[0])

hkg_gtex = set(gtex_exp_high) & set(gtex_cv_high)



tcga_cv_sorted = sorted(tcga_cv_dic.items(), key=lambda x: x[1]) #small to large
tcga_cv_cut = round(len(tcga_cv_sorted) * 0.5)
tcga_cv_high = []
for tmplist in tcga_cv_sorted[:tcga_cv_cut+1]:
    tcga_cv_high.append(tmplist[0])

tcga_exp_sorted = sorted(tcga_exp_dic.items(), key=lambda x: x[1], reverse = True) # large to small
tcga_exp_cut = round(len(tcga_exp_sorted) * 0.33)
tcga_exp_high = []
for tmplist in tcga_exp_sorted[:tcga_exp_cut+1]:
    tcga_exp_high.append(tmplist[0])

hkg_tcga = set(tcga_exp_high) & set(tcga_cv_high)



geo_cv_sorted = sorted(geo_cv_dic.items(), key=lambda x: x[1]) #small to large
geo_cv_cut = round(len(geo_cv_sorted) * 0.5)
geo_cv_high = []
for tmplist in geo_cv_sorted[:geo_cv_cut+1]:
    geo_cv_high.append(tmplist[0])

geo_exp_sorted = sorted(geo_exp_dic.items(), key=lambda x: x[1], reverse = True) # large to small
geo_exp_cut = round(len(geo_exp_sorted) * 0.33)
geo_exp_high = []
for tmplist in geo_exp_sorted[:geo_exp_cut+1]:
    geo_exp_high.append(tmplist[0])

hkg_geo = set(geo_exp_high) & set(geo_cv_high)

intersection_hkg = hkg_geo & hkg_tcga & hkg_gtex

#venn3([hkg_geo, hkg_gtex, hkg_tcga], ('GEO', 'GTEx', 'TCGA'))
#plt.savefig('venn_diagram.png')
#print('Gene\tGEO_CV\tGTEX_CV\tTCGA_CV\tGEO_EXP\tGTEX_EXP\tTCGA_EXP')
#for i in intersection_hkg:
#    print(i+'\t'+str(geo_cv_dic[i])+'\t'+str(gtex_cv_dic[i])+'\t'+str(tcga_cv_dic[i])+'\t'+str(geo_exp_dic[i])+'\t'+str(gtex_exp_dic[i])+'\t'+str(tcga_exp_dic[i]))
with open ('HKG_GEO.txt','w') as f:
    for i in hkg_geo:
        f.write(i+'\t'+str(geo_cv_dic[i])+'\t'+str(geo_exp_dic[i])+'\n')

with open ('HKG_GTEX.txt','w') as f:
    for i in hkg_gtex:
        f.write(i+'\t'+str(gtex_cv_dic[i])+'\t'+str(gtex_exp_dic[i])+'\n')

with open ('HKG_TCGA.txt','w') as f:
    for i in hkg_tcga:
        f.write(i+'\t'+str(tcga_cv_dic[i])+'\t'+str(tcga_exp_dic[i])+'\n')

