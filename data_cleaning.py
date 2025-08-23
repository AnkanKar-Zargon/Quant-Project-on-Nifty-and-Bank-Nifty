import pandas as pd

# === Load data ===
df = pd.read_parquet("data.parquet")

# --- Ensure datetime index ---
if "time" in df.columns:  
    df["time"] = pd.to_datetime(df["time"])
    df = df.set_index("time").sort_index()
else:
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

print("=== Missing values BEFORE cleaning ===")
print(df.isna().sum())
print(f"Total rows before cleaning: {len(df)}\n")

# === Drop all rows with ANY NaN ===
df_cleaned = df.dropna()

print("=== Missing values AFTER cleaning ===")
print(df_cleaned.isna().sum())
print(f"Total rows after cleaning: {len(df_cleaned)}")
print(f"🚮 Dropped {len(df) - len(df_cleaned)} rows\n")

# === Save cleaned parquet ===
output_file = "data_cleaned.parquet"
df_cleaned.to_parquet(output_file, engine="pyarrow", index=True)

print(f"✅ Cleaned parquet saved as {output_file}")
