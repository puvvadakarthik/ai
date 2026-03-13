
import pandas as pd

def get_nse_symbols():
    url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
    df = pd.read_csv(url)
    return [s + ".NS" for s in df["SYMBOL"].tolist()]
