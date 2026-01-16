alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
charecters = "!@£$%^&*():;'><? "
sentance1 = "cat is a feline"
sentance2 ="cat5 ar8 "

sentences = [sentance1,sentance2]

for sentance in sentences:
    for i in sentance:
        if i in charecters or numbers:
            print("theres a non valid chaerter in this sentance")
            break
        else:
            continue
