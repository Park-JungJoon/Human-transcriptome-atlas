# this code is written for TAU calculating for each db/tissue
with open ('GTEX_TAU.tsv','w') as g:
    with open ('T_MEAN_GTEX_TISSUE_GCT.tsv') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.rstrip()
            vals = line.split('\t')[1:]
            vals =  [float(i) for i in vals]
            sorted_vals = sorted(vals, reverse = True)
            if sorted_vals[0] == 0:
                continue
            oneminus_xivals = []
            for i in sorted_vals:
                xi = 1- i/sorted_vals[0]
                oneminus_xivals.append(xi)
            tau = sum(oneminus_xivals)/26
            g.write(str(line.split('\t')[0])+'\t'+str(tau)+'\n')
with open ('TCGA_TAU.tsv','w') as g:
    with open ('T_MEAN_TCGA_TISSUE_GCT.tsv') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.rstrip()
            vals = line.split('\t')[1:]
            vals =  [float(i) for i in vals]
            sorted_vals = sorted(vals, reverse = True)
            if sorted_vals[0] == 0:
                continue
            oneminus_xivals = []
            for i in sorted_vals:
                xi = 1- i/sorted_vals[0]
                oneminus_xivals.append(xi)
            tau = sum(oneminus_xivals)/20
            g.write(str(line.split('\t')[0])+'\t'+str(tau)+'\n')
with open ('GEO_TAU.tsv','w') as g:
    with open ('T_MEAN_GEO_TISSUE_GCT.tsv') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.rstrip()
            vals = line.split('\t')[1:]
            vals =  [float(i) for i in vals]
            sorted_vals = sorted(vals, reverse = True)
            if sorted_vals[0] == 0:
                continue
            oneminus_xivals = []
            for i in sorted_vals:
                xi = 1- i/sorted_vals[0]
                oneminus_xivals.append(xi)
            tau = sum(oneminus_xivals)/26
            g.write(str(line.split('\t')[0])+'\t'+str(tau)+'\n')
