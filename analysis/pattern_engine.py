
def trend_filter(df):
    ema50=df["Close"].ewm(span=50).mean()
    ema200=df["Close"].ewm(span=200).mean()
    price=df["Close"].iloc[-1]
    return price>ema50.iloc[-1] and ema50.iloc[-1]>ema200.iloc[-1]

def detect_nr7(df):
    rng=df["High"]-df["Low"]
    last7=rng.tail(7)
    return last7.iloc[-1]==min(last7)

def detect_inside_bar(df):
    last=df.iloc[-1]
    prev=df.iloc[-2]
    return last["High"]<prev["High"] and last["Low"]>prev["Low"]

def detect_darvas(df):
    high=df["High"].rolling(20).max()
    return df["Close"].iloc[-1]>high.iloc[-2]

class PatternEngine:

    def __init__(self,df):
        self.df=df
        self.patterns=[]
        self.score=0

    def run(self):

        if not trend_filter(self.df):
            return {"patterns":[],"score":0}

        if detect_nr7(self.df):
            self.patterns.append("NR7")
            self.score+=10

        if detect_inside_bar(self.df):
            self.patterns.append("InsideBar")
            self.score+=10

        if detect_darvas(self.df):
            self.patterns.append("DarvasBreakout")
            self.score+=20

        return {"patterns":self.patterns,"score":self.score}
