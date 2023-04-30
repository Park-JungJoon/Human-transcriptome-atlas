with open  ('only_seg_gene_info.tsv','w') as g:
    with open ('GENE_ALL_INFO_TS_HKG_INTRON.tsv') as f:
        lines= f.readlines()
        for line in lines:
            line = line.rstrip()
            ts = line.split('\t')[1:4]
            hkg = line.split('\t')[4:7]
            etype = line.split('\t')[-1]
            if etype != 'SEG':
                continue
            if ts.count('NA') == 3 and hkg.count('NA') == 3:
                continue
            ans = line.replace('NA\t','')
            ans = ans.replace('SEG','')
            g.write(ans+'\n')
