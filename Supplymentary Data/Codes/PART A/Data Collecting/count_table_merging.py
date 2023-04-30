from collections import defaultdict
import json
genedic = defaultdict(list)
dic = defaultdict(dict)
#Using intersections genes only
with open ('using_genes.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        genedic[line] = []

#Gene Feature parsing from V38 annotation
with open ('v36_summary.txt') as f:
    lines = f.readlines()
    for line in lines:
        ls = line.split('; ')
        geneid = ls[0].split('.')[0]
        geneid = geneid.replace('gene_id "','')

        genename = ls[2]
        genename = genename.replace("gene_name ", "")
        genename = genename.replace('"','')

        genetype = ls[1]
        genetype = genetype.replace("gene_type ","")
        genetype = genetype.replace('"','')
        if geneid in genedic.keys():
            genedic[geneid].append(genename)
            genedic[geneid].append(genetype)
print('using gene parsing comp')

#encode merge
totalsamp = []
with open ('encode_count_table.tsv') as f:
    lines = f.readlines()
    samples = lines[0].rstrip().split('\t')[2:]
    totalsamp += samples
    for line in lines[1:]:
        encode_gene = line.split('\t')[0].split('.')[0]
        ls = line.split('\t')[2:]
        if encode_gene not in genedic.keys():
            continue
        for s in range(len(samples)):
            samples[s] = samples[s]
            dic[encode_gene][samples[s]]=ls[s]
print('encode merge comp')

#gtex merge
with open ('gtex_count_table.tsv') as f:
    lines = f.readlines()
    samples = lines[0].rstrip().split('\t')[2:]
    totalsamp += samples
    for line in lines[1:]:
        line = line.rstrip()
        gtex_gene = line.split('\t')[0].split('.')[0]
        ls = line.split('\t')[2:]
        if gtex_gene not in genedic.keys():
            continue
        for s in range(len(samples)):
            dic[gtex_gene][samples[s]]=ls[s]
print('gtex merge comp')

#TCGA filename to fileid
filematdic = defaultdict(str)
with open ('./files20221221.json') as f:
    jsonfile = json.load(f)
for i in jsonfile:
    fileid = i['file_id']
    filename = i['file_name'].replace('.rna_seq.augmented_star_gene_counts.tsv','')
    filematdic[filename] = fileid
print('Json parsing comp')

#tcga merge
with open ('tcga_count_table.tsv') as f:
    lines = f.readlines()
    samples = lines[0].rstrip().split('\t')[2:]
    for line in lines[1:]:
        tcga_gene = line.split('\t')[0].split('.')[0]
        ls = line.split('\t')[2:]
        if tcga_gene not in genedic.keys():
            continue
        for s in range(len(samples)):
            dic[tcga_gene][filematdic[samples[s]]]=ls[s]
    for i in samples:
        totalsamp.append(filematdic[i])
print('tcga merge comp')

#Make table
totalsamp = sorted(totalsamp)
with open ('../COUNT_TABLE_merged.tsv' , 'w') as g:
    stri = 'Gene\tGene Name\tGene Type\t'+'\t'.join(totalsamp) #header
    g.write(stri+'\n')
    for k_gene, v_dic in dic.items():
        g.write(k_gene+'\t'+'\t'.join(genedic[k_gene])+'\t')
        for i in totalsamp:
          g.write(dic[k_gene][i]+'\t')
    g.write('\n')

