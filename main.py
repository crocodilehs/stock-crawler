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

    title = f'{name} {target_stock}'
    print(f'現在查的是: {title}')

    # 把綠漲紅跌改成紅漲綠跌
    mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
    style = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc, y_on_right=False, edgecolor="black")
    df = indicator.RSI(df, 14)
    df = indicator.BBANDS(df)
    df = indicator.MACD(df)
    df = indicator.KD(df)
    # 畫其中一段時間
    start = '2023-06-05'
    end = '2023-09-12'
    tdf = df.loc[start:end,:]

    """
    panel: 畫在第幾張畫布上
    label: 圖例
    """
    add_plots = {
        "RSI": mpf.make_addplot(tdf['RSI'], panel=4, ylabel='RSI', color='purple', label=f"RSI {tdf['RSI'][-1]:.2f}"),
        "hist": mpf.make_addplot(tdf['MACDhist'], type='bar', width=0.7, panel=2,
                             color='dimgray', alpha=1, secondary_y=False),
        "MACD": mpf.make_addplot(tdf['MACD'], panel=2, ylabel='MACD', color='fuchsia', secondary_y=False, label="MACD", width=0.8),
        "singal": mpf.make_addplot(tdf['MACDsingal'], panel=2, color='b', secondary_y=False, label="singal", width=0.8),
        "slowk": mpf.make_addplot(tdf['slowk'], panel=3, ylabel='KD', label="K", width=0.8),
        "slowd": mpf.make_addplot(tdf['slowd'], panel=3, label="D", width=0.8),
        "upper": mpf.make_addplot(tdf['upper'], panel=0, label='upper', linestyle='--', width=0.5),
        "middle": mpf.make_addplot(tdf['middle'], panel=0, label='middle', color='y', linestyle=':', width=0.8),
        "lower": mpf.make_addplot(tdf['lower'], panel=0, label='lower', linestyle='--', width=0.5)
    }
    """
    figratio: 圖的大小
    figscale: 圖的比例
    volume: 成交量的圖
    mav: 移動平均線(單位天)
    type可選candle or line
    """
    fig, axes = mpf.plot(tdf,type='candle', addplot=list(add_plots.values()), figscale=1, figratio=(15,12),
                        style=style, volume=True, returnfig=True)
    # 改字體讓中文可以顯示
    fig.suptitle(title, fontfamily='Microsoft JhengHei')
    # 圖例
    axes[2].set_ylabel("Volume")
    axes[0].legend(fontsize=10, loc='lower left', frameon=True)
    axes[4].legend(fontsize=10, loc='lower left', frameon=True)
    axes[6].legend(fontsize=10, loc='lower left', frameon=True)
    axes[8].legend(fontsize=10, loc='lower left', frameon=True)
    mpf.show()


if __name__ == "__main__":
    #main("2330.TW")
    main("AAPL")