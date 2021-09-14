import pandas as pd
import pandas_datareader.data as web
import numpy as np
import yfinance as yfin
import matplotlib.pyplot as plt
yfin.pdr_override()

start = pd.to_datetime("2017-01-01")
end = pd.to_datetime("2021-01-01")

print("Welcome to the portfolio allocation tool \n"
      "Enter the stocks that you like \n"
      "Then, let us give you a great portfolio with 5\n"
      "Write DONE when you are done")

tickers1 = []
tickers2 = []
tickers3 = []
tickers4 = []
tickers5 = []


def retvol(stock):
    stock["Normed Return"] = stock["Close"] / stock.iloc[0]["Close"]
    daily_std = np.std(stock["Normed Return"])
    stock["Std"] = daily_std * 252 ** 0.5


def analysis(ticker, tickers1, tickers2, tickers3, tickers4, tickers5):
    stock_df = web.DataReader(ticker, start, end)

    stock_df["Normed Return"] = stock_df["Close"] / stock_df.iloc[0]["Close"]
    daily_std = np.std(stock_df["Normed Return"])
    stock_df["Std"] = daily_std * 252 ** 0.5

    pb = web.get_quote_yahoo(ticker)["priceToBook"]
    pb = int(pb)

    if (stock_df["Normed Return"][-1] > 10) & (stock_df["Std"][-1] <= 60):
        tickers1.append(ticker)

    elif (stock_df["Normed Return"][-1] > 5) & (stock_df["Std"][-1] <= 30):
        tickers2.append(ticker)

    elif (stock_df["Normed Return"][-1] > 2.5) & (stock_df["Std"][-1] <= 15):
        tickers3.append(ticker)

    elif (stock_df["Normed Return"][-1] > 1) & (stock_df["Std"][-1] <= 5):
        tickers4.append(ticker)

    elif pb < 2:
        tickers5.append(ticker)


parameter = 0
while parameter == 0:
    ticker = input("Stock Symbol: ")
    try:
        if ticker == "DONE" :
            parameter = 1
        else:
            analysis(ticker, tickers1, tickers2, tickers3, tickers4, tickers5)
    except IndexError:
        print("Symbol Not Found")

if len(tickers1) == 0:
    tickers1 = 'TSLA'
    tickers1a = web.DataReader(tickers1, start, end)
    retvol(tickers1a)
else:
    for tick in tickers1:
        num = 0
        ra = 0
        stock_name = str(tuple(tickers1)[num].strip("[' ']"))
        stock_itself = web.DataReader(stock_name, start, end)
        retvol(stock_itself)
        ratio = stock_itself["Normed Return"][-1] / stock_itself["Std"][-1]
        if ratio > ra:
            ra = ratio
            constant = stock_name
        else:
            pass
        num = num + 1

    tickers1a = web.DataReader(constant, start, end)
    tickers1 = constant
    retvol(tickers1a)

if len(tickers2) == 0:
    tickers2 = 'NVDA'
    tickers2a = web.DataReader(tickers2, start, end)
    retvol(tickers2a)
else:
    for tick in tickers2:
        num = 0
        ra = 0
        stock_name = str(tuple(tickers2)[num].strip("[' ']"))
        stock_itself = web.DataReader(stock_name, start, end)
        retvol(stock_itself)
        ratio = stock_itself["Normed Return"][-1] / stock_itself["Std"][-1]
        if ratio > ra:
            ra = ratio
            constant = stock_name
        else:
            pass
        num = num + 1

    tickers2a = web.DataReader(constant, start, end)
    tickers2 = constant
    retvol(tickers2a)

if len(tickers3) == 0:
    tickers3 = 'MSFT'
    tickers3a = web.DataReader(tickers3, start, end)
    retvol(tickers3a)
else:
    for tick in tickers3:
        num = 0
        ra = 0
        stock_name = str(tuple(tickers3)[num].strip("[' ']"))
        stock_itself = web.DataReader(stock_name, start, end)
        retvol(stock_itself)
        ratio = stock_itself["Normed Return"][-1] / stock_itself["Std"][-1]
        if ratio > ra:
            ra = ratio
            constant = stock_name
        else:
            pass
        num = num + 1

    tickers3a = web.DataReader(constant, start, end)
    tickers3 = constant
    retvol(tickers3a)

if len(tickers4) == 0:
    tickers4 = 'UBER'
    tickers4a = web.DataReader(tickers4, start, end)
    retvol(tickers4a)
else:
    for tick in tickers4:
        num = 0
        ra = 0
        stock_name = str(tuple(tickers4)[num].strip("[' ']"))
        stock_itself = web.DataReader(stock_name, start, end)
        retvol(stock_itself)
        ratio = stock_itself["Normed Return"][-1] / stock_itself["Std"][-1]
        if ratio > ra:
            ra = ratio
            constant = stock_name
        else:
            pass
        num = num + 1

    tickers4a = web.DataReader(constant, start, end)
    tickers4 = constant
    retvol(tickers4a)

if len(tickers5) == 0:
    tickers5 = 'WFC'
    tickers5a = web.DataReader(tickers5, start, end)
    retvol(tickers5a)
else:
    for tick in tickers5:
        num = 0
        ra = 0
        stock_name = str(tuple(tickers5)[num].strip("[' ']"))
        stock_itself = web.DataReader(stock_name, start, end)
        retvol(stock_itself)
        ratio = stock_itself["Normed Return"][-1] / stock_itself["Std"][-1]
        if ratio > ra:
            ra = ratio
            constant = stock_name
        else:
            pass
        num = num + 1

    tickers5a = web.DataReader(constant, start, end)
    tickers5 = constant
    retvol(tickers5a)


for stock_d in (tickers1a,tickers2a,tickers3a,tickers4a,tickers5a):
    stock_d["Normed Return"] = stock_d["Close"] / stock_d.iloc[0]["Close"]

for stock_d, allo in zip((tickers1a,tickers2a,tickers3a,tickers4a,tickers5a),[.1,.2,.25,.25,.2]):
    stock_d["Allocation"] = stock_d["Normed Return"] * allo

for stock_d in (tickers1a,tickers2a,tickers3a,tickers4a,tickers5a):
    stock_d["Position Values"] = stock_d["Allocation"] * 10000000

all_pos_vals = [tickers1a["Position Values"],tickers2a["Position Values"],tickers3a["Position Values"],tickers4a["Position Values"],tickers5a["Position Values"]]
portfolio_val = pd.concat(all_pos_vals,axis=1)
portfolio_val.columns = [f"{tickers1} Pos",f"{tickers2} Pos",f"{tickers3} Pos",f"{tickers4} Pos",f"{tickers5} Pos"]
portfolio_val["Total Pos"] = portfolio_val.sum(axis=1)

portfolio_val["Total Pos"].plot(figsize=(10,8))
plt.title("Total Portfolio Value")
plt.show()

plt.plot(tickers1a["Std"],tickers1a["Normed Return"],label=tickers1)
plt.plot(tickers2a["Std"],tickers2a["Normed Return"],label=tickers2)
plt.plot(tickers3a["Std"],tickers3a["Normed Return"],label=tickers3)
plt.plot(tickers4a["Std"],tickers4a["Normed Return"],label=tickers4)
plt.plot(tickers5a["Std"],tickers5a["Normed Return"],label=tickers5)
plt.title("Return/ Volatility")
plt.xlabel("Volatility")
plt.ylabel("Returns")
plt.legend()
plt.show()






