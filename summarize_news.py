import pandas as pd
from openai_chatgpt import complete_chat
# sol 1. 依照每一行去做處理
# news = pd.read_csv("news.csv")
# records = news.to_dict(orient='records')
# for record in records[:5]:
#     print(record['title'])

# sol 2.
news = pd.read_csv("news.csv")
groups = news.groupby('topic_id')
for gid, group in groups:
    print(list(group['title']), '\n')
