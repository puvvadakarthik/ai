
from data.fetch_data import get_data
from config import MOMENTUM_THRESHOLD
from engine.parallel_engine import parallel_run

def scan_one(symbol):

    try:
        df=get_data(symbol)
        r=df["Close"].pct_change(60).iloc[-1]
        if r>MOMENTUM_THRESHOLD:
            return {"stock":symbol,"momentum":r}
    except:
        pass

def momentum_scan(symbols):

    res=parallel_run(symbols,scan_one)

    return sorted(res,key=lambda x:x["momentum"],reverse=True)
