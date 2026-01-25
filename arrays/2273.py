
words = ["abba","baba","bbaa","cd","cd"]



def array_alter(words):
    for word in words:
            

        if sorted(word) in words:
            words.remove(word)
            print("a")
        else:
            continue


array_alter(words)


            


        
    
