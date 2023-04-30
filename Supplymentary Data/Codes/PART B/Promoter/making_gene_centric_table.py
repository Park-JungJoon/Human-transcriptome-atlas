from collections import defaultdict
# download "promoter_intersection_genes.txt","promoter_ensembl.txt","promoter_motifs.txt" from EPD
# output is "GENECENTRIC_TABLE_FINAL.tsv"
intersection = []
with open ("promoter_intersection_genes.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        intersection.append(line)

ensembl = {}
with open ("promoter_ensembl.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        p = line.split('\t')[0]
        e = line.split('\t')[1]
        if e not in intersection:
            continue
        ensembl[p] = e

motif  = {}
with open ("promoter_motifs.txt") as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.rstrip()
        p = line.split('\t')[0]
        m = ''.join(line.split('\t')[1:])
        if p not in ensembl.keys():
            continue
        motif[p] = m

coordinate = {}
with open ("promoter_coordinate.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        p = line.split('\t')[0]
        c = line.split('\t')[-1]
        if p not in ensembl.keys():
            continue
        coordinate[p] = c

sequence = {}
with open ("promoter_sequence.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        p = line.split('\t')[0]
        s = line.split('\t')[1]
        if p not in ensembl.keys():
            continue
        sequence[p] = s

metaall = {} #key = ensembl, 3000 genes don't match with EPD 
with open ('GENES_ALL_INFOS.tsv') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        e = line.split('\t')[0]
        i = '\t'.join(line.split('\t')[1:])
        metaall[e] = i

hkg = {}
ts = {}
with open ('GENES_SCORED_HKG_TS.tsv') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        gene = line.split('\t')[0]
        hk = int(line.split('\t')[2])
        tissue = line.split('\t')[3]
        ts_score = line.split('\t')[4]
        if hk == 3:
            hkg[gene] = 'HKG'
        else:
            hkg[gene] = 'NA'
        if ts_score != 'NA':
            if float(ts_score) > 1:
                ts[gene] = tissue+'\t'+str(ts_score)
            else:
                ts[gene] = 'NA\tNA'
        else:
            ts[gene] = 'NA\tNA'
for k in ensembl.keys():
    print(ensembl[k] +'\t'+metaall[ensembl[k]] +'\t'+hkg[ensembl[k]]+'\t'+ts[ensembl[k]] + '\t' + k + '\t' + coordinate[k] + '\t' + motif[k] + '\t'+ sequence[k])
for k in ts.keys():
    if k in ensembl.values():
        continue
    print(k+ '\tNA\t'+metaall[k]+'\t'+hkg[k]+'\t'+ts[k]+ '\tNot in EPD DB')
