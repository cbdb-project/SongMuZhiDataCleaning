# -*- coding: utf-8 -*-
"""
Create Time: 6/15/2021 2:35 PM
Author: Zhou

Extract officials from sub_sentence.py's output
get the df like this:
id1 subsentence1 kinship officials
id1 subsentence2 kinship officials
id2 subsentence1 kinship officials
... ...

"""

from officials_expression import officials_renew4
import pandas as pd

df_kinship_officials = pd.read_excel("kinship_subsentence3.1.xlsx", encoding = "utf-8")

df_kinship_officials["officials"] = ""

for idx, row in df_kinship_officials.iterrows():
    if idx % 10 == 0:
        print(idx)
    for item in officials_renew4:
        if item in row["subsentence"]:
            df_kinship_officials.loc[idx, "officials"] = item
            break

print(df_kinship_officials.head())

df_kinship_officials.to_excel("kinship_officials3.0.xlsx", encoding="utf-8")