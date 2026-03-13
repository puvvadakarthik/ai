
from data.fetch_data import get_data
from analysis.pattern_engine import PatternEngine
from engine.parallel_engine import parallel_run

def scan_one(symbol):

    try:
        df=get_data(symbol)
        engine=PatternEngine(df)
        r=engine.run()
        if r["score"]>0:
            return {"stock":symbol,"patterns":r["patterns"],"score":r["score"]}
    except:
        pass

def pattern_scan(symbols):

    res=parallel_run(symbols,scan_one)

    return sorted(res,key=lambda x:x["score"],reverse=True)
