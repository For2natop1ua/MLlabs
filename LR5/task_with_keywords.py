import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean
from difflib import SequenceMatcher


df_norm = pd.read_csv('videos_normalized.txt', sep=' ', dtype={'Video': str})
df_orig = pd.read_csv('videos_corrected.txt', sep=' ', dtype={'Video': str})
df_keywords = pd.read_csv('videos_with_keywords.txt', sep=' ', quotechar='"', dtype={'Video': str})
time_min, time_max = df_orig['Time_s'].min(), df_orig['Time_s'].max()
pos_min, pos_max = df_orig['Positive_count'].min(), df_orig['Positive_count'].max()
neg_min, neg_max = df_orig['Negative_count'].min(), df_orig['Negative_count'].max()


def string_similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def contains_keyword(user_words, video_words):
    user_set = set(user_words)
    video_set = set(video_words)
    return len(user_set & video_set) > 0


def recommend_with_keywords_priority(time, pos, neg, user_keywords, df_norm, df_orig, df_keywords, top_n=5):
    norm_time = (time - time_min) / (time_max - time_min) if time_max != time_min else 0
    norm_pos = (pos - pos_min) / (pos_max - pos_min) if pos_max != pos_min else 0
    norm_neg = (neg - neg_min) / (neg_max - neg_min) if neg_max != neg_min else 0
    input_vec = np.array([norm_time, norm_pos, norm_neg])
    user_keywords = user_keywords.strip().lower()
    user_words = [word.strip() for word in user_keywords.split() if word.strip()]
    with_keywords = []
    without_keywords = []
    for _, row in df_norm.iterrows():
        video_id = row['Video']
        row_vec = np.array([row['Time_s'], row['Positive_count'], row['Negative_count']])
        dist = euclidean(input_vec, row_vec)
        video_kw_row = df_keywords[df_keywords['Video'] == video_id]
        if video_kw_row.empty:
            continue
        video_kw_raw = str(video_kw_row['Keywords'].iloc[0])
        video_kw = video_kw_raw.strip().strip('"').strip("'")
        video_words = [word.strip().strip('"\'') for word in video_kw.split() if word.strip()]
        sim = string_similarity(user_keywords, video_kw)
        candidate = {
            'video': video_id,
            'time_s': int(df_orig[df_orig['Video'] == video_id].iloc[0]['Time_s']),
            'positive': int(df_orig[df_orig['Video'] == video_id].iloc[0]['Positive_count']),
            'negative': int(df_orig[df_orig['Video'] == video_id].iloc[0]['Negative_count']),
            'keywords': video_kw,
            'dist': round(dist, 4),
            'sim': round(sim, 3)
        }
        if user_words and contains_keyword(user_words, video_words):
            with_keywords.append(candidate)
        else:
            without_keywords.append(candidate)
    with_keywords = sorted(with_keywords, key=lambda x: x['dist'])
    without_keywords = sorted(without_keywords, key=lambda x: x['dist'])
    # ТОП-5: спочатку з ключовими словами, потім — решта
    result = with_keywords + without_keywords
    result = result[:top_n]
    for i, rec in enumerate(result, 1):
        rec['rank'] = i
    return result


if __name__ == "__main__":
    time = float(input("Час перегляду (сек): "))
    pos = float(input("Позитивні оцінки: "))
    neg = float(input("Негативні оцінки: "))
    keywords = input("Ключові слова (наприклад: action comedy): ")
    print("ТОП-5 РЕКОМЕНДАЦІЙ:")
    print(f"{'№':<3} {'Відео':<8} {'Час':<5} {'Поз':<6} {'Нег':<6} {'Відст':<7} {'Схожість':<9} {'Ключові слова'}")
    recs = recommend_with_keywords_priority(time, pos, neg, keywords, df_norm, df_orig, df_keywords)
    for rec in recs:
        print(f"{rec['rank']}.  {rec['video']:<8} {rec['time_s']:<5} {rec['positive']:<6} {rec['negative']:<6} "
              f"{rec['dist']:<7} {rec['sim']:<9} {rec['keywords']}")