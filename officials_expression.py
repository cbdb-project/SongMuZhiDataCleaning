# -*- coding: utf-8 -*-
"""
Create Time: 6/14/2021 4:16 PM
Author: Zhou

Generate the officials_list from officials.txt

"""

with open("officials.txt", encoding="utf-8") as file:
    officials_raw = file.readlines()

officials_renew1 = []
print(officials_raw)
for item in officials_raw:
    if "#" in item:
        officials = item.split("#")
        officials_renew1 += officials
    else:
        officials_renew1.append(item)

officials_renew2 = [item.strip() for item in officials_renew1]
officials_renew3 = [item for item in officials_renew2 if len(item)>0 ]
officials_renew4 = list(set(officials_renew3))
print(officials_renew4)



