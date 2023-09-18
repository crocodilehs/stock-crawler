# 台股數據分析
使用 [yfinance](https://github.com/ranaroussi/yfinance) 抓取數據，再用 [mplfinance](https://github.com/matplotlib/mplfinance/tree/master) 繪圖，技術指標使用 [TA-Lib](https://github.com/TA-Lib/ta-lib-python) 計算。

## 功能
* 抓取指定代號的歷史資料(台股要加上「.TW」，美股直接打代號)
* 畫出燭型圖或折線圖
* 畫出4種技術指標(RSI、布林通道、MACD、KD)的圖

## ToDo
- 做一個簡單的GUI
- 可以設定畫的日期範圍
- 選擇畫燭型圖或折線圖
- 選擇要畫那些技術指標
