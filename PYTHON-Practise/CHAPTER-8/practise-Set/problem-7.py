#Python function to remove a given word from a list and strip it at the same time.

l = ["Mandar","Yogiraj","Yogi","yash","raj"]

def rem(l,word):
    for item in l:
        l.remove(word)
        return l
    
print(rem(l,"yash"))

def strip_word(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    
print(strip_word(l,"raj"))

