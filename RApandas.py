import pandas as pd

df = pd.read_csv(r'/Users/kushwanthmeesala/Downloads/2024_fb_ads_president_scored_anon 2.csv')

print("\n== Overall Dataset Statistics ==")
print(df.describe(include='all'))

print("\n== Unique Values and Most Frequent ==")
for col in df.select_dtypes(include=['object', 'category']).columns:
    print(f"{col}:")
    print("Unique:", df[col].nunique())
    print("Top:", df[col].value_counts().head(1).to_dict())

print("\n== Aggregated by page_id ==")
print(df.groupby("page_id").describe(include='all'))

print("\n== Aggregated by page_id and ad_id ==")
print(df.groupby(["page_id", "ad_id"]).describe(include='all'))
