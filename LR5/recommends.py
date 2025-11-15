import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean

df_norm = pd.read_csv('videos_normalized.txt', sep=' ')
df_orig = pd.read_csv('videos_corrected.txt', sep=' ')
time_min, time_max = df_orig['Time_s'].min(), df_orig['Time_s'].max()
pos_min, pos_max = df_orig['Positive_count'].min(), df_orig['Positive_count'].max()
neg_min, neg_max = df_orig['Negative_count'].min(), df_orig['Negative_count'].max()


def recommend_videos(time, pos, neg, df_norm, df_orig, top_n=5):
    norm_time = (time - time_min) / (time_max - time_min) if time_max != time_min else 0
    norm_pos = (pos - pos_min) / (pos_max - pos_min) if pos_max != pos_min else 0
    norm_neg = (neg - neg_min) / (neg_max - neg_min) if neg_max != neg_min else 0
    input_vec = np.array([norm_time, norm_pos, norm_neg])
    distances = []
    for idx, row in df_norm.iterrows():
        row_vec = np.array([row['Time_s'], row['Positive_count'], row['Negative_count']])
        dist = euclidean(input_vec, row_vec)
        distances.append((dist, row['Video']))
    recommendations = sorted(distances, key=lambda x: x[0])[:top_n]
    result = []
    for i, (dist, video_id) in enumerate(recommendations, 1):
        orig_row = df_orig[df_orig['Video'] == video_id].iloc[0]
        result.append({
            'rank': i,
            'video': video_id,
            'time_s': int(orig_row['Time_s']),
            'positive': int(orig_row['Positive_count']),
            'negative': int(orig_row['Negative_count']),
            'distance': round(dist, 4)
        })
    return result


if __name__ == "__main__":
    time = float(input("Введіть час перегляду (сек): "))
    pos = float(input("Введіть кількість позитивних оцінок: "))
    neg = float(input("Введіть кількість негативних оцінок: "))
    print("ТОП-5 РЕКОМЕНДАЦІЙ:")
    print(f"{'№':<3} {'Відео':<8} {'Час':<6} {'Позитив':<8} {'Негатив':<8} {'Відстань'}")
    recs = recommend_videos(time, pos, neg, df_norm, df_orig)
    for rec in recs:
        print(
            f"{rec['rank']}.  {rec['video']:<8} {rec['time_s']:<6} "
            f"{rec['positive']:<8} {rec['negative']:<8} {rec['distance']}")
