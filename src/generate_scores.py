import os
import argparse
import matplotlib.pyplot as plt
from utils import load_transactions
from features import extract_wallet_features
from scoring import compute_credit_scores

def main(input_path, output_path):
    print("[1] Loading data...")
    df = load_transactions(input_path)

    print("[2] Extracting features...")
    features_df = extract_wallet_features(df)

    print("[3] Calculating scores...")
    scores_df = compute_credit_scores(features_df)

    print("[4] Saving scores...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    scores_df.to_csv(output_path, index=False)
    print(f"[✔] Done. Saved to {output_path}")

    # [5] Plotting graph of credit score distribution
    print("[5] Generating score distribution graph...")
    plt.figure(figsize=(10, 6))
    plt.hist(scores_df['score'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Credit Score Distribution')
    plt.xlabel('Credit Score')
    plt.ylabel('Number of Wallets')
    plt.grid(True)
    plt.tight_layout()

    graph_path = os.path.join(os.path.dirname(output_path), "credit_score_distribution.png")
    plt.savefig(graph_path)
    print(f"[✔] Graph saved to: {graph_path}")

    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True, help="Path to input JSON file")
    parser.add_argument('--output', type=str, default='output/wallet_scores.csv', help="Output CSV path")

    args = parser.parse_args()
    main(args.input, args.output)
