from data.fetch_data import get_data
from config import MOMENTUM_THRESHOLD
from engine.parallel_engine import parallel_run

def scan_one(symbol):

    try:
        df = get_data(symbol)

        r = df["Close"].pct_change(60).iloc[-1]

        if r > MOMENTUM_THRESHOLD:

            return {"stock": symbol, "momentum": r}

    except Exception as e:
        print(symbol, e)
