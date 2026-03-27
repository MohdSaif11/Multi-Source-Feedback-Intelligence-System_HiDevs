import pandas as pd

def sentiment_trend(df):
    df['date'] = pd.to_datetime(df['date'])
    return df.groupby(df['date'].dt.date)['sentiment_score'].mean()
    