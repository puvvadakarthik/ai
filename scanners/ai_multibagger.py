
from data.fetch_data import get_data
from analysis.ai_analyzer import extract_features, similarity_score
from engine.parallel_engine import parallel_run

def scan_one(symbol):

    try:
        df=get_data(symbol)
        f=extract_features(df)
        score=similarity_score(f)
        if score>0.8:
            return {"stock":symbol,"ai_similarity":score}
    except:
        pass

def ai_scan(symbols):

    res=parallel_run(symbols,scan_one)

    return sorted(res,key=lambda x:x["ai_similarity"],reverse=True)
