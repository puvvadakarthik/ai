
import yfinance as yf

def get_data(symbol):
    df = yf.download(symbol, period="2y", interval="1d", progress=False)
    df.dropna(inplace=True)
    return df
