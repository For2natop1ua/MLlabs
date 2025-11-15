import pandas as pd
import random

df = pd.read_csv('videos_corrected.txt', sep=' ')

keywords_pool = [
    "action", "adventure", "comedy", "drama", "horror", "thriller", "sci-fi", "fantasy",
    "romance", "animation", "documentary", "music", "sports", "gaming", "cooking", "travel",
    "fitness", "tech", "vlog", "tutorial", "review", "news", "kids", "animals", "cars", "asmr"
]

random.seed(42)
df['Keywords'] = [
    ' '.join(random.sample(keywords_pool, k=random.randint(2, 4)))
    for _ in range(len(df))
]

df.to_csv('videos_with_keywords.txt', sep=' ', index=False)
print("Файл videos_with_keywords.txt створено.")