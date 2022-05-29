from re import X
import pyecharts.options as opts
from pyecharts.charts import Kline,Line,Grid,EffectScatter
from pyecharts.globals import SymbolType
import csv
import datetime
x_data = []
y_data = []
buy_date_data=[]
sell_date_data=[]
buy_y_data=[]
sell_y_data=[]
#行情K线数据
with open('SH500-201806-202205.csv',mode='r') as f:
    reader=csv.reader(f)
    for row in reader:
        newList=row[0].split(',')
        x_data.append(row[0])
        y_data.append([row[1],row[2],row[3],row[4]])

#交易数据 
f=open('jukuan_500_trade_data.txt',encoding='utf-8')    
for line in f:
    newline=line.replace('\n','').split(',')
    #print(newline)
    if newline[2]=='buy':
        buy_date_data.append(newline[0].replace('-','/'))
        buy_y_data.append(newline[3])
    if newline[2]=='sell':
        sell_date_data.append(newline[0].replace('-','/'))
        sell_y_data.append(newline[3])
#创建K线图表    
kline=Kline()
kline.add_xaxis(x_data)
kline.add_yaxis('aa',y_data)
kline.set_global_opts(
        yaxis_opts=opts.AxisOpts(is_scale=True),
        xaxis_opts=opts.AxisOpts(is_scale=True),
        title_opts=opts.TitleOpts(title="Kline-基本示例"),
        #在图标内容区域拉伸
        datazoom_opts=[opts.DataZoomOpts(type_="inside")],
        #在图标下方拉伸
        #datazoom_opts=[opts.DataZoomOpts(pos_bottom="-2%")],
    )
#买入信号
y_data_buy_signals=[]
for tradeDay in x_data:
   
    #该交易日内有买入
    if tradeDay in buy_date_data:
        #
        curIndex=buy_date_data.index(tradeDay)
        y_data_buy_signals.append(buy_y_data[curIndex])
        print(buy_y_data[curIndex])
    else:
        y_data_buy_signals.append('')

buy_es=EffectScatter()
buy_es.add_xaxis(x_data)
buy_es.add_yaxis('买入',y_data_buy_signals,symbol=SymbolType.ROUND_RECT,itemstyle_opts=opts.ItemStyleOpts(
            color="#FF7F24",
            color0="#00da3c",
            border_color="#8A0000",
            border_color0="#008F28",
        ))
kline.overlap(buy_es)
#卖出信号
y_data_sell_signals=[]
for tradeDay in x_data:
   
    #该交易日内有买入
    if tradeDay in sell_date_data:
        #
        curIndex=sell_date_data.index(tradeDay)
        y_data_sell_signals.append(sell_y_data[curIndex])
        print(sell_y_data[curIndex])
    else:
        y_data_sell_signals.append('')

sell_es=EffectScatter()
sell_es.add_xaxis(x_data)
sell_es.add_yaxis('卖出',y_data_sell_signals,symbol=SymbolType.DIAMOND,itemstyle_opts=opts.ItemStyleOpts(
            color="#228B22",
            color0="#00da3c",
            border_color="#8A0000",
            border_color0="#008F28",
        ),)
kline.overlap(sell_es)
#渲染
kline.render()
