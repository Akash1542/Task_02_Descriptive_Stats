import csv
import math
from collections import defaultdict, Counter

def read_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def compute_stats(data):
    stats = {}
    for col in data[0].keys():
        values = [row[col] for row in data if col in row and row[col] != '']
        if not values:
            stats[col] = {'count': 0, 'note': 'No data'}
            continue

        numeric_values = []
        for v in values:
            if is_float(v):
                numeric_values.append(float(v))

        count = len(values)

        if numeric_values:
            n = len(numeric_values)
            mean = sum(numeric_values) / n
            std_dev = math.sqrt(sum((x - mean) ** 2 for x in numeric_values) / n)
            col_stats = {
                'count': count,
                'mean': mean,
                'min': min(numeric_values),
                'max': max(numeric_values),
                'std_dev': std_dev
            }
        else:
            value_counts = Counter(values)
            col_stats = {
                'count': count,
                'min': min(values),
                'max': max(values),
                'unique_count': len(value_counts),
                'most_common': value_counts.most_common(1)
            }

        stats[col] = col_stats

    return stats

def aggregate_by(data, *group_keys):
    groups = defaultdict(list)
    for row in data:
        key = tuple(row[k] for k in group_keys)
        groups[key].append(row)
    return groups

def summarize_aggregates(data, *group_keys):
    agg = aggregate_by(data, *group_keys)
    return {k: compute_stats(v) for k, v in agg.items()}

if __name__ == '__main__':
    path = r'/Users/kushwanthmeesala/Downloads/2024_fb_ads_president_scored_anon 2.csv'
    data = read_csv(path)

    print("\n== Overall Dataset Statistics ==")
    print(compute_stats(data))

    print("\n== Aggregated by page_id ==")
    print(summarize_aggregates(data, "page_id"))

    print("\n== Aggregated by page_id and ad_id ==")
    print(summarize_aggregates(data, "page_id", "ad_id"))