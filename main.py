#import yfinance as yf
import mplfinance as mpf
import Indicator
import updateData


#target_stock = "2330"
def main(target_stock):
    df = updateData.stock_data(target_stock)
    df = Indicator.RSI(df, 14)
    # 畫K線
    title = f'{target_stock}'
    # 改字體讓中文可以顯示
    #font={'font.family': 'Microsoft JhengHei'}

    # 把綠漲紅跌改成紅漲綠跌
    mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
    #s  = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc, rc=font)
    s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)

    # 其他圖表的細節設定

    type = '燭形圖'
    if type == '燭形圖':
      p = 'candle'
    if type == '折線圖':
      p = 'line'

    """
    figratio: 圖的大小
    figscale: 圖的比例
    volume: 成交量的圖
    mav: 移動平均線(單位天)
    """

    kwargs = dict(type=p, mav=(5,20,60), volume=True, figratio=(10,8), figscale=0.75,
                  title=target_stock, style=s, returnfig=True)

    # 畫其中一段時間
    draw_period = True
    start = '2023-01-01'
    end = '2023-08-21'
    tdf = df.loc[start:end,:]
    tdf = Indicator.ATR(tdf)
    tdf = Indicator.MACD(tdf)
    tdf = Indicator.KD(tdf)

    add_plots = {
        "RSI": mpf.make_addplot(tdf['RSI'], panel=0, ylabel='RSI', color='purple'),
        "ATR": mpf.make_addplot(tdf['ATR'], panel=2, ylabel='ATR'),
        "hist": mpf.make_addplot(tdf['MACDhist'], type='bar', width=0.7, panel=3,
                             color='dimgray', alpha=1, secondary_y=False),
        "MACD": mpf.make_addplot(tdf['MACD'], panel=3, color='fuchsia', secondary_y=True, ylabel='MACD', label="MACD"),
        "singal": mpf.make_addplot(tdf['MACDsingal'], panel=3, color='b', secondary_y=True, label="singal"),
        "slowk": mpf.make_addplot(tdf['slowk'], panel=4, ylabel='KD'),
        "slowd": mpf.make_addplot(tdf['slowd'], panel=4)
    }

    fig, axes = mpf.plot(tdf,type='candle', addplot=list(add_plots.values()), figscale=1,figratio=(15,12),title=title,
                        style=s, volume=True, returnfig=True)

    axes[1].legend([None]*(len(add_plots)+2))
    handles = axes[1].get_legend().legend_handles
    axes[1].legend(handles=handles,labels=list(add_plots.keys()))
    axes[2].set_ylabel("Volume")
    #axes[6].legend([None]*(len(add_plots)+2))
    #handles = axes[6].get_legend().legend_handles
    #axes[6].legend(handles=handles,labels=['hist', 'MACD', 'singal'], loc='center left')
    mpf.show()
    #print(tdf)
"""
if draw_period:

    apdict = mpf.make_addplot(tdf['RSI'], panel=2, ylabel='RSI', color='purple')

    kwargs = dict(type=p, mav=(5, 20, 60), volume=True, figratio=(15, 12), figscale=1, title=target_stock, style=s,
                  addplot=apdict, returnfig=True)
    fig, axes = mpf.plot(tdf, **kwargs)
    # add legend
    axes[0].legend([None] * 5)
    handles = axes[0].get_legend().legend_handles
    axes[0].legend(handles=handles[2:], labels=('5   days', '20 days', '60 days'))
    mpf.show()

else:
  fig, axes = mpf.plot(df, **kwargs)

  axes[0].legend([None] * 6)
  handles = axes[0].get_legend().legen_handles
  axes[0].legend(handles=handles[2:], labels=('5   days', '20 days', '60 days'))
  mpf.show()

"""

if __name__ == "__main__":
    main(2330)