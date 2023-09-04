"""
Indicator
計算技術指標
"""

from talib import abstract


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

def ATR(df):
  df.rename(columns={'Close':'close', 'High':'high', 'Low':'low'}, inplace = True)
  df['ATR'] = abstract.ATR(df)

  df.rename(columns={'close':'Close', 'high':'High', 'low':'Low'}, inplace = True)
  return df

