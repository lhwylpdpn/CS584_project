#!/usr/bin/python
# -*- coding: UTF-8 -*-


import time
import datetime
import sys
import csv
import tushare as ts
import pandas as pd
ts.set_token('6b57e4c863aa1e2d55c8ce62742130dd38332aafe1c43f2666dedfe5')
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
pro = ts.pro_api()

class get_data_from_tushare():

    def __init__(self):
        self.pro = ts.pro_api()
        self.data=''
    def get_stock_list(self):
        self.data = self.pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        self.data.to_csv('data_csv\stocklist.csv')
    def write_detail_data(self):
        for i in range(0,self.data.shape[0]):
            ts_code = self.data.iloc[i]['ts_code']
            df = pro.daily(ts_code=ts_code)
            df.to_csv('data_csv\\' + ts_code + '.csv')
            time.sleep(1) # 对方接口要求控制频次，每分钟不能超过500次，文件有大有小，是有概率超的，所以统一sleep下
            del (ts_code)

if __name__ == '__main__':

    obj_=get_data_from_tushare()
    obj_.get_stock_list()
    obj_.write_detail_data()