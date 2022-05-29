#处理从通达信中导出来的行情数据，整理完写入csv
import csv
from operator import truediv
data=[]
with open('D:\\new_tdx\\T0002\\export\\510500.csv',mode='r') as f:
    reader=csv.reader(f)
   
    for row in reader:
        if len(row)>0:
            newRow=row[0].replace('\t','').replace('   ',' ').lstrip()
            newList=newRow.split(' ')
            data.append([newList[0],newList[1],newList[2],newList[3],newList[4],'buy'])
            
        else:
            continue

print(data)
with open('SH500-201806-202205.csv',mode='w',encoding='UTF8',newline='') as f:
   writer= csv.writer(f)
   writer.writerows(data)