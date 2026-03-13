
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def extract_features(df):

    r6=df["Close"].pct_change(120).iloc[-1]
    vol=df["Close"].pct_change().std()
    vol_ratio=df["Volume"].iloc[-1]/df["Volume"].rolling(50).mean().iloc[-1]

    return np.array([r6,vol,vol_ratio]).reshape(1,-1)

multibagger_profiles=[
[1.5,0.03,2.0],
[2.0,0.04,1.8],
[1.2,0.025,2.2]
]

def similarity_score(features):

    sims=[]

    for p in multibagger_profiles:
        s=cosine_similarity(features,np.array(p).reshape(1,-1))[0][0]
        sims.append(s)

    return max(sims)
