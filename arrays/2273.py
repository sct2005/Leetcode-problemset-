words = ["abba","baba","bbaa","cd","cd"]


def soultion_1(words): #O(n^2)
    for i in words:
        for k in words:
            if sorted(i) == sorted(k):
                words.remove(k)

    print(words)

soultion_1(words)

