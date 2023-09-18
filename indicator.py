"""
Indicator
計算技術指標
"""

from talib import abstract
import talib


def RSI(df, period):
  df.rename(columns={'Close': 'close'}, inplace=True)
  df['RSI'] = abstract.RSI(df, period)
  df.rename(columns={'close': 'Close'}, inplace=True)
  return df

def MACD(df):
  df.rename(columns={'Close':'close', 'High':'high', 'Low':'low'}, inplace = True)
  a = abstract.MACD(df)
  df['MACD'], df['MACDsingal'], df['MACDhist'] = a.macd, a.macdsignal, a.macdhist
  df.rename(columns={'close':'Close', 'high':'High', 'low':'Low'}, inplace = True)
  return df

def KD(df):
  df.rename(columns={'Close':'close', 'High':'high', 'Low':'low'}, inplace = True)
  a = abstract.STOCH(df)
  df['slowk'], df['slowd'] = a.slowk, a.slowd
  df.rename(columns={'close':'Close', 'high':'High', 'low':'Low'}, inplace = True)
  return df

def BBANDS(df):
  df.rename(columns={'Close':'close', 'High':'high', 'Low':'low'}, inplace = True)
  df["upper"], df["middle"], df["lower"] = talib.BBANDS(df["close"], timeperiod=20, nbdevup=2.1, nbdevdn=2.1, matype=0)
  df.rename(columns={'close':'Close', 'high':'High', 'low':'Low'}, inplace = True)
  return df

