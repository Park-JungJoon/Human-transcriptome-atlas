from matplotlib_venn import venn3
import matplotlib.pyplot as plt

geo = []
with open ('./TS_GEO.tsv') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        if line.split('\t')[1] == 'Testis':
            continue
        g = line.split('\t')[0]+line.split('\t')[1]
        geo.append(g)
tcga = []
with open ('./TS_TCGA.tsv') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        if line.split('\t')[1] == 'Testis':
            continue
        g = line.split('\t')[0]+line.split('\t')[1]
        tcga.append(g)

gtex = []
with open ('./TS_GTEX.tsv') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        if line.split('\t')[1] == 'Testis':
            continue
        g = line.split('\t')[0]+line.split('\t')[1]
        gtex.append(g)
geo = set(geo)
tcga = set(tcga)
gtex = set(gtex)
#print(geo)
venn3([geo,tcga,gtex],('GEO','TCGA','GTEx'))
plt.savefig('TS_nott_venn_diagram.png')

