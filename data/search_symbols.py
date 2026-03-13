
from data.nse_symbols import get_nse_symbols

symbols = get_nse_symbols()

def search_stocks(q):
    q=q.lower()
    return [s for s in symbols if q in s.lower()][:10]
