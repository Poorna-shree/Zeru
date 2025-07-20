import pandas as pd

def extract_wallet_features(df):
    df['amount'] = df['actionData'].apply(lambda x: float(x.get('amount', 0)))
    
    grouped = df.groupby('userWallet')

    features = pd.DataFrame()
    features['num_deposits'] = grouped.apply(lambda x: (x['action'] == 'deposit').sum())
    features['num_borrows'] = grouped.apply(lambda x: (x['action'] == 'borrow').sum())
    features['num_repays'] = grouped.apply(lambda x: (x['action'] == 'repay').sum())
    features['total_amount'] = grouped['amount'].sum()
    features['avg_amount'] = grouped['amount'].mean()
    features['unique_tokens'] = grouped.apply(lambda x: x['actionData'].apply(lambda d: d.get('reserveSymbol')).nunique())

    # Compute repay ratio = total repay / (borrow + repay)
    features['repay_ratio'] = features['num_repays'] / (features['num_borrows'] + features['num_repays']).replace(0, 1)

    features = features.fillna(0)
    features.reset_index(inplace=True)
    return features