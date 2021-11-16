# -*- coding: utf-8 -*-
"""
Create Time: 6/8/2021 10:13 PM
Author: Zhou

The original demo to generate a .xlsx with colomns: id(content id), kinship and sentence
ONLY choose 100 rows from qsw_muzhi.xlsx to test the idea

1. Read the qsw_muzhi.xlsx, seperate the content col by "。",
    get the df like this:
    id1 sentence1
    id1 sentence2
    id1 sentence3
    id2 sentence1
    ... ...
2. Select the sentences that contain kinship expression
    get the df like this:
    id1 kinship sentence1 (suppose that sentence2, sentence3 do not contain kinship)
    id2 kinship sentence1
    ... ...
"""

from kinship_expression import sorted_kinship_final
import pandas as pd

df_text = pd.read_excel("qsw_muzhi.xlsx", encoding = "utf-8", nrows = 100)

# separate text into sentences by 。
df_sentences = pd.DataFrame(columns=["id", "sentence"])
print("------------separate sentences--------------")
for idx, row in df_text.iterrows():
    if idx % 10 == 0:
        print(idx)
    text2sentences = row["content"].split("。")
    # print(type(text2sentences))
    # print(type(text2sentences[0]))
    for item in text2sentences:
        df_to_be_added = {"id":row["content_id"], "sentence":item}
        # print(df_to_be_added)
        df_sentences = df_sentences.append(df_to_be_added, ignore_index=True)

print(df_sentences.head())
print(len(df_sentences))

# select sentences that contain kinship expression
df_kinships = pd.DataFrame(columns=["id", "kinship", "sentence"])
print("----------------extract kinships----------------------")
for idx, row in df_sentences.iterrows():
    if idx % 100 == 0:
        print(idx)
    for item in sorted_kinship_final:
        if item in row["sentence"]:
            df_to_be_added = {"id": row["id"], "kinship":item, "sentence":row["sentence"]}
            # print(df_to_be_added)
            df_kinships = df_kinships.append(df_to_be_added, ignore_index=True)
            break

print(df_kinships.head())
print(len(df_kinships))
df_kinships.to_excel("demo_kinship3.0.xlsx", encoding = "utf-8")




