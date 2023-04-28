import os
import json
with open ('./files20221221.json') as f:
    file = json.load(f)
for i in range(len(file)):
    os.system("./gdc-client download %s" %file[i]['file_id'])
# gdc-client program을 linux에 설치해서 다운로드 받음.
# input file 로 TCGA에서 제공하는 json파일을 파싱해서 사용함
