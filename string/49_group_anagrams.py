
# strs = ["eat","tea","tan","ate","nat","bat"]
# aList = []
# temp_row = ['*']
# # for i in strs:
# #     for k in strs:
# #         if i != k:
# #             if sorted(i) == sorted(k):
# #                 for j in aList:
# #                     if i 
# #                 aList.append(temp_row)
# temp = []
# for i in strs:
# for k in aList:
# if i not in aList:
# if sorted(i) == sorted((k[0])):
# k.append(i)
# else:
# aList.append(temp_row)
#                 (aList("*")).append(i)


strs = ["eat","tea","tan","ate","nat","bat"]
aList = []
for word in strs:
    placed = False
    
    for group in aList:
        
        if sorted(word) == sorted((group[0])):
            group.append(word)
            placed = True
            break
    if not placed:
        aList.append([word])
print(aList)
   
#our idea was perfect and most of thge frame work was in place , it was more the sytx as we knew what needed to be doen we were just overcomplicating it 
