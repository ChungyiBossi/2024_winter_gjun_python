import pandas as pd
from openai_chatgpt import complete_chat
# sol 1. 依照每一行去做處理
# news = pd.read_csv("news.csv")
# records = news.to_dict(orient='records')
# for record in records[:5]:
#     print(record['title'])

# sol 2.
news = pd.read_csv("news.csv")
groups = news.groupby('topic_id')  # 依照 topic_id 分組 = 同 topic_id 為一組
for gid, group in groups:
    temp = list(group['title'])
    message = "\n".join(temp)  # list -> string
    print(message)
    summarization = complete_chat(message)
    print("Summarization = ", summarization, '\n')
