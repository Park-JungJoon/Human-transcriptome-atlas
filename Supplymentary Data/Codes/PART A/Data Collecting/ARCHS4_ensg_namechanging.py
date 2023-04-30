gdic = {}
#download gprofiler_ensg.csv from gprofiler; purpose : translate gene symbol to enembl ID
with open ('gprofiler_ensg.csv') as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.rstrip()
        sym = line.split('\t')[0]
        ens = line.split('\t')[1]
        if sym.startswith('ENSG00'):
            gdic[sym] = sym
            continue
        elif ens == 'None':
            continue
        gdic[sym] = ens
with open ('ENSG_LIB_SIZE_NORMED_ARCHS4_GENE_COUNT_TABLE.tsv','w') as g:
    with open ('LIB_SIZE_NORMED_ARCHS4_GENE_COUNT_TABLE.tsv') as f:
        lines = f.readlines()
        g.write(lines[0])
        for line in lines[1:]:
            gn = line.split('\t')[0]
            els = line.split('\t')[1:]
            if gn in gdic.keys():
                g.write(gdic[gn]+'\t'+'\t'.join(els))
