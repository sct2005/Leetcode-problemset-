s = "anagram"

t = "nagaram"


def anagram (s,t):
    if sorted(s) == sorted(t):  #--- sorted will just sort them in alpahbetical order
        print(True)#- so if truly an anagram once sorted it should be the same 
    else:
        print(False)


anagram(s,t)
