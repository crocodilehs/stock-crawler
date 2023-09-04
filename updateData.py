"""
updateData

ToDo
要增加存成csv或資料庫然後只更新每天的資料的部份
一次下載幾個常用的
把上市上櫃的代號資料存下來

檢查有沒有下載過，不是最新的資料就下載補進去
"""
import datetime
import os
import yfinance as yf
import pandas as pd


def stock_data(stock_id):
    today = datetime.date.today()
    tomarrow = today + datetime.timedelta(days=1)
    address = stock_id + ".csv"
    if os.path.isfile(address):
        df_new = pd.read_csv(address, index_col="Date", parse_dates=["Date"])

        end = datetime.datetime.strptime(str(today), '%Y-%m-%d')
        # 下載缺少的資料
        df = yf.download(stock_id + ".TW", start=df_new.index[-1], end=tomarrow)
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
        df = yf.download(stock_id + ".TW", end=tomarrow)
        df.to_csv(address, encoding='utf-8')
        print("此為新資料，已建立csv檔")
        return df


#df = stock_data("2330", datetime.date.today())