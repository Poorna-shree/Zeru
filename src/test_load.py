import os

data_folder = "C:\\Users\\CHINNU\\Desktop\zeru\\aave-credit-scoring\\data"
file_path = os.path.join(data_folder, "user_transactions.json")

print("🔍 Listing all files in:", data_folder)
print(os.listdir(data_folder))  # Show what Python sees

if os.path.exists(file_path):
    print("✅ File exists!")
    with open(file_path, 'r') as f:
        print("✅ File opened successfully!")
        print("First 100 characters:")
        print(f.read(100))
else:
    print("❌ File not found at:", file_path)
