# 股票走勢圖
使用 [yfinance](https://github.com/ranaroussi/yfinance) 抓取數據，再用 [mplfinance](https://github.com/matplotlib/mplfinance/tree/master) 畫圖，技術指標使用 [TA-Lib](https://github.com/TA-Lib/ta-lib-python) 計算。

## 功能
* 抓取並下載指定代號最近一年的交易資料(台股要加上「.TW」，美股直接打代號)
* 畫出最近半年的燭型圖
* 畫出4種技術指標(RSI、布林通道、MACD、KD)
