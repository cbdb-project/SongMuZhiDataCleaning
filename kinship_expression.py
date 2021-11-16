# -*- coding: utf-8 -*-
"""
Create Time: 6/6/2021 4:16 PM
Author: Zhou

1. Generate kinship list from kinship.txt (for male) and kinship_extend.txt(for female)
2. Sort the kinship list by the length of each element,
to avoid "烈祖" cannot be extracted after "祖" being extracted
This method can be optimized
3. Output the sorted_kinship_final list for further work

"""

kinship_raw = []

# kinship.txt can also be used here
with open("kinship_extend.txt", encoding="utf-8") as f:
    kinship_raw = f.readlines()

kinship_final = list(set(kinship_raw))    # remove duplicates
# print(kinship_final)
kinship_final = [item.strip() for item in kinship_final if not "wsep" in item] # delete \n
kinship_final.remove("kin")
kinship_final.remove("")
# print(kinship_final)
# print(len(kinship_final))

# add some kinship expressions
kinship_final.append("夫人")
kinship_final.append("七代祖")
kinship_final.append("烈祖")

# sort kinship_final
sorted_kinship_final = sorted(kinship_final, key=lambda i:len(i), reverse=True)

print(sorted_kinship_final)