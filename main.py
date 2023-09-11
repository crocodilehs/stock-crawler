"""
TODO
現在固定畫一段時間
"""
import mplfinance as mpf
import indicator
import updateData
import warnings

def main(target_stock):
    warnings.filterwarnings('ignore')
    name = updateData.searchStock(target_stock)
    df = updateData.stockData(target_stock)
    #df = indicator.RSI(df, 14)
    print(f'現在查的是: {name}')
    # 畫K線
    title = f'{name} {target_stock}'

    # 把綠漲紅跌改成紅漲綠跌
    mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
    style = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)

    # 畫其中一段時間
    #draw_period = True
    start = '2023-06-05'
    end = '2023-09-12'
    tdf = df.loc[start:end,:]
    tdf = indicator.RSI(tdf, 14)
    tdf = indicator.ATR(tdf)
    tdf = indicator.MACD(tdf)
    tdf = indicator.KD(tdf)
    """
    panel: 畫在第幾張畫布上
    label: 圖例
    """
    add_plots = {
        "RSI": mpf.make_addplot(tdf['RSI'], panel=0, ylabel='RSI', color='purple', label="RSI"),
        "ATR": mpf.make_addplot(tdf['ATR'], panel=2, ylabel='ATR', label="ATR"),
        "hist": mpf.make_addplot(tdf['MACDhist'], type='bar', width=0.7, panel=3,
                             color='dimgray', alpha=1, secondary_y=False),
        "MACD": mpf.make_addplot(tdf['MACD'], panel=3, color='fuchsia', secondary_y=True, ylabel='MACD', label="MACD"),
        "singal": mpf.make_addplot(tdf['MACDsingal'], panel=3, color='b', secondary_y=True, label="singal"),
        "slowk": mpf.make_addplot(tdf['slowk'], panel=4, ylabel='KD', label="K"),
        "slowd": mpf.make_addplot(tdf['slowd'], panel=4, label="D")
    }
    """
    figratio: 圖的大小
    figscale: 圖的比例
    volume: 成交量的圖
    mav: 移動平均線(單位天)
    type可選candle or line
    """
    fig, axes = mpf.plot(tdf,type='candle', addplot=list(add_plots.values()), figscale=1,figratio=(15,12),
                        style=style, volume=True, returnfig=True)
    # 改字體讓中文可以顯示
    fig.suptitle(title, fontfamily='Microsoft JhengHei')
    # 圖例
    axes[2].set_ylabel("Volume")
    mpf.show()


if __name__ == "__main__":
    main("2330")