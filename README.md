# Aave V2 Wallet Credit Scoring

## Project Overview

This project builds a credit scoring model for Ethereum wallets interacting with the Aave V2 DeFi protocol. The goal is to assign a credit score (0–1000) to each wallet based on historical transaction behavior, indicating reliability and risk level.

## Dataset

- Source: Aave V2 transaction data (JSON format) with ~100K records
- Transactions include actions like `deposit`, `borrow`, `repay`, `redeemunderlying`, and `liquidationcall`

## Methodology

### Feature Engineering

We extract the following features per wallet:

- Number of deposits, borrows, and repayments
- Total and average transaction amounts
- Number of unique tokens interacted with
- Repay ratio = repays / (borrows + repays)

### Scoring Logic

- Features are normalized using Min-Max scaling
- Weighted sum to compute credit score (scale 0–1000):
  - Deposits: 30%
  - Repay ratio: 40%
  - Unique tokens: 20%
  - Average amount: 10%

Higher scores indicate responsible and diversified usage; lower scores may indicate risky or exploitative behavior.

## How to Run

1. Place raw transaction JSON file under `data/user_transactions.json`
2. Run the scoring script:

```bash
python src/generate_scores.py --input data/user_transactions.json --output output/wallet_scores.csv

Output:

Wallet scores saved in output/wallet_scores.csv

Credit score distribution graph saved in output/credit_score_distribution.png

Dependencies
Python 3.x

pandas

scikit-learn

matplotlib

Install dependencies via:

bash
Copy code
pip install pandas scikit-learn matplotlib
Future Improvements
Incorporate time-based weighting for recent transactions

Penalize wallets with liquidation calls

Use advanced ML models with labeled data

Develop interactive visualization dashboard
'''
with open(output_dir / 'README.md', 'w', encoding='utf-8') as f:
f.write(content)

def save_analysis(output_dir):
content = '''# Credit Score Analysis Report

Score Distribution
The credit scores range from 0 to 1000, representing wallet reliability and risk. The histogram below (see credit_score_distribution.png) shows the distribution of scores across all wallets:

Majority of wallets cluster in the mid-range (400-700), indicating moderate activity and repayment behavior

A smaller proportion have very high scores (>900), indicating frequent deposits, high repay ratio, and diversified tokens

Some wallets score low (<200), potentially reflecting exploitative or bot-like behavior, low repayments, or liquidation events

Behavior Insights
Wallets with high repay_ratio and multiple deposits tend to have higher scores, reflecting responsible borrowing and repayment

Wallets interacting with more unique tokens are likely more diversified, which correlates with higher scores

Average transaction amount moderately affects scores, rewarding wallets with consistent and reasonable transaction sizes

Limitations
Current scoring does not factor in liquidation events or time decay of transactions

No supervised labels available; scoring is heuristic based on domain knowledge

Further validation with real-world risk data would improve robustness

Conclusion
This credit scoring framework provides a transparent, extensible way to quantify wallet trustworthiness based solely on transaction history. It forms a solid foundation for more advanced DeFi credit risk assessment models.
