# -*- coding: utf-8 -*-
"""
Create Time: 6/14/2021 2:34 PM
Author: Zhou

In demo.py I only choose the sentence that contain kinship
because I observed that all the information we need appear in such a sentence.
Here the sentence was further splited by ";" as I noticed each unit with a ";"
mostly contains one record

get the df like this:
id1 subsentence1 kinship
id1 subsentence2 kinship
id2 subsentence1 kinship
... ...

"""

import pandas as pd
from kinship_expression import sorted_kinship_final

df_kinship_sentence = pd.read_excel("demo_kinship3.0.xlsx", encoding = "utf-8")

df_sub_sentence = pd.DataFrame(columns=["id", "subsentence"])
print("------------subsentence-----------------")
for idx, row in df_kinship_sentence.iterrows():
    if idx % 10 == 0:
        print(idx)
    sentence2subsentences = row["sentence"].split("；")
    # print(sentence2subsentences)
    for item in sentence2subsentences:
        df_to_be_added = {"id":row["id"], "subsentence": item}
        df_sub_sentence = df_sub_sentence.append(df_to_be_added, ignore_index=True)
# print(df_sub_sentence.head())
df_sub_sentence.to_excel("subsentence.xlsx", encoding="utf-8")

# extract kinship from kinship_sub_sentence
df_sub_sentence["kinship"] = ""
print("-----------------extract kinship-----------------")
for idx, row in df_sub_sentence.iterrows():
    if idx % 10 == 0:
        print(idx)
    for item in sorted_kinship_final:
        if item in row["subsentence"]:
            df_sub_sentence.loc[idx, "kinship"] = item
            break

print(df_sub_sentence.head())

# delete duplicate rows
df_sub_sentence = df_sub_sentence.drop_duplicates()

print(len(df_sub_sentence))


df_sub_sentence.to_excel("kinship_subsentence3.1.xlsx", encoding="utf-8")


