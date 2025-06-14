import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/kushwanthmeesala/Downloads/2024_fb_ads_president_scored_anon 2.csv")

plt.figure(figsize=(10, 5))
sns.histplot(df['estimated_spend'], bins=50, kde=True)
plt.title("Distribution of Estimated Spend")
plt.xscale('log')  
plt.xlabel("Estimated Spend")
plt.ylabel("Ad Count")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='currency', y='estimated_spend')
plt.yscale('log')
plt.title("Spend Distribution by Currency")
plt.show()

top_pages = df['page_id'].value_counts().head(10)
top_pages.plot(kind='barh', figsize=(8, 5))
plt.gca().invert_yaxis()
plt.title("Top 10 Pages by Ad Count")
plt.xlabel("Ad Count")
plt.show()

msg_types = ['advocacy_msg_type_illuminating', 'attack_msg_type_illuminating', 'issue_msg_type_illuminating']
msg_avg = df[msg_types].mean()
msg_avg.plot(kind='bar', figsize=(6, 4))
plt.title("Average Message Type Distribution")
plt.ylabel("Proportion")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(df[['estimated_spend', 'estimated_impressions', 'estimated_audience_size']].corr(), annot=True, cmap='coolwarm')
