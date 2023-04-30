# getting intersection hkg  
hkggeo = []
with open ('/eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/c_hkg/HKG_GEO.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        hkggeo.append(line.split('\t')[0])
hkggtex = []
with open ('/eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/c_hkg/HKG_GTEX.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        hkggtex.append(line.split('\t')[0])
hkgtcga = []
with open ('/eevee/val/jjpark/PAPER_RNA_SEQ_ATLAS/c_hkg/HKG_TCGA.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        hkgtcga.append(line.split('\t')[0])

intersection = set(hkggtex) & set(hkgtcga) & set(hkggeo)
for i in intersection:
    print(i)
