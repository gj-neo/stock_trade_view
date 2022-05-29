import numpy as np
f=open('jukuan_data.txt',encoding='utf-8')
txt=[]
for line in f:
    newline=line.replace('\n','').strip().replace('买','buy').replace("卖",'sell')
    splitLine=newline.split()
    if len(newline)==0 or splitLine[2]!='500ETF(510500.XSHG)':
        continue
    print(splitLine)
    txt.append(splitLine[0]+","+splitLine[2]+','+splitLine[3]+','+splitLine[6])
f=open('jukuan_500_trade_data.txt','w',encoding='utf-8',newline='')
for line in txt:
    f.writelines(line+'\r\n')