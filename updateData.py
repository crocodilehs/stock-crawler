"""
updateData
檢查資料並補充最新資料
用股票代號查詢名稱
"""
import datetime
import os
import yfinance as yf
import pandas as pd
import requests
import re


def stockData(stock_id: str):
    """
    下載該代號的所有歷史交易數據
    :param stock_id: 股票代號
    :return: 股票資料dataframe
    """
    today = datetime.date.today()
    tomarrow = today + datetime.timedelta(days=1)
    address = stock_id + ".csv"
    if os.path.isfile(address):
        df_new = pd.read_csv(address, index_col="Date", parse_dates=["Date"])

        end = datetime.datetime.strptime(str(today), '%Y-%m-%d')
        # 下載缺少的資料
        df = yf.download(stock_id, start=df_new.index[-1], end=tomarrow)
        if end not in df_new.index:
            # 合併新資料到舊資料然後存檔
            df_new = pd.concat([df_new, df])
            df_new.to_csv(address, encoding='utf-8')
            print(f"已更新到 {today} 的最新資料")
            return df_new
        else:
            print("已是最新資料，無需更新")
            return df_new
    else:
        df = yf.download(stock_id, end=tomarrow)
        df.to_csv(address, encoding='utf-8')
        print("此為新資料，已建立csv檔")
        return df


def searchStock(target: str):
    """
    下載代號和名稱的對照表並存起來
    不會自動更新存好的檔案，每次都要下載太久了
    :param target: 股票代號
    :return: 股票名稱
    """
    if ".TW" not in target:
        return ""
    if not os.path.isfile("name.csv"):
        res = requests.get("https://isin.twse.com.tw/isin/C_public.jsp?strMode=2")
        df = pd.read_html(res.text)[0]
        # 設定column名稱
        df.columns = df.iloc[0]
        # 刪除第一行
        df = df.iloc[2:]
        df = df.dropna(thresh=3, axis=0).drop("CFICode", axis=1)
        df = df.drop("備註", axis=1)
        df = df.drop("國際證券辨識號碼(ISIN Code)", axis=1)
        df = df.drop("上市日", axis=1)
        df.columns = ['有價證券代號及名稱', '市場別', '產業別']
        df[['有價證券代號', '名稱']] = df['有價證券代號及名稱'].str.extract(r'(\S+)\s+(\S+)')
        df.drop('有價證券代號及名稱', axis=1, inplace=True)
        # 重置索引
        df.reset_index(drop=True, inplace=True)
        df = df.set_index('有價證券代號')
        #df = df.drop('Unnamed: 0', axis=1)
        df = df[['名稱', '市場別', '產業別']]
        df.to_csv("name.csv")
    else:
        df = pd.read_csv("name.csv")
        df = df.set_index('有價證券代號')
        print("")
    result = df.loc[target, '名稱']

    return result