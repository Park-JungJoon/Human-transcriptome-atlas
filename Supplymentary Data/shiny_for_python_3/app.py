from shiny import App, reactive, render, ui
import os
import pandas as pd
from collections import defaultdict
from shiny.types import ImgData
media = '/leafeon/analysis1/jjpark/atlas_webapp/shiny_for_python_1/media/'
genes = ["Example"]
# making genes as gene names
with open (media + 'test_gene.txt') as f:
#with open (media + 'gene_name.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        genes.append(line)

app_ui = ui.page_fluid(
    # searching box
    ui.input_selectize(
        "search",
        "Select Gene To See",
        genes,
    ),
    ui.output_table('genetable'),
    ui.output_table('promotertable'),
    ui.output_image('geo_boxplot', height="150px"),
    ui.output_image('gtex_boxplot', height="150px"),
    ui.output_image('tcga_boxplot', height="150px"),
)
#  parsing GENECENTRIC_TABLE_FINAL.tsv a = genecentric_table_fianl.tsv
def table_parsing(a):
    with open (a) as f:
        global gene_promoter_dic
        global promoter_info_dic
        global gene_info_dic
        global epdless
        gene_promoter_dic = defaultdict(list)
        promoter_info_dic = defaultdict(list)
        gene_info_dic = defaultdict(list)
        epdless = {}
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            gene = line.split('\t')[0]
            list_gene_info = line.split('\t')[1:11]
            for info in list_gene_info:
                gene_info_dic[gene].append(info)
            #gene_info_dic[gene] = gene_info
            promoter = line.split('\t')[11]
            if promoter == 'Not in EPD DB':
                gene_promoter_dic[gene].append('Not in EPD DB')
                epdless[gene] = 0
                continue
            promoter_type = line.split('\t')[12]
            digit_promoter_motif = line.split('\t')[13] #TATA,Inr,CCAAT,GC
            promoter_motif = []
            if digit_promoter_motif[0] == '1':
                promoter_motif.append('TATA box')
            if digit_promoter_motif[1] == '1':
                promoter_motif.append('Inr')
            if digit_promoter_motif[2] == '1':
                promoter_motif.append('CCAAT box')
            if digit_promoter_motif[3] == '1':
                promoter_motif.append('GC box')
            if len(promoter_motif) == 0:
                promoter_motif.append('No Motifs Founded')
            promoter_seq = line.split('\t')[14]
            gene_promoter_dic[gene].append(promoter)
            promoter_info_dic[promoter].append(promoter_type)
            promoter_info_dic[promoter].append(promoter_motif)
            promoter_info_dic[promoter].append(promoter_seq)
        gene_info_dic['Example'].append('Example Gene')
        gene_info_dic['Example'].append('Specificity of GEO DB')
        gene_info_dic['Example'].append('Specificity of GTEx DB')
        gene_info_dic['Example'].append('Specificity of TCGA DB')
        gene_info_dic['Example'].append('DB that sort this gene as House Keeping Gene')
        gene_info_dic['Example'].append('Single Exon Gene / Multi Exon Gene')
        gene_info_dic['Example'].append('Determination of whether the gene is HKG')
        gene_info_dic['Example'].append('Determination of whether the gene is Tissue Specific Gene')
        gene_info_dic['Example'].append('Power of Specificity if the gene is TS')


# make pandas table to show on web. input should be ensg gene name
def gene_table_showing(ensg_gene):
    if ensg_gene == 'Example':
        gene_table = pd.DataFrame({'Gene' : ensg_gene,
                                   'GEO Specific Tissue' : [gene_info_dic[ensg_gene][0]],
                                   'GTEx Specific Tissue' : [gene_info_dic[ensg_gene][1]],
                                   'TCGA Specific Tissue' : [gene_info_dic[ensg_gene][2]],
                                   'HKG Predicted DB' : [gene_info_dic[ensg_gene][3]],
                                   'Single Exon Gene' :[gene_info_dic[ensg_gene][4]],
                                   'House Keeping Gene' : [gene_info_dic[ensg_gene][5]],
                                   'Predicted Tissue Specific' : [gene_info_dic[ensg_gene][6]],
                                   'TS score' : [gene_info_dic[ensg_gene][7]]})
    else:
        tmp_hkg = [','.join([i for i in gene_info_dic[ensg_gene][3:6] if i != 'NA'])]
        if tmp_hkg[0] == '':
            tmp_hkg =  'NA'
        else:
            tmp_hkg = tmp_hkg
        gene_table = pd.DataFrame({'Gene' : ensg_gene,
                                   'GEO Specific Tissue' : [gene_info_dic[ensg_gene][0]],
                                   'GTEx Specific Tissue' : [gene_info_dic[ensg_gene][1]],
                                   'TCGA Specific Tissue' : [gene_info_dic[ensg_gene][2]],
                                   'HKG Predicted DB' : tmp_hkg,
                                   'Single Exon Gene' :[gene_info_dic[ensg_gene][6].replace('SEG','Single Exon Gene').replace('MEG','Multi Exon Gene')],
                                   'House Keeping Gene' : [gene_info_dic[ensg_gene][7]],
                                   'Predicted Tissue Specific' : [gene_info_dic[ensg_gene][8]],
                                   'TS score' : [gene_info_dic[ensg_gene][9]]})
    return(gene_table)

def promoter_table_showing(ensg_gene):
    promoters = gene_promoter_dic[ensg_gene]
    if ensg_gene in epdless.keys():
        promoter_table = pd.DataFrame({'Not in EPD DB' : 'NA'},index = [0])
        return (promoter_table)
    else:
        if ensg_gene == 'Example':
            promoters = ['example_promoter']
            promoter_type = ['Type of promoter']
            promoter_motifs = ['Motifs in promoter']
            promoter_sequences = ['-50 ~ 10 bp from initiation site']
            tmpdic = {}
            tmpdic['Promoter'] = promoters
            tmpdic['Promoter Type'] = promoter_type
            tmpdic['Promoter Motifs'] = promoter_motifs
            tmpdic['Promoter Sequences'] = promoter_sequences
            answer = pd.DataFrame.from_dict(tmpdic)
            return(answer)

        else:
            promoters = gene_promoter_dic[ensg_gene]
            promoter_type = []
            promoter_motifs = []
            promoter_sequences = []
            for promoter in promoters:
                promoter_type.append(promoter_info_dic[promoter][0]) #type
                promoter_motifs.append(', '.join(promoter_info_dic[promoter][1])) #motif
                promoter_sequences.append(promoter_info_dic[promoter][2]) #seq
            tmpdic = {}
            tmpdic['Promoter']  = promoters
            tmpdic['Promoter Type'] = promoter_type
            tmpdic['Motifs in Promoter'] = promoter_motifs
            tmpdic['Promoter Sequence'] = promoter_sequences
            answer = pd.DataFrame.from_dict(tmpdic)
            return(answer)

def server(input, output, session):
    @output
    @render.table
    def genetable():
        gene = input.search()
        table_parsing(media+'FINAL_GENE_CENTRIC_TABLE.tsv')
        gene_table = gene_table_showing(gene)
        return (gene_table)
    
    @output
    @render.table
    def promotertable():
        gene = input.search()
        table_parsing(media + 'FINAL_GENE_CENTRIC_TABLE.tsv')
        promoter_table = promoter_table_showing(gene)
        return (promoter_table)

                #gene_table.style.set_table_attributes(
                #'class = "dataframe shiny-table table w-auto"'
                #)
                #.hide(axis= "index")
                #.format(
                #{
                #    "TS score" : '{0:0.1f}'
                #}
                #.set_table_styles(
                #[dict(selector = "th", props=[("test-align","right")]),
                #    dict(selector = "tr>td", props = [("padding-top","0.1rem"),("padding-bottom","0.1rem"),],),
                #]
                #)
                #)
            #)
    
    @output
    @render.image
    def geo_boxplot():
        gene = input.search()
        image_root = media + 'GEO_'+gene + '.png'
        img : ImgData = {"src" : image_root, "width": "300px"}
        return(img)
    @output
    @render.image
    def gtex_boxplot():
        gene = input.search()
        image_root = media + 'GTEX_'+gene + '.png'
        img : ImgData = {"src" : image_root, "width": "300px"}
        return(img)
    @output
    @render.image
    def tcga_boxplot():
        gene = input.search()
        image_root = media + 'TCGA_'+gene + '.png'
        img : ImgData = {"src" : image_root, "width": "300px"}
        return(img)

app = App(app_ui,server)


