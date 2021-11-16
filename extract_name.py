# -*- coding: utf-8 -*-
"""
Create Time: 6/15/2021 7:27 PM
Author: Zhou

Extract name from extract_officials.py's output
For first name,
I suppose that the string between kinship keyword and "," is the first name
For last name,
Add last name from contendID_subject.xlsx by id-传主
"""

import pandas as pd
df_kinship_officials_name = pd.read_excel("kinship_officials3.0.xlsx", encoding = "utf-8")

# extract first name
df_kinship_officials_name["first_name"] = ""
for idx, row in df_kinship_officials_name.iterrows():
    if idx % 10 == 0:
        print(idx)
    kinship = str(row["kinship"])
    subsentence = str(row["subsentence"])
    if kinship != "nan" and "，" in subsentence:
        begin = subsentence.index(kinship) + len(kinship)
        end = subsentence.index("，")
        if (end - begin) <= 3:  # cannot be applied to shaoshuminzu
            df_kinship_officials_name.loc[idx, "first_name"] = subsentence[begin:end]

# extract last name
# 1. generate the dict {content id: last name of the subject}
df_last_name = pd.read_excel("contentID_subject.xlsx", encoding = "utf-8")
last_name_dict = {}
for idx, row in df_last_name.iterrows():
    last_name_dict[row["content_id"]] = row["subject"][0]
print(last_name_dict)

# 2. match the last name by content id
df_kinship_officials_name["last_name"] = ""
for idx, row in df_kinship_officials_name.iterrows():
    if idx % 10 == 0:
        print(idx)
    df_kinship_officials_name.loc[idx, "last_name"] = last_name_dict[row["id"]]


print(df_kinship_officials_name.head())

df_kinship_officials_name.to_excel("kinship_officials_name3.0.xlsx", encoding="utf-8")