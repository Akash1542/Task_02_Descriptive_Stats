import polars as pl

file_path = r'/Users/kushwanthmeesala/Downloads/2024_fb_ads_president_scored_anon 2.csv'
df = pl.read_csv(file_path)

print("== Descriptive Statistics ==")
print(df.describe())

for col in ['page_id', 'currency']:
    print(f"\n== Value Counts for {col} ==")
    vc_df = df.select([
        pl.col(col).value_counts()
    ]).unnest(col).sort("count", descending=True)
    print(vc_df)

print("\n== Number of Unique Values per Column ==")
print(df.select([
    pl.col(col).n_unique().alias(f"{col}_nunique") for col in df.columns
]))
