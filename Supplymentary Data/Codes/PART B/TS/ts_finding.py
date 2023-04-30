# this code is written for TS finding for each db by tau criteria, expression level, fold change.
gtexsortlist = []
with open ('./GTEX_TAU.tsv') as g:
    lines = g.readlines()
    for line in lines:
        line = line.rstrip()
        gene = line.split('\t')[0]
        ta = float(line.split('\t')[1])
        tmp = []
        tmp.append(gene)
        tmp.append(ta)
        gtexsortlist.append(tmp)

gtexsorted_tau = sorted(gtexsortlist, key = lambda x:x[1], reverse = True)
gtex_top_tau_gene = []
for i in range(round(len(gtexsorted_tau)*0.25)):
    gtex_top_tau_gene.append(gtexsorted_tau[i][0])
######
tcgasortlist = []
with open ('TCGA_TAU.tsv') as g:
    lines = g.readlines()
    for line in lines:
        line = line.rstrip()
        gene = line.split('\t')[0]
        ta = float(line.split('\t')[1])
        tmp = []
        tmp.append(gene)
        tmp.append(ta)
        tcgasortlist.append(tmp)

tcgasorted_tau = sorted(tcgasortlist, key = lambda x:x[1], reverse = True)

tcga_top_tau_gene = []

for i in range(round(len(tcgasorted_tau)*0.25)):
    tcga_top_tau_gene.append(tcgasorted_tau[i][0])
######
geosortlist = []
with open ('GEO_TAU.tsv') as g:
    lines = g.readlines()
    for line in lines:
        line = line.rstrip()
        gene = line.split('\t')[0]
        ta = float(line.split('\t')[1])
        tmp = []
        tmp.append(gene)
        tmp.append(ta)
        geosortlist.append(tmp)   

geosorted_tau = sorted(geosortlist, key = lambda x:x[1], reverse = True)

geo_top_tau_gene = []

for i in range(round(len(geosorted_tau)*0.25)):
    geo_top_tau_gene.append(geosorted_tau[i][0])
#TAU 
gtexdic = {}
with open ('T_MEAN_GTEX_TISSUE_GCT.tsv') as f:
    lines = f.readlines()
    header = lines[0].rstrip().split('\t')
    linelen = len(header)
    for line in lines[1:]:
        ensg = line.split('\t')[0]
        if ensg not in gtex_top_tau_gene:
            continue
        ls = line.split('\t')
        goal = []
        for i in range(1,linelen):
            shortls = []
            shortls.append(header[i])
            shortls.append(float(ls[i]))
            goal.append(shortls)
        gn = line.split('\t')[0]
        gtexdic[gn] = goal

gtexmeanexpdic = {}
with open ('EXP_GTEX_GENE_MEAN.tsv') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        gtexmeanexpdic[line.split('\t')[0]] = float(line.split('\t')[1])

with open ('TS_GTEX.tsv','w') as g:
    for k,v in gtexdic.items():
        sortedv = sorted(v, key=lambda x: -x[1])
        avg = gtexmeanexpdic[k]
        if avg > 0.0949 :
            if sortedv[1][1] == 0 or sortedv[0][1] /sortedv[1][1] > 5:
                g.write(k+'\t'+ sortedv[0][0] +'\t'+str(sortedv[0][1])+'\t'+str(sortedv[1][1])+'\n')

tcgadic = {}
with open ('T_MEAN_TCGA_TISSUE_GCT.tsv') as f:
    lines = f.readlines()
    header = lines[0].rstrip().split('\t')
    linelen = len(header)
    for line in lines[1:]:
        ensg = line.split('\t')[0]
        if ensg not in tcga_top_tau_gene:
            continue
        ls = line.split('\t')
        goal = []
        for i in range(1,linelen):
            shortls = []
            shortls.append(header[i])
            shortls.append(float(ls[i]))
            goal.append(shortls)
        gn = line.split('\t')[0]
        tcgadic[gn] = goal

tcgameanexpdic = {}
with open ('EXP_TCGA_GENE_MEAN.tsv') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        tcgameanexpdic[line.split('\t')[0]] = float(line.split('\t')[1])


with open ('TS_TCGA.tsv','w') as g:
    for k,v in tcgadic.items():
        sortedv = sorted(v, key=lambda x: -x[1])
        sum_sortedv = 0
        avg = tcgameanexpdic[k] 
        if avg  > 0.0692:
            if sortedv[1][1] == 0 or sortedv[0][1] /sortedv[1][1] > 5:
                g.write(k+'\t'+ sortedv[0][0] +'\t'+str(sortedv[0][1])+'\t'+str(sortedv[1][1])+'\n')

geodic = {}
with open ('T_MEAN_GEO_TISSUE_GCT.tsv') as f:
    lines = f.readlines()
    header = lines[0].rstrip().split('\t')
    linelen = len(header)
    for line in lines[1:]:
        ensg = line.split('\t')[0]
        if ensg not in geo_top_tau_gene:
            continue
        ls = line.split('\t')
        goal = []
        for i in range(1,linelen):
            shortls = []
            shortls.append(header[i])
            shortls.append(float(ls[i]))
            goal.append(shortls)
        gn = line.split('\t')[0]
        geodic[gn] = goal

geomeanexpdic = {}
with open ('EXP_GEO_GENE_MEAN.tsv') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        geomeanexpdic[line.split('\t')[0]] = float(line.split('\t')[1])


with open ('TS_GEO.tsv','w') as g:
    for k,v in geodic.items():
        sortedv = sorted(v, key=lambda x: -x[1])
        avg = geomeanexpdic[k] 
        if avg >0.169 :
            if sortedv[1][1] == 0 or sortedv[0][1] /sortedv[1][1] > 5:
                g.write(k+'\t'+ sortedv[0][0] +'\t'+str(sortedv[0][1])+'\t'+str(sortedv[1][1])+'\n')

