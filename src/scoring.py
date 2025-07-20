import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def compute_credit_scores(features_df):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(features_df[['num_deposits', 'repay_ratio', 'unique_tokens', 'avg_amount']])

    features_df[['dep_scaled', 'repay_scaled', 'tok_scaled', 'avg_amt_scaled']] = scaled

    scores = []
    for _, row in features_df.iterrows():
        score = (
            row['dep_scaled'] * 0.3 +
            row['repay_scaled'] * 0.4 +
            row['tok_scaled'] * 0.2 +
            row['avg_amt_scaled'] * 0.1
        ) * 1000
        scores.append(score)

    result = pd.DataFrame({
        'userWallet': features_df['userWallet'],
        'score': scores
    })
    return result