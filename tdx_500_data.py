#处理从通达信中导出来的行情数据，整理完写入csv
import csv
from operator import truediv
from timeit import repeat
data=[]
with open('510500.csv',mode='r') as f:
    reader=csv.reader(f)
    i=0
    for row in reader:
        #标题栏跳过
        if i==0:           
            i+=1
            continue
        if len(row)>0:
            newRow=row[0].replace('\t','').replace('   ',' ').lstrip()
            newList=newRow.split()
            if(len(newList)==0):
                continue
            data.append([newList[0],newList[1],newList[2],newList[3],newList[4]])
        else:
            continue

print(data)
with open('SH500-201806-202205.csv',mode='w',encoding='UTF8',newline='') as f:
   writer= csv.writer(f)
   writer.writerows(data)